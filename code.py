print("i love css2021(upper)".upper()) #this is all upper case

print('i love css2021 (rjust 20)'.rjust(20)) #the second letter is in upper case

print('i love css2021.(capitalize)'.capitalize())#the first letters in upper case

print("i like" + str (" cs_class_cod ") + (" alot "))#adding the whole sentence

print(f'{print}(print function)')#printing the whole function

print(f'{type(229)}(print type)')#data type

#list
list_1 = ["one","two","three"]

list_1.append("four")#adding at the end

list_1.insert(0,"zero")#adding it at the beginning

list_2=[1,2,3]

list_2.extend(list_1)#adding list_1 to list_2

print(list_1)

#dictionary
clan = {"father": "jonathan" , "mother":"christine", "sister":"rena","brother":"ronald"} 

#mapping
print(type(clan))

print(list(clan.keys()))

print(len(clan))

#update
clan.update({"father": "matovu"})

print(clan)

clan.update({"friend":"sumayah"})

print(clan)

x = clan.get("brother")

print(x)

print(len(clan))
#iterate
for m in clan.keys():
    print(clan[m])


