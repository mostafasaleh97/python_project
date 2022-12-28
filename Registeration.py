import myfunction as fn
def registeration():
    (fname,lname,email,password,mobile)=fn.details()
    userinfo= f"{fname}:{lname}:{email}:{password}:{mobile}\n"
    try:
        fileobject= open("userinfo.txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobject.write(userinfo)
        fileobject.close()


