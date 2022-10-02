#Basic graph implementation in Python
class graph:
  def __init__(self, v):
    """Graph initialization"""
    self.vertexes= v
    self.graph= []
    for x in range(v):
      self.graph.append([0])
      self.graph[x]*= v
    self.print()

  def edge(self, p1, p2):
    """Adds edge between two vertexes or an autoloop in a single one"""
    if p1>= 0 and p1<self.vertexes and p2>= 0 and p2<self.vertexes:
      self.graph[p1][p2]+=1
      if p1!=p2:
        self.graph[p2][p1]+=1
    self.print()

  def unedge(self, p1, p2):
    """Removes edge between two vertexes or the autoloop of a single one"""
    if p1>= 0 and p1<self.vertexes and p2>= 0 and p2<self.vertexes:
      if self.graph[p1][p2]>0:
        self.graph[p1][p2]-=1
        if p1!=p2:
          self.graph[p2][p1]-=1
    self.print()

  def print(self):
    """Prints graph as a adjacency matrix"""
    for x in self.graph:
      print(x)
    print("")

#Testing
start= graph(3)
start.edge(0,1)
start.edge(1,1)
start.unedge(0,1)
start.unedge(1,1)
start.unedge(0,1)
start.edge(-1,3)

#Visual example: graph with 3 vertexes
#[0, 1, 2]
#[3, 4, 5]
#[6, 7, 8]