'''
# =========
# Tools
# ====
'''

# Imports
from os import walk, system as execute
from time import sleep as wait

# --- Colors
from colors import *
# --- Utils
from utils import *
# --- Configs
from configs import *

# Vars
codes = {
  'code': 'Visual Studio Code',
  'notepad': 'Notepad',
  'subl': 'Sublime Text Editor 3',
  'nano': 'Nano',
}

scriptFiles = getPath()
codeEditor = codes[getEditor()]

# Utils
def getScripts():
  scripts = []
  for (dirpath, dirnames, filenames) in walk(scriptFiles):
    scripts.extend(filenames)
    break
  
  return scripts

# Functions
def executeScript():
  count = 0
  scripts = getScripts()
  items = [] 

  if len(scripts) > 0:
    for script in scripts:
      count = count + 1
      if count <= 9:
        items.append('    [{}]: Script {}'.format(c('0'+str(count), 'cyan'), script))
      else:
        items.append('    [{}]: Script {}'.format(c(str(count), 'cyan'), script))
      pass
  else:
    items.append('    [{}]: Não há Scripts vá para a opção numero {} e crie um novo.'.format(c('-', 'cyan'), c('2', 'green')))

  items.append('\n    [{}]: Voltar para o menu...'.format(c('00', 'red')))

  banner()

  print('=== Scripts:')
  for item in items:
    print(item)

  print(c('\n    :>]', 'green'), 'Selecione um script')
  script = input(c('    :>> ', 'green'))

  if script.replace(' ', '') != '':
    if int(script) <= 9: script = f'0{script}'
    if f'0{script}.py' in scripts:
      print(c('\n    :>]', 'green'), 'Você deseja usar algum argumento? [Y/n]')
      arg = input(c('    :>> ', 'green'))
      args = []

      print(c('\n    :>]', 'green'), 'Args:')
      if arg == '' or arg.upper().split()[0] in ['Y', 'S']:
        while True:
          argNew = input(c('    :>> ', 'green'))
          if argNew != '':
            args.append(argNew)
          else:
            break

      banner()
      
      if arg.upper().split()[0] in ['Y', 'S']:
        print('=== python', f'0{script}.py', ''.join(args), '\n')
        execute(f'python "{scriptFiles}\\0{script}.py" ' + ''.join(args))
      else:
        print('=== python', f'0{script}.py', '\n')
        execute(f'python "{scriptFiles}\\0{script}.py"')
      print('\033[00m\n')
      input('    {} Pressione enter para voltar ao menu....'.format(c(':>>', 'green')))
      return 'restart'
    elif script in ['0', '00']:
      return 'restart'
    else:
      return 'error'
  else:
    return 'error'

def createScript():
  scripts = getScripts()
  if len(scripts) >= 9:
    nmScript = f'0{len(scripts) + 1}.py'
  else:
    nmScript = f'00{len(scripts) + 1}.py'

  banner()
  print('=== Criar novo script\n')
  
  print('    {} Arquivo criado: {}'.format(c(':>>', 'green'), nmScript))
  print('    {} Caminho: "{}"'.format(c(':>>', 'green'), getPath()))

  wait(0.025)

  print('    {} Editor de código: {}'.format(c(':>>', 'green'), codeEditor))  

  wait(0.025)

  print('\n    {} Abrindo {}...'.format(c(':>>', 'green'), codeEditor))
  execute(f'{getEditor()} "{getPath()}\\"')
  wait(0.5)
  
  with open(f'{getPath()}\\{nmScript}', 'w') as f:
    f.write(f'# Script {nmScript}\n# File created by [SCRIPT EXECUTIVE]\n\n# Imports\n\n# Vars\n\n# Functions\n')

  execute(f'{getEditor()} "{getPath()}\\{nmScript}"')
  input('    {} Pressione enter para voltar ao menu....'.format(c(':>>', 'green')))
  return 'restart'

def editScript():
  scripts = getScripts()
  items = [] 
  count = 0

  if len(scripts) > 0:
    for script in scripts:
      count = count + 1
      if count <= 9:
        items.append('    [{}]: Script {}'.format(c('0'+str(count), 'cyan'), script))
      else:
        items.append('    [{}]: Script {}'.format(c(str(count), 'cyan'), script))
      pass
  else:
    items.append('    [{}]: Não há Scripts vá para a opção numero {} e crie um novo.'.format(c('-', 'cyan'), c('2', 'green')))

  items.append('\n    [{}]: Voltar para o menu...'.format(c('00', 'red')))

  banner()
  print('=== Editar Script\n')
  for item in items:
    print(item)
  
  print(c('\n    :>]', 'green'), 'Selecione um script')

  script = input(c('    :>> ', 'green'))

  if int(script) >= 9: nmScript = f'0{len(scripts)}.py'
  else: nmScript = f'00{len(scripts)}.py'

  if script.replace(' ', '') != '':
    if nmScript in scripts:
      print(c('    :>>', 'green'), 'Abrindo', codeEditor, 'no script', c(f'{nmScript}', 'cyan'), f'em "{getPath()}".')
      wait(0.5)
      execute(f'{getEditor()} "{getPath()}\\"')
      wait(0.3)
      execute(f'{getEditor()} "{getPath()}\\{nmScript}"')
      input('    {} Pressione enter para voltar ao menu....'.format(c(':>>', 'green')))
    elif script in ['0', '00']:
      return 'restart'
    else:
      return 'error'
  else:
    return 'error'

def delScript():
  scripts = getScripts()
  items = [] 
  count = 0

  if len(scripts) > 0:
    for script in scripts:
      count = count + 1
      if count <= 9:
        items.append('    [{}]: Script {}'.format(c('0'+str(count), 'cyan'), script))
      else:
        items.append('    [{}]: Script {}'.format(c(str(count), 'cyan'), script))
      pass
  else:
    items.append('    [{}]: Não há Scripts vá para a opção numero {} e crie um novo.'.format(c('-', 'cyan'), c('2', 'green')))

  items.append('\n    [{}]: Voltar para o menu...'.format(c('00', 'red')))

  banner()
  print('=== Deletar Script\n')
  for item in items:
    print(item)
  
  print(c('\n    :>]', 'green'), 'Selecione um script')

  script = input(c('    :>> ', 'green'))

  if int(script) >= 9: nmScript = f'0{len(scripts)}.py'
  else: nmScript = f'00{len(scripts)}.py'

  if script.replace(' ', '') != '':
    if nmScript in scripts:
      print('\n    {} Script {}.py {}.'.format(c(':>>', 'green'), nmScript, c('deletado', 'red')))
      execute(f'rm "{getPath()}\\{nmScript}"')
      input('    {} Pressione enter para voltar ao menu....'.format(c(':>>', 'green')))
    elif script in ['0', '00']:
      return 'restart'
    else:
      return 'error'
  else:
    return 'error'
  