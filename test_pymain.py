import distributedpython

payload = "[\"red\", \"orange\", \"yellow\", \"green\", \"blue\", \"purple\"]"
function = """
def(colour){
    print(colour)
    progress()
    return colour
}
"""

distributedpython.run(payload=payload, function=function)