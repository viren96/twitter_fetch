import requests
from . import utils
from . import decorators

#its bad practice to place your bearer token directly into the script (this is just done for illustration purposes)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALh2ZgEAAAAANOi7hZWDLX8YK2eIA57rQpTXrms%3DpaBHRg2fjnlOpMRubl7IEvsrfqjatSoALKIv6RFOaF2ZNLwNWZ"


def get_twitter_stats(word,from_date,to_date):
    try:
        retweet_count,tweet_count,like_count,quote_count = 0, 0, 0, 0
        no_of_days = utils.get_date_difference(from_date,to_date)
        for i in range(no_of_days+1):
            start_time = utils.generate_date_iso_from_string(from_date,i)
            end_time = utils.generate_date_iso_from_string(from_date,i+1)
            day_result = get_twitter_stats_each_day(word,start_time,end_time)
            tweet_count += day_result['tweet_count']
            retweet_count += day_result['retweet_count']
            like_count += day_result['like_count']
            quote_count += day_result['quote_count']

        result = {'word': word,'tweet_count': tweet_count,'retweet_count': retweet_count,'like_count':like_count, 'quote_count': quote_count}
        return result
    except Exception as ex:
        print(str(ex))
        return None


@decorators.my_api_cache
def get_twitter_stats_each_day(word,start_time,end_time):
    """
    Each day separate call so that we can cache the result of previous day for more time and for today for less time.
    """
    is_next = True
    resp = call_twitter_api(word, start_time, end_time)
    retweet_count,tweet_count,like_count,quote_count = 0, 0, 0, 0
    while is_next:
        meta_data = resp['meta']
        if meta_data['result_count'] > 0:
            tweets = resp['data']
            for tweet in tweets:
                tweet_count += 1
                retweet_count += tweet['public_metrics']['retweet_count']
                like_count += tweet['public_metrics']['like_count']
                quote_count += tweet['public_metrics']['quote_count']

        next_token = meta_data.get('next_token','')
        if next_token == '':
            is_next = False
        else:
            resp = call_twitter_api(word, start_time, end_time,next_token)
    result = {'tweet_count': tweet_count,'retweet_count': retweet_count,'like_count':like_count, 'quote_count': quote_count}
    return result



def call_twitter_api(query, start_time, end_time, next_token='', tweet_fields = 'public_metrics,geo', bearer_token = BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    if next_token != '':
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&start_time={}&end_time={}&next_token={}&tweet.fields={}".format(
        query, start_time, end_time, next_token, tweet_fields)
    else:
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&start_time={}&end_time={}&tweet.fields={}".format(
            query, start_time, end_time, tweet_fields)
    print(url)
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()