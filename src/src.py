from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
answer = cg.get_coins_markets(vs_currency='usd')
print(answer)



