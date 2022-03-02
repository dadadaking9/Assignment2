import Profile as p


#brandon = p.Profile(username=input('Type username: '), password=input('Type password: '))
#print(brandon.username, brandon.password)
#brandon.save_profile("C:\\Users\\Brand\\Desktop\\SchoolWork\\ICS32\\Assignment2\\Practice Folder\\test.dsu")
emi = p.Profile()
#print(emi.username,emi.password)
emi.load_profile('C:\\Users\\Brand\\Desktop\\SchoolWork\\ICS32\\Assignment2\\Practice Folder\\test.dsu')
emi.bio = 'Hello world!'
#print(emi.username, emi.password, emi.bio)

#emi.set_entry('Hello world!')

#emi.get_entry()
#print(emi.get_posts)
print(emi)