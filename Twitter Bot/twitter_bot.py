import tweepy
import time

# print(dir(tweepy.API.mentions_timeline))
Consume_Key = ''
Consume_Secret = ''
Access_Key = ''
Access_Secret = ''

auth = tweepy.OAuthHandler(Consume_Key, Consume_Secret)
auth.set_access_token(Access_Key, Access_Secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
#
#
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    print(last_seen_id)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    # mentions = api.mentions_timeline()
    # print(mentions)
    # print(mentions[0].__dict__.keys())
    for mention in reversed(mentions):
        print(str(mention.id) + ' ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!', flush=True)
            print('Rresponding back', flush=True)
            api.update_status('@' + mention.user.screen_name +'#HelloWorld Respond back!!', mention.id)

while True:
    tweets()
    time.sleep(15)
