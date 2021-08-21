from rembot.services import remnote
from rembot.services import twitter
from rembot.services import scheduler

INBOX_REM = 'q5MhuXuBri2tn4qc5'
TWITTER_USER_ID = '1404389153941381121'
CRONTAB = '0 * * * *'
_last_tweet = None


async def start(events):

    def get_latest_tweets():
        global _last_tweet
        tweets = twitter.get_tweets_from(TWITTER_USER_ID, since=_last_tweet)
        if tweets and len(tweets):
            _last_tweet = tweets[0]['id']
            return tweets
        return []

    def tweet_to_rem_text(tweet):
        return f"{tweet['text']} https://twitter.com/i/web/status/{tweet['id']}"

    async def create_rem_from_tweets(*args, **kwargs):
        for tweet in get_latest_tweets():
            rem = tweet_to_rem_text(tweet)
            await remnote.create(INBOX_REM, rem)

    scheduler.schedule(create_rem_from_tweets, CRONTAB)
