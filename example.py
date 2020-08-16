import distributedpython

payload = "[\"red\", \"orange\", \"yellow\", \"green\", \"blue\", \"purple\"]"
function = """
def myfunction(colour):
    print(colour)
    progress()
    return colour
"""

distributedpython.run(payload, function)