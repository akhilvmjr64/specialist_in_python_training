#kali linux
import os
print("Hai!")
while 1:
	cmd = input('Tell me what you want :')
	
	if ('not' in cmd or "n't" in cmd) or (('launch' in cmd or 'start' in cmd or 'open' in cmd or 'run' in cmd or 'execute' in cmd) and ('stop' in cmd or 'end' in cmd or 'close' in cmd or 'exit' in cmd)):
		print("""The input you gave is ambiguious give a correct input
	Following are the correct types of inputs
		- Giving a direct command name
		- Giving an input with no `not` and `n't`
		- Inputting an english sentence using keyword such as launch or start or open or run or execute if you want to start some program
		- Inputting an english sentence using keyword such as stop or end or close or exit if you want to close some program
		- Shouldn't input a setence containing commands for both starting and stopping""")
	elif ('firefox' in cmd or 'browser' in cmd):
		if cmd == 'firefox' or cmd == 'firefox':
			os.system('firefox &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd :
			os.system("kill `ps -aux | grep 'firefox' | awk '{print $2}'`")
	elif ('gedit' in cmd or 'editor' in cmd):
		if cmd == 'gedit' or cmd == 'editor':
			os.system('gedit &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('gedit &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'gedit' | awk '{print $2}'`")
		print(r"default is set to gedit can use 'mousepad' or 'vim' also")
	elif ('mousepad' in cmd):
		if cmd == 'mousepad':
			os.system('mousepad &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('mousepad &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'mousepad' | awk '{print $2}'`")
	elif ('vim' in cmd):
		if cmd == 'vim':
			os.system('vim &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('vim &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'vim' | awk '{print $2}'`")
	elif ('python' in cmd):
		if cmd == 'python':
			os.system('tput setab 8')
			print('To close Python interpreter use exit function')
			os.system('tput setab 0')
			os.system('python3')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('tput setab 8')
			print('To close Python interpreter use exit function')
			os.system('tput setab 0')
			os.system('python3')
	elif ('youtube' in cmd or 'ytube' in cmd):
		if cmd == 'youtube' or cmd == 'ytube':
			os.system('firefox youtube.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox youtube.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'firefox' | awk '{print $2}'`")
	elif ('facebook' in cmd or 'fb' in cmd):
		if cmd == 'facebook' or cmd == 'fb':
			os.system('firefox facebook.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox facebook.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'firefox' | awk '{print $2}'`")
	elif ('instagram' in cmd or 'insta' in cmd):
		if cmd == 'insta' or cmd == 'instagram':
			os.system('firefox instagram.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox instagram.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'firefox' | awk '{print $2}'`")
	elif ('linkedin' in cmd):
		if cmd == 'linkedin':
			os.system('firefox linkedin.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox linkedin.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'firefox' | awk '{print $2}'`")
	elif ('gmail' in cmd or 'mail' in cmd):
		if cmd == 'gmail' or cmd == 'mail':
			os.system('firefox gmail.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox gmail.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("kill `ps -aux | grep 'firefox' | awk '{print $2}'`")
	elif cmd == 'exit' or cmd == 'close' or cmd == 'stop' or cmd == 'end':
		print('bye!')
		break
	else:
		print("I dont't know about the input you have given hence printing out the input \n'{}'".format(cmd))
