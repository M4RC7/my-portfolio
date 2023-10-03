cmd = ''
while cmd != '0':
  cmd = input('cmd?')
  #print(cmd)
  #print(type(cmd)) #input always return str
  if cmd == '0':
    print('end')
  elif cmd == '1':
    print('cmd1')
  elif cmd == '2':
    print('cmd2')
  elif cmd == '3':
    print('cmd3')
  else:
    print('inv')
