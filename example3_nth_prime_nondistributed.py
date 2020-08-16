import time

a = [10, 100, 1000, 10000, 20000, 30000, 40000, 50000]

def myfunction(n):
    prime_numbers = [2,3]
    i=3
    while (True):
        i+=1
        status = True
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                status = False
                break
        if(status==True):
            prime_numbers.append(i)
        if(len(prime_numbers)==n):
            break
    print(f"{n}th Prime Number is: {prime_numbers[n-1]}")

current = time.time()

for x in a:
    myfunction(x)
    print(time.time() - current)