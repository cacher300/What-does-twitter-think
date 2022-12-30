import pandas as pd
import tweepy
consumer_key = ""
consumer_secret = ""
access_token = "-"
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#api.update_status("Hdddsdello Tweepy")

keywords = 'canucks'
limit=1000

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

with open('tweets.txt', 'w', encoding="utf-8") as f:
    dfAsString = df.to_string(header=False, index=False)
    f.write(dfAsString)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)

with open("tweets.txt", "r", encoding="utf-8") as file:
    #read content of file to string
    data = file.read()

def good_count_words(filename, search_filename):
    # Open the search file in read-only mode
    with open(search_filename, 'r', encoding="utf8") as search_file:
        # Read the entire search file into a single string
        search_text = search_file.read()

    # Split the search text into a list of search words
    search_words = search_text.split()

    # Open the file to be searched in read-only mode
    with open(filename, 'r', encoding="utf8") as f:
        # Read the entire file into a single string
        text = f.read()

    # Split the text into a list of words
    words = text.split()

    occurrences = []
    length = len(search_words)
    for i in range(length):
       occurrences.append(0)
    for i in range(len(search_words)):
      for j in words:
            if search_words[i] == j:
             occurrences[i] += 1

    return occurrences


def bad_count_words(badfilename, search_filename):
    # Open the search file in read-only mode
    with open(search_filename, 'r', encoding="utf8") as search_file:
        # Read the entire search file into a single string
        search_text = search_file.read()

    # Split the search text into a list of search words
    search_words = search_text.split()

    # Open the file to be searched in read-only mode
    with open(badfilename, 'r', encoding="utf8") as f:
        # Read the entire file into a single string
        text = f.read()

    # Split the text into a list of words
    words = text.split()

    occurrences = []
    length = len(search_words)
    for i in range(length):
       occurrences.append(0)
    for i in range(len(search_words)):
      for j in words:
            if search_words[i] == j:
             occurrences[i] += 1

    return occurrences


filename = "good.txt"
badfilename = "bad.txt"
search_filename = "tweets.txt"
good_word_count = good_count_words(filename, search_filename)
bad_word_count = bad_count_words(badfilename, search_filename)
print(sum(good_word_count))
print(sum(bad_word_count))



