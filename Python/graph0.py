class graph:
  def __init__(self, v):
    self.vertexes= v
    self.graph= [0]
    self.graph*= v**2 #graph initialization

  def edge(self, p1, p2):
    """Adds edge between two vertexes or an autoloop in a single one"""
    if p1>= 0 and p1<self.vertexes and p2>= 0 and p2<self.vertexes:
      self.graph[p1*self.vertexes+p2]+=1
      if p1!=p2:
        self.graph[p2*self.vertexes+p1]+=1

  def unedge(self, p1, p2):
    """Removes edge between two vertexes or the autoloop of a single one"""
    if p1>= 0 and p1<self.vertexes and p2>= 0 and p2<self.vertexes:
      if self.graph[p1*self.vertexes+p2]>0:
        self.graph[p1*self.vertexes+p2]-=1
        if p1!=p2:
          self.graph[p2*self.vertexes+p1]-=1

  def print(self):
    """Prints graph as a adjacency matrix"""
    i=0
    limit= self.vertexes**2
    while i<limit:
      print(self.graph[i:i+self.vertexes])
      i+=self.vertexes
    print("")

start= graph(3)
start.print()
start.edge(0,1)
start.print()
start.edge(1,1)
start.print()
start.unedge(0,1)
start.print()
start.unedge(1,1)
start.print()
start.unedge(0,1)
start.print()
start.edge(-1,3)
start.print()

#     0 1 2
#  0 [0 1 2
#  1 [3 4 5
#  2 [6 7 8
#  row*v+column