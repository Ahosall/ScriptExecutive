'''
# =========
# Utils
# ====
'''

# Imports
import pyfiglet

from colors import *

from os import system as execute

# Vars

# Functions
def banner():
  execute('clear')
  
  font = pyfiglet.figlet_format('Script Executive', font='slant')
  print(colorRandom(font))
  return 'pass'