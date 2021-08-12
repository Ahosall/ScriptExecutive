'''
# =========
# Configs
# =====
'''

# Imports
import json

# Vars
f = open('configs.json', 'r+')
config = json.load(f)
f.close()

# Utilitarys
def getEditor(): return config['settings']['code']
def changeEditor(newEditor):
  config['settings']['code'] = newEditor

  with open('configs.json', 'w+') as file: json.dump(config, file)
  
  return config

def getPath(): return config['settings']['folders']['scripts']
def changePath(newPath):
  config['settings']['folders']['scripts'] = newPath

  with open('configs.json', 'w+') as file: json.dump(config, file)

  return config

# Functions 