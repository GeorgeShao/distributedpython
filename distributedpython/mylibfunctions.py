import subprocess
import os

def run(payload, function):
	try:
		process = subprocess.Popen(['python', '-m', 'metapensiero.pj', 'test_translation.py'], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
	except Exception as e:
		print("Exception:", e)

	placeholder_js_file = open("./distributedpython/placeholder_events.js", "r")
	example_js_file = open("./distributedpython/example_events.js", "r")
	main_js_file = open("./distributedpython/events.js", "w")
	placeholder_js_text = placeholder_js_file.read()
	placeholder_js_text = placeholder_js_text.replace("[PAYLOAD]", payload)
	placeholder_js_text = placeholder_js_text.replace("{FUNCTION}", function)
	main_js_file.write(placeholder_js_text)
	placeholder_js_file.close()
	example_js_file.close()
	main_js_file.close()

	try:
		process = subprocess.Popen(['node', './distributedpython/events.js', '--scheduler=https://demo-scheduler.distributed.computer/'], 
									stdout=subprocess.PIPE,
									stderr=subprocess.PIPE,
									universal_newlines=True)
	except Exception as e:
		print("Exception:", e)

	while True:
		output = process.stdout.readline()
		if output.strip() != "":
			print(output.strip())
		# Do something else
		return_code = process.poll()
		if return_code is not None:
			# Process has finished, read rest of the output
			for output in process.stdout.readlines():
				print(output.strip())
			return return_code