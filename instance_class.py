class house():
    def __init__(self, owner):
        self.owner=owner
    def set_house(self,color):
        self.color=color
    def get_house_color(self):
        return (f'house owner: {self.owner}'+  ' ' + f'house color: {self.color}')
    
house1= house('ram')
house1.set_house('pink')
print(house1.get_house_color())
house2= house('dinesh')
house2.set_house('blue')
print(house2.get_house_color())
