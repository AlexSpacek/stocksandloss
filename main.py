from scraper import stock_daily
from analyzer import Analyzer
TSLA = Analyzer(ticker='TSLA',data=stock_daily('TSLA').data)
#print(TSLA.ticker)
#TSLA.profit(methodName='simple',capitalForEachTrade=5000)
testBuy = TSLA.methodBuy_Simple()
print(testBuy)
testSell = TSLA.methodSell_Simple()
print(testSell)