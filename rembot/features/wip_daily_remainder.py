from rembot.services import scheduler
from rembot.services import telegram
from rembot.services import remnote

REMAIND_TAG = 'WIP'
HEADER = "Good Morning! 🌞☕\nThis is your work in progress:\n"
BULLET_TEMPLATE = ' • {0}'
CRONTAB = '0 7 * * 0-5'


async def start(events):

    async def bullet_list_for_tagged_rems(tag_name):
        children = list()
        tag = await remnote.get_by_name(tag_name)
        for child in tag['tagChildren']:
            child = await remnote.get(child)
            child = child['name']
            if len(child) > 0:
                child = child[0]
                child = BULLET_TEMPLATE.format(child)
                children.append(child)
        return '\n'.join(children)

    async def send_rems_tagged_to_remaind():
        bullet_list = await bullet_list_for_tagged_rems(REMAIND_TAG)
        message = HEADER + bullet_list
        print('wip_daily_remainder')
        await telegram.send_message(message)

    scheduler.schedule(send_rems_tagged_to_remaind, CRONTAB)