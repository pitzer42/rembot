from aiohttp import web


async def enable(events):
    print('heroku keep alive 1')
    
    async def handle(request):
        print('heroku keep alive 3')
        return web.Response(text='rembot')

    app = web.Application()
    app.add_routes([web.get('/', handle)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner)    
    await site.start()
    print('heroku keep alive 2')
