from aiohttp import web


async def enable(events):
    
    async def handle(request):
        return web.Response(text='rembot')

    app = web.Application()
    app.add_routes([web.get('/', handle)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner)    
    await site.start()
