import random
import matplotlib.pyplot as plt
def sum7(n):
    count=0
    for i in range(1,n):
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        if dice1+dice2==7:
            count= count + 1
    return count/(n-1)
rolls=int(input('enter number of rolls: '))
trials=int(input('enter number of trails'))

average=[]
sum=0
for i in range(1,trials+1):
    result=sum7(rolls)
    sum=sum+result
    average.append(sum/i)
plt.plot(average, label='Estimated probability')
plt.axhline(y=1/6, label='actual value', color='r',linestyle='--' )
plt.xlabel('Number of trails')
plt.ylabel('probability of gettinf sum = 7')
plt.title('convergence of getting sum = 7 in dice')
plt.grid(True)
plt.legend()
plt.show()

