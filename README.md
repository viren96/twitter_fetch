# twitter_fetch
1. Create a virutal environemt. (Can follow https://www.ginkgobioworks.com/2021/02/04/creating-a-rest-api-using-django-rest-framework/)
2. Install the packages from requirements file.


API CALL
http://127.0.0.1:8000/api/v1/twitter_stats/?word=bhiwandi&from_date=20220222&to_date=20220223

Output:
{
    "word": "bhiwandi",
    "tweet_count": 150,
    "retweet_count": 606,
    "like_count": 167,
    "quote_count": 3
}


<img width="770" alt="image" src="https://user-images.githubusercontent.com/25107964/155691625-bd74e315-ebba-43e9-bbcd-43b785ff54da.png">
