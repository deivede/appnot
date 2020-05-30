import tweepy

def taketts():

    lasttw = open("lasttw.txt", "r")
    put = lasttw.read()
    lasttw.close()

    auth = tweepy.OAuthHandler("7TPANllmOdForjljyewaYkLpt", "am0DqUHc75sxTwKND1uqsABLNtMDzZ7LAb1gLQW8vJJtOJMFLq")
    auth.set_access_token("53538435-wbsRePsZhHyGDTf4PXxo5xHkr8gB2bePtzu18xmD7",
                          "A2huzhminJJxd2tky3VBsZFM1F8MlgSi1WomiTWJ9yewI")

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



