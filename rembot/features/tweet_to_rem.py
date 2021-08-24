from rembot.services import remnote
from rembot.services import twitter
from rembot.services import scheduler

INBOX_REM = 'q5MhuXuBri2tn4qc5'
TRACKED_TWITTER_USER_IDS = ['1404389153941381121']
CRONTAB = '0/5 * * * *'
_users_last_tweet = dict()


async def start(events):

    def get_latest_tweets(user_id):
        global _users_last_tweet
        last_tweet = _users_last_tweet.get(user_id)
        tweets = twitter.get_tweets_from(user_id, since=last_tweet)
        if tweets and len(tweets):
            last_tweet = tweets[0]['id']
            _users_last_tweet[user_id] = last_tweet
            return tweets
        return []

    def tweet_to_rem_text(tweet):
        return f"{tweet['text']} https://twitter.com/i/web/status/{tweet['id']}"

    async def create_rem_from_tweets(*args, **kwargs):
        for user_id in TRACKED_TWITTER_USER_IDS:
            for tweet in get_latest_tweets(user_id):
                rem = tweet_to_rem_text(tweet)
                await remnote.create(INBOX_REM, rem)

    scheduler.schedule(create_rem_from_tweets, CRONTAB)
