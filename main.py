from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
report = cg.get_coins_markets(vs_currency='usd')
print(report)

num = int(input("Put number: "))
sumnum = 0
while sumnum < num:
    sumnum += 1
    print(sumnum,"-", report[sumnum]['name'], report[sumnum]['market_cap'])

