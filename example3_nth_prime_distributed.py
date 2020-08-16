import distributedpython

payload = "[10, 100, 1000, 10000, 20000, 30000, 40000, 50000]"
function = """
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
            prime_numbers[len(prime_numbers)] = i
        if(len(prime_numbers)==n):
            break
    progress()
    return (f"{n}th Prime Number is: {prime_numbers[n-1]}")
"""

distributedpython.run(payload, function)