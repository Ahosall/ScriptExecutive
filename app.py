# By Feh's

# Imports
import sys
import os
import pathlib

from time import sleep as wait

# Check if "configs" exists
if not pathlib.Path('./configs.json').exists(): os.system('python setup.py')

# Custom Imports
sys.path.append('functions')

# ------ Utils
from utils import *

# ------ Colors
from colors import *

# ------ Tools
from tools import *

# Vars

# Main function
def main():
  banner()

  # --- Menu
  items = [
    '                         --- {} {} ---                                '.format(c('By Feh\'s', 'magenta'), c('<3', 'red')),
    '                                                                      ',
    '         [{}]: Executar Script     |     [{}]: Criar novo script      '.format(c('01', 'cyan'), c('02', 'cyan')),
    '         [{}]: Editar Script       |     [{}]: Apagar script          '.format(c('03', 'cyan'), c('04', 'cyan')),
    '                                                                      ',
    '         [{}]: Configurações       |     [{}]: Verificar atualização  '.format(c('05', 'cyan'), c('06', 'cyan')),
    '                              [{}]: Sair                              '.format(c('00', 'red')),
  ]

  for item in items:
    print(item)

  option = input(c('\n    :>> ', 'green'))

  # Tools
  if option in ['01', '1']: return executeScript()
  elif option in ['02', '2']: return createScript()
  elif option in ['03', '3']: return editScript()
  elif option in ['04', '4']: return delScript()
  
  # Options
  elif option in ['05', '5']: return settings()
  elif option in ['06', '6']: return checkUpdate()

  # Errors or exit
  elif option in ['00', '0']: return 'exit'
  else: return 'error'

if __name__ == '__main__':
  while True:
    func = main()

    if func == 'exit':
      banner()
      print(c('    :>>', 'cyan'), 'Byee~')      
      sys.exit(1)
    elif func == 'error':
      print(c('    :>]', 'red'), 'Ops! parece que você informou uma opção incorreta. Voltando para o menu...')
      wait(3.5)
      pass