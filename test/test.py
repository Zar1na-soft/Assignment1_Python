from src import *
num = int(input("Put number: "))
sumnum = 0
while sumnum < num:
    print(sumnum+1,"-", answer[sumnum]['name'], answer[sumnum]['market_cap'])
    sumnum += 1