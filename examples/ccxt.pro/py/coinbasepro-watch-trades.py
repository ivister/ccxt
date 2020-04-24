# -*- coding: utf-8 -*-

import ccxtpro
import asyncio

async def main(loop):
    exchange = ccxtpro.coinbasepro({'enableRateLimit': False, 'asyncio_loop': loop})
    method = 'watchTrades'
    print('CCXT Pro version', ccxtpro.__version__)
    if exchange.has[method]:
        while True:
            try:
                trades = await exchange.watch_trades('BTC/USD')
                num_trades = len(trades)
                trade = trades[-1]
                print(exchange.iso8601(exchange.milliseconds()), trade['symbol'], trade['datetime'], trade['price'], trade['amount'], num_trades, 'in cache')
            except Exception as e:
                print(e)
                await exchange.close()
    else:
        raise Exception(exchange.id + ' ' + method + ' is not supported or not implemented yet')

loop = asyncio.new_event_loop()
loop.run_until_complete(main(loop))