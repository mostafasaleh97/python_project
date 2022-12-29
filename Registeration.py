import myfunction as fn
def registeration():
    global username
    (username,fname,lname,email,password,mobile)=fn.details()
    userinfo= f"{username}:{fname}:{lname}:{email}:{password}:{mobile}\n"
    try:
        fileobject= open("userinfo.txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobject.write(userinfo)
        fileobject.close()
    return username