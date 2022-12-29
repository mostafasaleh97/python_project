def details():
    while True:

        username=input("Enter username:")
        fname=input("Enter your fname:")
        lenght1=len(fname)
        if lenght1==0 or fname.isdigit():
            print("fname is not vaild")
            continue
        else:
            while True:
                lname = input("Enter your lname:")
                lenght2 = len(lname)

                if lenght2 == 0 or lname.isdigit():
                    print("lname is not vaild")
                    continue
                else:
                    while True:
                        email = input("Enter your eamil:")
                        for i in email:
                            if "@" in email and ".com" in email:
                                while True:
                                    password = input("Enter your password:")
                                    confirmpassword = input("confirm your password:")
                                    if confirmpassword == password:
                                        mobile = input("Enter your mobile phone:")
                                        break
                                    else:
                                        print("passwords aren't matched")
                                        continue
                            else:
                                print("NOT VAILD")
                                continue
                            break
                        break
                    break
            break
    return username, fname, lname, email, password, mobile

