import distributedpython

payload = "[\"red\", \"orange\", \"yellow\", \"green\", \"blue\", \"purple\"]"
function = """
    def(colour){
        console.log(colour)
        progress()
        return colour
    }
"""

distributedpython.run(payload=payload, function=function)