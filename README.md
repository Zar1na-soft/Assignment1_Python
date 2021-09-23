# Assignment1_Python
First, we must obtain the data from coingecko.com
CoinGeckoAPI was imported from pycoingecko.
CoinGeckoApi() was used to pull the data, which was then named as a cg.
In cg.get_coins_market(), a list of all supported coins' prices, market capitalization, volume, and market data is stored.
All of this information was retrieved as an array by the report.
answer = cg.get_coins_markets(vs_currency='usd')
Using the following code, we can now obtain market capitalization.
answer[index]['market_cap']
