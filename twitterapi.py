import tweepy
from twkeys import *

def taketts(usr):

    def takeusr(slct_usr):

        usrdb = {
           "playactionfa": "3344165463",
            "deivede73": "53538435"
        }

        usuario = slct_usr
        return usrdb[usuario]

    idusr = takeusr(usr)

    txtdb =   usr + ".txt"

    ntxtdb =  usr + "NWT.txt"

    lasttw = open(txtdb, "r")
    put = lasttw.read()
    lasttw.close()

    auth = tweepy.OAuthHandler(oauthkey, oauthskey)
    auth.set_access_token(tokkey, tokskey)

    api = tweepy.API(auth)


    new_tweets = api.user_timeline(since_id=put, user_id=idusr)

    nw_tweets = len(new_tweets)

    strnt = str(nw_tweets)

    if nw_tweets != 0:
        ult = new_tweets[0].id_str
    else:
        ult = put

    if put is not ult:
      lasttw2 = open(txtdb, "w")
      lasttw2.write(ult)
      lasttw2.close()

    newt = open(ntxtdb, "w")
    newt.write(strnt)
    newt.close()

    pictt = {
        "ntw": strnt
    }

    return pictt
