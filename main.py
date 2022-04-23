import subprocess
import json

with open('./config.json', 'r') as g:
        path = json.load(g)

shell = path["options"]["env"]


def command(command, path):

	command[0] = f'commands/{path["current"]}/' + cmd[0] + '.py'
	fil = ['python3'] + command

	try:
		subprocess.run(fil)
	except Exception:
		print(f"command not found:{command}")


def cli():
	global path
	paths = path["paths"]
	paths["current"] = path["default"]

	exit = 0
	cliInput = ''
	
	while exit != 1:
		cliInput = input(shell)
		cliInput = cliInput.lower().split()

		if cliInput.count(2) < 2:
			cliInput.append("default")

		if cliInput[0] == 'exit':
			exit = 1
		elif cliInput[0] == 'use':
			path["current"] = paths[cliInput[1]]
		else:
			command(cliInput, paths)


cli()