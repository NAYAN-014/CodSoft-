contacts ={}

while True:
    print("\n Contack Book App")
    print("1.Create Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search Contact")
    print("6.Count Contact")
    print("7.Exit")

    choice = input("Enter your choice:")

    if choice =='1':
        name=input("Enter name =")
        if name in contacts:
            print(f"contact name{name} already exists!")
        else:
            age= input("Enter age=")    
            mobile= input("Enter Mobile number=") 
            email= input("Enter Email =") 
            contacts[name]={"age":int(age), "email":email,"mobile":mobile}
            print(f"*contact name {name} has been created sucessfully!*")

    elif choice=='2':
        name=input("Enter Contact name to view =")
        if name in contacts:
             contact=contacts[name]
             print(f"Name:{name},Age:{age},Mobile Number:{mobile}")
        else:
            print("*contact not found*")

    elif choice=="3":
        name=input("Enter name to Update Contact=")
        if name in contacts: 
            age= input("Enter Updated age=")    
            mobile= input("Enter Updated Mobile number=") 
            email= input("Enter Updated Email =") 
            contacts[name]={"age":int(age), "email":email,"mobile":mobile}
            print(f"*contact name {name} has been Update sucessfully!*")
        else:
            print("contact not found")  

    elif choice=="4":
        name=input("Enter Contact name to Delete=")
        if name in contacts:    
            del contacts[name]    
            print(f"*contact name {name} has been Delete sucessfully!*")
        else:
            print("*contact not found*")
    elif choice=="5":
        search_name = input("enter contact name to search=")
        found= False
        for name, contact in contacts.items():
         if search_name.lower() in name.lower():
            print(f"found-Name{name},Age:{age},mobile{mobile},Email:{email}")
            found= True
        if not found:
            print("No contact Found with that name")

    elif choice=="6":
        print(f"Total contact in your book:{len(contacts)}") 

    elif choice =="7":
        print("closing the program")   
        break

    else:
        print("invalid input ")    
