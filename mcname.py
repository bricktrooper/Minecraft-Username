import sys
import json
import platform
from os.path import expanduser

SETTINGS = "launcher_accounts.json"

HOME = expanduser("~")

if platform.system() == "Windows":
	MINECRAFT = "\\AppData\\.minecraft\\"
else:
	MINECRAFT = "/Library/Application Support/minecraft/"

FILENAME = HOME + MINECRAFT + SETTINGS
print(FILENAME)

username = input("Username: ")
if len(username) == 0:
	print("ERROR: No username provided")
else:
	# read Minecraft launcher settings from file
	file = open(FILENAME, "r+")
	settings = json.load(file)
	# set new username
	account_id = settings['activeAccountLocalId']
	account = settings['accounts'][account_id]
	account['minecraftProfile']['name'] = username
	# overwrite file with new launcher settings
	file.seek(0)
	file.truncate(0)
	json.dump(settings, file, indent=3)
	file.close()
	print("Minecraft username was set to '%s'" % (username))
