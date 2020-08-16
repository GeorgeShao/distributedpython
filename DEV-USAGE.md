# DistributedPython - DEV-USAGE.md

### Environment Setup
1. Create DCP account at [http://distributed.computer/](http://distributed.computer/).
2. Download your bank keystore file (from [http://distributed.computer/](http://distributed.computer/)) and name it "default.keystore" in a new ".dcp" folder in your root directory.
3. Generate a id.keystore file (on the [http://distributed.computer/](http://distributed.computer/) website) and put it in the same ".dcp" folder in your root directory.
4. Clone this repository using git.
5. ```npm i dcp-client``` to install dependencies.
6. ```pip install javascripthon``` to install dependencies.

### Library Install
```python setup.py install``` to install library locally

### Library Uninstall
```pip uninstall distributedpython``` to uninstall library

### How to Use
1. Create a new Python file
2. Type ```import distributedpython``` at the top of the file.
3. Type ```payload = "[INSERT_YOUR_PAYLOAD_HERE]"```, replacing "[INSERT_YOUR_PAYLOAD_HERE]" with your array that you want to deploy to DCP.
4. Type ```function = """[INSERT_YOUR_FUNCTION_HERE]"""```, replacing "[INSERT_YOUR_FUNCTION_HERE]" with your Python code that you want to deploy to DCP. Please note that the function string can be multiple lines.
5. Type ```distributedpython.run(payload, function)```.
6. Run the file!