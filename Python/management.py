links= []
hints= '''0- end execution;
1- create;
2- read;
3- update;
4- delete;
5- review hints.'''

opt, aux= '', ''
pos= 0
print(hints)
while opt!='0':
  opt= input('Option?')
  match opt:
    case '0': ### End execution
      print('Execution ended.')
    case '1': ### Create
      aux= input('What to insert?')
      links.append(aux)
    case '2': ### Read
      print(links)
    case '3': ### Update
      try:
        print(len(links), 'entry(ies). ', end='')
        pos= int(input('Which position?'))
        print('Entry ', pos, ' has \'', links[pos], '\'', sep='')
        aux= input('Replace with?')
        links[pos]= aux
        print('Entry ', pos, ' now has \'', links[pos], '\'', sep='')
      except ValueError:
        print('Not a number.')
      except IndexError: 
        print('Invalid position')
    case '4': ### Delete
      try:
        print(len(links), 'entry(ies). ', end='')
        pos= int(input('Which position?'))
        print('Entry ', pos, ' has \'', links[pos], '\'', sep='')
        aux= input('Confirm delete? \'Y\' for yes.')
        if aux=='Y':
          links.pop(pos)
          print('Entry ', pos, ' removed.', end='')
        else:
          print('Entry ', pos, ' not removed', end='')
        print(len(links), 'entry(ies)')
      except ValueError:
        print('Not a number.')
      except IndexError: 
        print('Invalid position')
    case '5': ### Review hints
      print(hints)
    case _:
      print('Invalid option.')