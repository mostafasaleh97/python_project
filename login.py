def login():
    global username
    while True:
        username=input("Enter your username:")
        password=input("Enter your password:")
        try:
            fileobject= open("userinfo.txt", 'r')
        except Exception as e:
            print(e)
        else:
            info=fileobject.readlines()
            fileobject.close()
        for i in info:
            data = i.split(":")
            if username == data[0] and password == data[4]:
                print("login successfully")
                break
            
        else:
            print("wrong data")
            continue
        break
    return username

    
