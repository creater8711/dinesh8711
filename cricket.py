# file=open('warner.txt')
# file_read=file.read()
# print(file_read)
# file.close()

# with open('warner.txt', 'r') as file:
#     file_read = file.read(6)
#     print(file_read)
    
#     file.close()

#f=open("warner.txt", 'a')
#f.write("i am learning python advance ")
#f.close() 

#f = open('warner.txt','r')

#file = open('warner.txt' , 'r')
#file_name_read = file.read()
#print(file_name_read)

#file.close()

#file = open('warner.txt', 'w')
#file.write("hello david wrner " )

#file.close()

import json 
data = {
        'name':'dinesh',   
        'age': 19,
        'city':'bhairahawa'
}
with open('warnar.txt','w') as file:
        json.dump(data, file, indent=15)
print(data)




   

   