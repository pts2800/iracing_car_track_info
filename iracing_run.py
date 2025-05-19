#!/user/bin/python3

def manageDB():
    print("test")

def getData():
    print("test")

def cleanDB():
    print("test")

#main function
def main():
    print("#################")
    print("#### WELCOME ####")
    print("#################")
    print("Choose Selection: ")
    print("1 - run all")
    print("2 - run specific year")
    print("3 - run specific season")
    print("4 - run specific week")
    print("5 - clean up database CAUTION: DELETES DATABASE ENTRIES")
    print("99 - for testing purposes (year 2024, season 3, week 5)")
    choice = int(input("Enter Choice: "))

    webdata = 'C:\\scripting\\iracing\\web_data\\'
    year = -1
    season = -1
    week = -1

    if choice == 1:
        cleanDB()
        getData(webdata, year, season, week)
    elif choice == 2:
        year = int(input("Enter Year: "))
        cleanDB()
        getData(webdata, year, season, week)
    elif choice == 3:
        cleanDB()
        year = int(input("Enter Year: "))
        season = int(input("Enter Season: "))
        getData(webdata, year, season, week)
    elif choice == 4:
        cleanDB()
        year = int(input("Enter Year: "))
        season = int(input("Enter Season: "))
        week = int(input("Enter week: "))
        getData(webdata, year, season, week)
    elif choice == 5:
        cleanDB()
    elif choice == 99:
        cleanDB()
        getData(webdata,2024,3,5)
    else:
        print("invalid choice")

main()
