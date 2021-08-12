'''
# =========
# Setup
# =====
'''

# Imports
from functions.configs import changeEditor, changePath
import os
import sys
import json
import pathlib

from time import sleep as wait

sys.path.append('functions')

# ------ Utils
from utils import *

# ------ Colors
from colors import *

# ------ Configs
from configs import *

# Vars
configDefault = {"settings": {"code": "nulo", "folders": {"scripts": "nulo"}}, "program": {"language": "PT-BR"}}

# Functions
def checkConfig():
  print('{} Verificando arquivo de configuração.'.format(c('===', 'cyan')))
  file = os.path.isfile('./configs.json')

  if not file:
    print('    {} O arquivo de configuração não existe!'.format(c(':>>', 'green')))
    print('    {} Criando...                           '.format(c(':>>', 'green')))

    with open('./configs.json', 'w') as configFile:
      json.dump(configDefault, configFile)
    print('    {} ...Ok!                               \n'.format(c(':>>', 'green')))
  else:
    print('    {} Arquivo existe.                    \n'.format(c(':>>', 'green')))  
  pass

def selectCode():
  items = [    
    '    I - Qual editor de código você irá usar? (precisa estar instalado na maquina)',
    '        [{}]: Visual Studio Code    '.format(c('01', 'cyan')),
    '        [{}]: Sublime Text 3        '.format(c('02', 'cyan')),
    '        [{}]: Nano                  '.format(c('03', 'cyan')),
    '        [{}]: Vim                   '.format(c('04', 'cyan'))
  ]

  for item in items:
    print(item)
  
  codeEditor = input('\n    {} '.format(c(':>>', 'green')))

  if codeEditor.replace(' ', '') != '':
    if codeEditor in ['01', '1']: return 'code'
    elif codeEditor in ['02', '2']: return 'text'
    elif codeEditor in ['03', '3']: return 'nano'
    elif codeEditor in ['04', '4']: return 'vim'
    else: 
      return 'error'
  else:
    return 'error'

  pass

def setPathScript():
  items = [
    '    II - Em qual pasta ficará os Scripts? (por apdrão os scripts ficam dentro da pasta "execute" na raiz do programa)',
    '    {}\n'.format(c('Insira o caminho corretamente!!!', 'white', 'red'))
  ]
  
  for item in items:
    print(item)

  path = input('    {} '.format(c(':>>', 'green')))

  if path.replace(' ', '') != '':
    if pathlib.Path(path).exists(): return path
    else: return 'error'
  else: return 'error'

# --- Function Main
def main():
  items = [
    '{} Setup [Script Executive]\n       '.format(c('===', 'cyan')),
    '    Etapas:',
    '        1. Configurar editor de código',
    '        2. Configurar pasta onde ficará os scripts',
  ]
  banner()
  checkConfig()
  
  for item in items:
    print(item)
  
  print('\n    Irá começar em 2 segundos, aguarde...\n')
  wait(2)

  code = selectCode()
  if code == 'error': return 'error'

  banner()
  items[2] = ''.join(items[2]) + ' -> (' + c(code, 'cyan') + ')'

  for item in items:
    print(item)
  
  print('\n    Ok, agora iremos configurar o caminho dos scripts. Aguarde 2 segundos...\n')
  wait(3)

  pathScripts = setPathScript()
  if pathScripts == 'error': return 'error'

  banner()
  items[3] = ''.join(items[3]) + ' -> (' + c(pathScripts, 'cyan') + ')'

  for item in items:
    print(item)

  print('''
    Certo, agora que tudo está configurado, aguarde um momento iremos salvar as configurações,
    e configurar o script para que quando você quiser só digitar "execScr" (sem as aspas duplas)
    em um terminal ou cmd (command line) o [{}] será executado.
  '''.format(c('Script Executive', 'cyan')))

  wait(10)

  print('    {} Code Editor:', codeEditor)
  changeEditor(codeEditor)

  print('    {} Scripts Folder:', pathScripts)
  changePath(pathScripts)

  

  # setScrExec_path()

  pass

if __name__ == '__main__':
  environVariable = os.environ['PATH']
  for a in environVariable.split(';'):
    # print(a.encode('UTF-8'))
    if not a.encode('UTF-8') == b'C:\\Users\\Hifuzion Dev\\WorkSpace\\Randoms\\py\\scripts\\bin': 
      os.environ['PATH'] = 'TEST;'
    
    print(environVariable)


  # while True:
  #   func = main()

  #   if func == 'exit':
  #     print(c('    :>>', 'cyan'), 'Byee~')
  #     wait(4)
  #     sys.exit(1)
  #   if func == 'error':
  #     print(c('    :>]', 'red'), 'Ops! parece que você informou uma opção incorreta. Voltando para o menu...')
  #     wait(1)
  #     pass
