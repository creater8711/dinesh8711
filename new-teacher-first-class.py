# i=1
# while(i<5):
#     print(i)
#     if(i==3):
#         break
#     i=i+1
    
# def dinesh(*args):
#     sum = 0
    
#     for num in args:
#         sum = sum + num
    
#     return sum

# sum = dinesh (2,5,45,65,7)
# print (sum)
# sum = dinesh(2,5,87)
# print (sum)    

# def KxaK(**kwargs):
#     sum = 0
#     for key,value in kwargs.items():
        
import json
data={
    'math': 80,
    'science':40
    
}
json_data=json.dumps(data)
print(json_data)


