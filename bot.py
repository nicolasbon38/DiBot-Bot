from auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
list_di = ['di', 'dhi', 'dy']
bad_chars = [';', ':', '!', "*", '.']
compte = 'EmmanuelMacron'

def reply_to_tweet(tweetId, username, content):
    api.update_status('@{} {} !'.format(username, content), in_reply_to_status_id=tweetId)


def get_last_tweets_from_user(username):
    tweets = api.user_timeline(screen_name=username, count=199, include_rts=False, tweet_mode='extended')
    return tweets

def analyze_tweet(status):
    text = status.full_text
    words = text.split(' ')
    last_word = words[len(words)-1]

    if 'di' in last_word and 'di' != last_word[-2:]:
        content = get_what_to_say(''.join(i for i in last_word if not i in bad_chars))
        if content:
            try: 
                print(content)
                print(text)
                #reply_to_tweet(status.id, compte, content)
            except tweepy.error.TweepError:
                pass

def get_what_to_say(word):
    i = 0
    while i < len(word) - 1 and (word[i] != 'd' or word[i + 1] != 'i'):
        i += 1
    if i == len(word) - 1:
        raise ValueError

    if len(word[i + 2:]) <= 1:
        return None
    return word[i + 2:]


def main():
    tweets = get_last_tweets_from_user(compte)
    for tweet in tweets:
        analyze_tweet(tweet)

main()