from rembot import run

from rembot.services import telegram
from rembot.services import scheduler
from rembot.services import remnote
from rembot.services import heroku_keep_alive

from rembot.features import reply_telegram_with_rem
from rembot.features import wip_daily_remainder


services = scheduler, telegram, remnote#, heroku_keep_alive
features = reply_telegram_with_rem, wip_daily_remainder

run(services, features)