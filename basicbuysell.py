import random
import matplotlib.pyplot as plt

def sim(n):
    cash=0
    stock=0
    price=100
    drift = -0.05
    volatility = 1
   
    prices=[]
    prices.append(price)

    for i in range(n):
        price += drift + random.gauss(0, volatility)
        if len(prices) >= 5:
            avg = sum(prices[-5:]) / 5
        else:
            avg = sum(prices) / len(prices)

        if price > avg:
            cash-=price
            stock+=1
        else:
            cash+=price
            stock-=1
           
        prices.append(price)
    profitloss=cash+stock*price
    return profitloss
x=int(input('enter number of pricevariations: '))
trails=int(input('number of trails'))

pricelist=[]
for i in range(1,trails+1):
    pricelist.append(sim(x))

plt.plot(pricelist, label='profit and loss')
plt.axhline(y=0,label='neutral',color='r',linestyle='--')
plt.xlabel('trials')
plt.ylabel('cash')
plt.title('Stochastic Market Simulator with Strategy Backtesting and PnL Analysis')
plt.legend()
plt.show()
