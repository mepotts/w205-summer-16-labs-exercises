import tweepy

consumer_key = "BICrdK3Vj9xVNpr3Po9IssqTU";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "AlwXO6mXxZkuHwUvUlp4sn7OGkGub5gtPZmHMfrVe5E2Qd7Oxu";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "748586503362732033-KSzFNHkwWcx2ejMlOdxTSUednbu9uzZ";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "x88Dt83h3WbhZpiz4eORQNIPLWza4Npi8sH480oizGVpg";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



