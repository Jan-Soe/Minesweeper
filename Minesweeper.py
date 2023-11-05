import random as r
class Map:
    def __init__(self,size_x,size_y,bomb_percent):
        self.size_x=size_x
        self.size_y=size_y
        self.bomb_number=int(bomb_percent/100.0*size_x*size_y)
    def create_map(self):
        bomb_placer = self.bomb_number
        self.true_map = {}
        while bomb_placer > 0:
            bomb_placer-=1
            self.true_map["{x},{y}".format(x=r.randint(0,self.size_x),y=r.randint(0,self.size_y))]=True
        
        for x in range(self.size_x):
            for y in range(self.size_y):
                if "{x},{y}".format(x=x,y=y) not in self.true_map:
                    self.true_map["{x},{y}".format(x=x,y=y)]= False
        return dict(self.true_map.items())
map1 = Map(15,15,5)
print(map1.create_map())