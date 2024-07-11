# class animal:
#     def __init__(self,name,food,work):
#         self.name=name
#         self.food=food
#         self.work=work
#         print(f'{name} food:' + self.food + " "  'dog work:'+ self.work, 'cat work:'+self.work )
        
#     def view_details(self):
#             print(self.food +self.work)
# ani1 = animal('dog',"  "'pasta'," : "'bark')
# ani2=animal('cat',"  "'milk'," " 'mwow')
# ani2.view_details()
# ani1.view_details()
class Animal:
    def __init__(self, name, food, work):
        self.name = name
        self.food = food
        self.work = work
    
    def view_details(self):
        print(f'{self.name} food: {self.food}, work: {self.work}')

ani1 = Animal('dog', 'pasta', 'bark')
ani2 = Animal('cat', 'milk', 'meow')

ani1.view_details()
ani2.view_details()
