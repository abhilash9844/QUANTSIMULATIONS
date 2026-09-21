import random
def random_varibale(x):

    if(x<1/3.0):
        z=10
    elif(x>(1/3.0) and x<(2/3.0)):
        z=5
    else:
        z=1
    return z

def rngenerator():
    return random.random()
def experiment(n):
    sum=0
    
    for i in range(n):
        y=rngenerator()
        x=random_varibale(y)
        if(x==10):
             sum+=x*(3/8.0)
        elif(x==5):
             sum+=x*(9/8.0)
        else:
             sum+=x*(3/2.0)     
       
    return sum/n*1.0
n=int(input("Enter the no of Iteration: "))
z=experiment(n)
print("\nTHE EXPERIMENT VALUE OF E_Q(X) is : ",z)
print("\nTHE THEORYTICAL VALUE OF E_Q(X) is : ",29/8)
#I have consider the probability measure Q[1/8,3/8,1/2] because we know that 
#a person always tries to spend less money and it is not P[1/3,1/3,1/3] like in 
#previous case 
