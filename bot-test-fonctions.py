#Fichier pour tester les fonctions avec l'api de twitter
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "hcJVNswdLvpNRqCLmUDcqwspN"
consumer_secret = "EiUHT9yuPbamp7jElC63PYQDKxmNzLHSPAhU4idmDTK0SSfUlD"
access_token = "1402177276708544516-bxx2LjLGQeIyq7e09aeH2CWU3YKtpI"
access_token_secret = "BWWe2IfG6jW2F4G1LOlzNPGp02mSYi4k1kYFe27nX7BSb"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Nom du compte
screen_name = "testtwe49912384"

# Recuperer les abonnements du compte
c = tweepy.Cursor(api.friends, screen_name)

# Compte le nombre d'abonnoments
count = 0
for friends in c.items():
    count += 1
print(screen_name + " has " + str(count) + " friends.")

# Juste pour 30 abonnements
for friends in tweepy.Cursor(api.friends, screen_name).items(30):
    print(friends.screen_name)

# Envoi d'un poste
# api.update_status(status="test\n\ntesst")

#Recupere tous le potes avec mot clé
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=["femme", "gaming"], languages=["fr"]	)

# Rettweter un poste en fonction de l'id
# api.retweet(1402904878108844033)



