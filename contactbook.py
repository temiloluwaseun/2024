contactbook={}
while True:
    options=input("to view contactbook enter 1\nto add contact enter 2\nto search for contact enter 3\nto quit enter 4\n")
    if options=="1":
        print(contactbook)
    if options=="2":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        contactbook[name] = phone_number
        print(f"Contact '{name}' added successfully.")
    if options=="3":
        search=input("Enter name to search: ")
        if search in contactbook:
            print(contactbook[search])
        else:
            print("Not Found")
    if options=="4":
        x=input("Are you sure you want to quit and refresh? ")
        if x.lower()=="yes":
            print("Quitting...")
            break