class Wanderer:
  ### attempting to directly access these variables will raise 'AttributeError'.
  __pos_x = None
  __pos_y = None
  __beep = None
  __grid = None
  __debug = None

  ### constructor (The 'self' parameter is a reference to the current instance of the class,
  ### and is used to access variables that belongs to the class.
  ### It does not have to be named 'self' , you can call it whatever you like,
  ### but it has to be the first parameter of any function in the class)
  def __init__(self, height, width):
    self.__debug = True
    self.__pos_x, self.__pos_y, self.__beep = 0, 0, 0
    self.__grid = []
    for i in range(height): self.__grid.append([0]*width)

  def __debug(self, x):
    if self.__debug: print(x)

  def up(self):
    if self.__pos_y>0:
      self.__pos_y-=1
      print(f'Moved to {{{self.__pos_x}, {self.__pos_y}}}.')
    else:
      print('Can\'t move up!')
  def down(self):
    if self.__pos_y<len(self.__grid)-1:
      self.__pos_y+=1
      print(f'Moved to {{{self.__pos_x}, {self.__pos_y}}}.')
    else:
      print('Can\'t move down!')
  def left(self):
    if self.__pos_x>0:
      self.__pos_x-=1
      print(f'Moved to {{{self.__pos_x}, {self.__pos_y}}}.')
    else:
      print('Can\'t move left!')
  def right(self):
    if self.__pos_x<len(self.__grid[0])-1:
      self.__pos_x+=1
      print(f'Moved to {{{self.__pos_x}, {self.__pos_y}}}.')
    else:
      print('Can\'t move left!')

  def placeBeep(self, i, j):
    self.__grid[i][j] += 1
    print(f'New beep placed at {{{i}, {j}}}.')
  def pickBeep(self):
    if self.__grid[self.__pos_y][self.__pos_x]>0:
      self.__beep+=1
      self.__grid[self.__pos_y][self.__pos_x]-=1
      print(f'Beep picked. Now it has {self.__beep} beeps.')
    else:
      print('No beep to pick!')
  def dropBeep(self):
    if self.__beep>0:
      self.__beep-=1
      self.__grid[self.__pos_y][self.__pos_x]+=1
      print(f'Beep dropped. Now it has {self.__beep} beeps.')
    else:
      print('No beep to drop!')

  def showGrid(self):
    for i in self.__grid: print(i)

  ### equivalent of 'ToString()'
  def __str__(self):
    return f"""{{
  position: {{{self.__pos_x}, {self.__pos_y}}}
  beep: {self.__beep}
}}"""
# def __str__(self):
#     return """{{
#   position: {{{}, {}}}
#   beep: {}
# }}""".format(self.pos_x, self.pos_y, self.beep)

### Test
w1 = Wanderer(2,5)
w1.placeBeep(1,1)
w1.down()
w1.right()
w1.pickBeep()
w1.left()
w1.dropBeep()
w1.showGrid()
print(w1)