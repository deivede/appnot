import tweepy
from twkeys import *

def taketts():

    lasttw = open("lasttw.txt", "r")
    put = lasttw.read()
    lasttw.close()

    auth = tweepy.OAuthHandler(oauthkey, oauthskey)
    auth.set_access_token(tokkey, tokskey)

    api = tweepy.API(auth)

    new_tweets = api.user_timeline(since_id=put)

    nw_tweets = len(new_tweets)

    strnt = str(nw_tweets)

    if nw_tweets != 0:
        ult = new_tweets[0].id_str
    else:
        ult = put

    if put is not ult:
      lasttw2 = open("lasttw.txt", "w")
      lasttw2.write(ult)
      lasttw2.close()

    newt = open("newt.txt", "w")
    newt.write(strnt)
    newt.close();

    return strnt
