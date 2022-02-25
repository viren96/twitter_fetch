from django.core.cache import cache
from . import utils


def my_api_cache(function):
    """
    cache of 1 hour if current date (as result may change) else cache for 7 days.
    """
    def wrapper(*args, **kw):
        key = function.__name__ + str(args)

        current_date_time = utils.get_current_date_iso()

        response = cache.get(key, 'NOT_FOUND')
        if response == 'NOT_FOUND':
            response = function(*args, **kw)
            if response is not None:
                if args[2] != current_date_time:
                    cache.set(key, response, 24 * 60 * 60* 7)  # 7 day cache
                else:
                    cache.set(key, response, 24 * 60) # cache for 1 hour
            return response
        else:
            print("caching present for key:" + key)
            return response
    return wrapper


