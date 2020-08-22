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
	elif ('youtube' in cmd or 'ytube' in cmd):
		if cmd == 'youtube' or cmd == 'ytube':
			os.system('microsoftedge youtube.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('microsoftedge youtube.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im msedge.exe /f/t")
	elif ('facebook' in cmd or 'fb' in cmd):
		if cmd == 'facebook' or cmd == 'fb':
			os.system('microsoftedge facebook.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('microsoftedge facebook.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im msedge.exe /f/t")
	elif ('instagram' in cmd or 'insta' in cmd):
		if cmd == 'insta' or cmd == 'instagram':
			os.system('microsoftedge instagram.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('microsoftedge instagram.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im msedge.exe /f/t")
	elif ('linkedin' in cmd):
		if cmd == 'linkedin':
			os.system('microsoftedge linkedin.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('microsoftedge linkedin.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im msedge.exe /f/t")
	elif ('gmail' in cmd or 'mail' in cmd):
		if cmd == 'gmail' or cmd == 'mail':
			os.system('microsoftedge gmail.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('microsoftedge gmail.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im msedge /f/t")
	elif ('youtube' in cmd or 'ytube' in cmd) and 'chrome' in cmd:
		if cmd == 'youtube' or cmd == 'ytube':
			os.system('chrome youtube.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('chrome youtube.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im msedge.exe /f/t")
	elif ('facebook' in cmd or 'fb' in cmd) and 'chrome' in cmd:
		if cmd == 'facebook' or cmd == 'fb':
			os.system('chrome facebook.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('chrome facebook.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im chrome.exe /f/t")
	elif ('instagram' in cmd or 'insta' in cmd) and 'chrome' in cmd:
		if cmd == 'insta' or cmd == 'instagram':
			os.system('chrome instagram.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('chrome instagram.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im chrome.exe /f/t")
	elif ('linkedin' in cmd) and 'chrome' in cmd:
		if cmd == 'linkedin':
			os.system('chrome linkedin.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('chrome linkedin.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im chrome.exe /f/t")
	elif ('gmail' in cmd or 'mail' in cmd) and 'chrome' in cmd:
		if 'chrome' in cmd:
			os.system('chrome gmail.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('chrome gmail.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im chrome.exe /f/t")
	elif ('youtube' in cmd or 'ytube' in cmd) and 'firefox' in cmd:
		if cmd == 'youtube' or cmd == 'ytube':
			os.system('firefox youtube.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox youtube.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im firefox.exe /f/t")
	elif ('facebook' in cmd or 'fb' in cmd) and 'firefox' in cmd:
		if cmd == 'facebook' or cmd == 'fb':
			os.system('firefox facebook.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox facebook.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im firefox.exe /f/t")
	elif ('instagram' in cmd or 'insta' in cmd) and 'firefox' in cmd:
		if cmd == 'insta' or cmd == 'instagram':
			os.system('firefox instagram.com')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox instagram.com')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im firefox.exe /f/t")
	elif ('linkedin' in cmd) and 'firefox' in cmd:
		if cmd == 'linkedin':
			os.system('firefox linkedin.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox linkedin.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im firefox.exe /f/t")
	elif ('gmail' in cmd or 'mail' in cmd) and 'firefox' in cmd:
		if 'firefox' in cmd:
			os.system('firefox gmail.com &')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox gmail.com &')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im firefox.exe /f/t")
	elif ('msedge' in cmd or 'edge' in cmd or 'microsoftedge' in cmd):
		if cmd == 'edge' or cmd == 'browser' or cmd == 'msedge' or cmd == 'microsoftedge':
			os.system('microsoftedge')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('microsoftedge')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd :
			os.system("taskkill /im msedge.exe /t /f")
	elif ('chrome' in cmd):
		if cmd == 'chrome':
			os.system('chrome')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('chrome')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd :
			os.system("taskkill /im chrome.exe /t /f")
	elif ('firefox' in cmd):
		if cmd == 'firefox':
			os.system('firefox')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('firefox')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd :
			os.system("taskkill /im firefox.exe /t /f")
	elif ('notepad' in cmd or 'editor' in cmd):
		if cmd == 'notepad' or cmd == 'editor':
			os.system('notepad')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('notepad')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im notepad.exe /t /f ")
		print(r"default is set to gedit can use 'sublime' or 'vscode' also")
	elif ('vscode' in cmd or 'code' in cmd or 'vs' in cmd or 'visual studio code' in cmd):
		if cmd == 'vs' or cmd == 'code' or cmd == 'vscode' or cmd == 'visual studio code':
			os.system('code')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('code')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Code.exe /f /t")
	elif ('win word' in cmd or 'word' in cmd or 'msword' in cmd):
		if cmd == 'microsoft word' or cmd == 'microsoft office word' or cmd == 'word' or cmd == 'msword' or cmd=='win word' or cmd == 'winword':
			os.system('start word')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('start word')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Winword.exe /f /t")
	elif ('win excel' in cmd or 'excel' in cmd or 'msexcel' in cmd):
		if cmd == 'microsoft excel' or cmd == 'microsoft office excel' or cmd == 'excel' or cmd == 'msexcel' or cmd=='win excel' or cmd == 'winexcel':
			os.system('start excel')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('start excel')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Excel.exe /f /t")
	elif ('win ppt' in cmd or 'power point' in cmd):
		if cmd == 'microsoft ppt' or cmd == 'microsoft office ppt' or cmd == 'ppt' or cmd == 'msppt' or cmd=='win ppt' or cmd == 'winppt' or cmd == 'microsoft power point' or cmd == 'microsoft office power point' or cmd == 'power point' or cmd == 'ms power point' or cmd=='win power point' or cmd == 'win power point':
			os.system('start powerpnt')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('start powerpnt')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Powerpnt.exe /f /t")
	elif ('calc' in cmd):
		if cmd == 'calc' or cmd=='calculator':
			os.system('calc')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('calc')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Calculator.exe /f /t")
	elif ('vlc' in cmd):
		if cmd == 'vlc' or cmd == 'vlc media player':
			os.system('vlc')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('vlc')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im vlc.exe /f /t")
	elif ('pycharm' in cmd):
		if cmd == 'pycharm':
			os.system('pycharm')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('pycharm')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Pycharm.exe /f /t")
	elif ('vbox' in cmd or 'virbox' in cmd or 'virtualbox' in cmd):
		if cmd == 'vbox' or cmd == 'virbox' or cmd == 'VirtualBox':
			os.system(r'"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system(r'"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im VirtualBox.exe /f /t")
	elif ('jupyter' in cmd or 'notebook' in cmd):
		if cmd == 'jupyter' or cmd == 'jupyter notebook' or cmd == 'notebook':
			os.system('jupyter notebook')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('jupyter notebook')
	elif ('pycharm' in cmd):
		if cmd == 'pycharm':
			os.system('pycharm')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system('pycharm')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im Pycharm.exe /f /t")
	elif ('subl' in cmd or 'sublime' in cmd):
		if cmd == 'subl' or cmd == 'sublime' or cmd=='sublime_text' or cmd == 'sublimetext':
			os.system(r'"C:\Program Files\Sublime Text 3\subl"')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			os.system(r'"C:\Program Files\Sublime Text 3\subl"')
		elif 'stop' in cmd or 'close' in cmd or 'exit' in cmd or 'end' in cmd:
			os.system("taskkill /im sublime_text.exe /f /t")
	elif ('python' in cmd):
		if cmd == 'python':
			print('To close Python interpreter use exit function')
			os.system('python3')
		elif 'launch' in cmd or 'run' in cmd or 'start' in cmd or 'open' in cmd or 'execute' in cmd:
			print('To close Python interpreter use exit function')
			os.system('python3')
	elif cmd == 'exit' or cmd == 'close' or cmd == 'stop' or cmd == 'end':
		print('bye!')
		break
	else:
		print("I dont't know about the input you have given hence printing out the input \n'{}'".format(cmd))