import subprocess
import os

def run(payload, function):
	transpile_py_file = open("./distributedpython/transpile_temp.py", "w")
	transpile_py_file.write(function)

	transpile_py_file.close()

	try:
		os.system('python -m metapensiero.pj ./distributedpython/transpile_temp.py')
	except Exception as e:
		print("Exception:", e)

	transpile_js_file = open("./distributedpython/transpile_temp.js", "r")
	transpile_js_file_text = transpile_js_file.read()
	transpile_js_file_text = transpile_js_file_text.replace("//# sourceMappingURL=transpile_temp.js.map","")
	function = transpile_js_file_text

	transpile_js_file.close()

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
		run_process = subprocess.Popen(['node', './distributedpython/events.js', '--scheduler=https://scheduler-v3.distributed.computer/'], 
									stdout=subprocess.PIPE,
									stderr=subprocess.PIPE,
									universal_newlines=True)
	except Exception as e:
		print("Exception:", e)

	while True:
		output = run_process.stdout.readline()
		if output.strip() != "":
			print(output.strip())
		# Do something else
		return_code = run_process.poll()
		if return_code is not None:
			# Process has finished, read rest of the output
			for output in run_process.stdout.readlines():
				print(output.strip())
			return return_code