from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
answer = cg.get_coins_markets(vs_currency='usd')
print(answer)

num = int(input("Put number: "))
sumnum = 0
while sumnum < num:
    print(sumnum+1,"-", answer[sumnum]['name'], answer[sumnum]['market_cap'])
    sumnum += 1

