from Registeration import registeration
from login import login
import datetime
import time
import os
date_format = '%Y-%m-%d'
metadata=["title","details","target","startdate","endddate"]
print("\nWelcome to python project by Mostafa Saleh\n")
time.sleep(2)
def main():
    global username
    while True:

        choice=input("Enter your choice Register/login:")
        if choice=="Register":
            username=registeration()
            print("your account added successffully")
            break
        elif choice=="login":
            username=login()
            break
        else:
            print("wrong choice")



def createproject():
    while True:
        title=input("Enter project title:")
        titlelen=len(title)
        if titlelen==0 or title.isdigit():
            print("title is not vaild")
            continue
        else:
            details=input ("Enter project details:")
            while True:
                target=input("Enter total target in bounds:")
                if target.isdigit():
                    while True:
                        try:
                        # formatting the date using strptime() function
                            startdate=input("Set start date for the campaign in that format YYYY-MM-DD:")
                            dateObject = datetime.datetime.strptime(startdate, date_format)
                            enddate=input("Set end date for the campaign in that format YYYY-MM-DD:")
                            dateObject = datetime.datetime.strptime(enddate, date_format)
                            break
                        # If the date validation goes wrong
                        except ValueError:
                    # printing the appropriate text if ValueError occurs
                            print("Incorrect data format, should be YYYY-MM-DD")
                            continue
                else:
                    print("target should be integer")
                    continue
                break

            break
    return title, details, target, startdate, enddate




def addproject():

    (title,details,target,startdate,enddate)=createproject()
    projectdata= f"{title}:{details}:{target}:{startdate}:{enddate}\n"
    try:
        fileobject= open(username + ".txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobject.write(projectdata)
        fileobject.close()
        print("added successfully")
    
    showprojects()

def readfile():
    global data
    file= open(username + ".txt", 'r')
    data=file.readlines()
    file.close()
    return data
    
def showprojects():
    global project
    readfile()
    print("Hi" + " " + username )
    if  os.stat(username + ".txt").st_size == 0:
        print("you don't have projects untill now")
        stat=input("Do you want to creat your first project y/n :")
        if stat=="y":
            addproject()
        else:
            pass
        
        time.sleep(2)
        
    else:
        
        
        print("your projetcs are :")
        time.sleep(2)
        for i in data:
            project=i.split(":")
            print(project[0])
        print("choose your select:")
        while True:
            choice=input("create project  show project  edit project  delete project  search  logout :")
            if choice=="create project":
                addproject()
                break
            elif choice == "show project":
                displayproject()
                break
            elif choice=="edit project":
                editproject()
                break
            elif choice=="delete project":
                deleteproject()
                break
            elif choice=="search":
                searchbydate()
                break
            elif choice=="logout":
                exit
            else:
                print("wrong choice")
                continue
    lastchance()



def displayproject():
    global name
    name=input("Enter the name of project: ")
    readfile()
    for i in data:
        project=i.split(":")
        if name==project[0]:
            print("title" +":"+ project[0])
            print("details" + ":" + project[1]) 
            print("target" + ":" + project[2])
            print ("startdate" + ":" + project[3])
            print("enddate" + ":" +project[4])
            break
    else:
        print("This project doesn't exist")
        displayproject()    



def editproject():
    global data
    displayproject()
    change=input("Enter the field you want to change:")
    for i in metadata:
        if change==i:
            num=metadata.index(change)
            break
        else:
            continue
    else:
        print("this field doesn't exist")
        
    update=input("Enter your update:")
    for i in data:
        project=i.split(":")
        if project[0]==name:
            num2=data.index(i)
            project[num]=update
            break
    project=':'.join(project)
    data[num2]=project
    file= open(username + ".txt", 'r+')
    for x in data:
        data=file.write(x)
    file.close() 
    print("Updated successfully")
    
def deleteproject():
    title=input("Enter the name of project you want to delete:")
    file= open(username + ".txt", 'r')
    data=file.readlines()
    file.close()
    for i in data:
        project=i.split(":")
        if project[0]==title:
            num2=data.index(i)
            break
    else:
        print("this project doesn't exist")
        deleteproject()
    data.pop(num2)
    file= open(username + ".txt", 'w')
    for x in data:
        data=file.write(x)
    print("deleted successfully")    
    file.close()  
    


def searchbydate():
    while True:
        try:
        # formatting the date using strptime() function
            searchdate=input("Set start or end  date for the campaign in that format YYYY-MM-DD:")
            dateObject = datetime.datetime.strptime(searchdate, date_format)
            break
        # If the date validation goes wrong
        except ValueError:
    # printing the appropriate text if ValueError occurs
            print("Incorrect data format, should be YYYY-MM-DD")
            continue
    readfile()
    for i in data:
        project=i.split(":")
        if searchdate==project[3] or searchdate==project[4]:
            print("title" +":"+ project[0])
            print("details" + ":" + project[1]) 
            print("target" + ":" + project[2])
            print ("startdate" + ":" + project[3])
            print("enddate" + ":" +project[4])
        else:
            print("No project match this date")
            searchbydate() 
        
def lastchance():
    chance=input("Do you want another service y/n:")
    if chance=="y":
        showprojects()
    elif chance=="n":
        print("Thank you for your visiting our project")
        exit
    else:
        print("wrong choice")
        lastchance()            
        

main()
showprojects()
