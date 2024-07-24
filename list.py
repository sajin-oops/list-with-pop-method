val = ["Sajin",1,"Aaron",2,"Lijin",3]
print(val)
print(val[0])
print(val[3]) # Accessing list with index number
num = [1,2,3,4,5,6,7,8,9]
print(num[:2])
print(num[::2])
val.insert(0,"smart") #insert
print(val)
# output['smart', 'Sajin', 1, 'Aaron', 2, 'Lijin', 3]
val[0] = "politeguy" #used to modify the old value
print(val)
# output ['politeguy', 'Sajin', 1, 'Aaron', 2, 'Lijin', 3]
print(val.pop(5)) #poped value is Lijin
print(val)
# ['politeguy', 'Sajin', 1, 'Aaron', 2, 3]