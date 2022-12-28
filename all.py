from Registeration import registeration
from login import login

def main():
    while True:

        choice=input("Enter your choice Register/login:")
        if choice=="Register":
            registeration()
            break
        elif choice=="login":
            login()
            break
        else:
            print("wrong choice")
