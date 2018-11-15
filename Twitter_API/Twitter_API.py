from twitter import OAuth, TwitterStream
from flask import Flask,request,jsonify
import json
import pandas as pd
app=Flask(__name__)
name = []
text=[]
retweet=[]
status_count=[]
file_data={}
@app.route('/data',methods=['POST'])
def hello():

   if request.method == "POST":
       data = request.get_data(cache =False, as_text = True)
       load_data = json.loads(data)

       CKey = load_data["CKey"]
       CSecret = load_data["CSecret"]
       AToken = load_data["AToken"]
       ASecret = load_data["ASecret"]
       filter = load_data["filter"]


       oauth = OAuth(AToken, ASecret, CKey, CSecret)

       twitter_stream = TwitterStream(auth=oauth)

       get_data = twitter_stream.statuses.filter(track='change')

       tweet_count = 100
       for tweet in get_data:
           tweet_count -= 1


          # print(tweet['user']['screen_name'],tweet['text'])
           name.append(tweet['user']['screen_name'])
           text.append(tweet['text'])
           retweet.append(tweet['retweet_count'])
           status_count.append(tweet['user']['statuses_count'])
           print("name:", name)
           print("text:", text)
           file_data={"name":name,"text":text,"retweet":retweet,"status":status_count}
           file=pd.DataFrame(file_data)
           file.to_csv('FinalData.csv',index=False)

           if tweet_count <= 0:
               break


   return jsonify({"name":name,"tweets":text,"retweet":retweet,"status":status_count})

if __name__ == '__main__':
    app.run(debug=True)


