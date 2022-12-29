import datetime
date_format = '%Y-%m-%d'
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




