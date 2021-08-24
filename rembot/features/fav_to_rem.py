from rembot.services import remnote
from rembot.services import twitter
from rembot.services import scheduler

INBOX_REM = 'q5MhuXuBri2tn4qc5'
TRACKED_TWITTER_USER_IDS = ['1404389153941381121']
CRONTAB = '0/5 * * * *'
_users_last_fav = dict()


async def start(events):

    def get_latest_favs(user_id):
        global _users_last_fav
        last_fav = _users_last_fav.get(user_id)
        favs = twitter.get_tweets_from(user_id, since=last_fav)
        if favs and len(favs):
            last_fav = favs[0]['id']
            _users_last_fav[user_id] = last_fav
            return favs
        return []

    def fav_to_rem_text(tweet):
        return f"{tweet['text']} https://twitter.com/i/web/status/{tweet['id']}"

    async def create_rem_from_favs(*args, **kwargs):
        for user_id in TRACKED_TWITTER_USER_IDS:
            for fav in get_latest_favs(user_id):
                rem = fav_to_rem_text(fav)
                await remnote.create(INBOX_REM, rem)

    scheduler.schedule(create_rem_from_favs, CRONTAB)
