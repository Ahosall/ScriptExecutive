'''
# =========
# Colors
# =====
'''
# Imports
import random

# Vars
formats = {
  'underline': '\033[04m',
  'muted': '\033[90m'
}

colors = {
  'black': '\033[1;30m',
  'red': '\033[1;31m',
  'green': '\033[1;32m',
  'yellow': '\033[1;33m',
  'blue': '\033[1;34m',
  'magenta': '\033[1;35m',
  'cyan': '\033[1;36m',
  'white': '\033[1;37m',
}

backgrounds = {
  'black': '\033[1;40m',
  'red': '\033[1;41m',
  'green': '\033[1;42m',
  'yellow': '\033[1;43m',
  'blue': '\033[1;44m',
  'magenta': '\033[1;45m',
  'cyan': '\033[1;46m',
  'white': '\033[1;47m',
}

def c(string, color, bg=False):
  
  if bg == False:    
    string = f'{colors[color]}{string}\033[00m'
  else:
    string = f'{colors[color]}{backgrounds[bg]}{string}\033[00m'

  return string

def colorRandom(string):
  newColor =[]
  for x in colors:
    newColor.append(x)

  color = random.choice(newColor)

  string = f'{colors[color]}{string}\033[00m'
  return string