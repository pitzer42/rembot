from rembot import run

from rembot.services import telegram
from rembot.services import scheduler
from rembot.services import remnote
from rembot.services import twitter

from rembot.features import telegram_to_rem
from rembot.features import tweet_to_rem
from rembot.features import fav_to_rem
from rembot.features import wip_daily_remainder


services = scheduler, telegram, remnote, twitter
features = telegram_to_rem, tweet_to_rem, wip_daily_remainder

run(services, features)