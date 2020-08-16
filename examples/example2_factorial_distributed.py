import distributedpython

payload = "[1, 10, 100, 1000, 10000, 100000]"
function = """
def myfunction(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    progress()
    return (f"{num}! = {factorial}")
"""

distributedpython.run(payload, function)