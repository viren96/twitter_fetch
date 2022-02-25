from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import twitter
import json


@api_view()
def get_tweet_stats(request):
    try:
        args = request.GET if request.method=='GET' else json.loads(request.body.decode('UTF-8'))
        word = args['word']
        from_date = args['from_date']
        to_date = args['to_date']
        resp = twitter.get_twitter_stats(word,from_date,to_date)
        return Response(resp)
    except Exception as ex:
        print(str(ex))
        return Response({"status": "failed", "data": {"message": "Something went wrong."}})
