import subprocess

try:
	process = subprocess.Popen(['python', '-m', 'metapensiero.pj', 'test_translation.py'], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
except Exception as e:
    print("Exception:", e)