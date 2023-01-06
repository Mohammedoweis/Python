import time


def mainPage(user_id):
    while True:
        print("""============ Crowd-Funding Main Page =========== 
            1) create raise campaign
            2) view all campaigns
            3) edit Your projects
            4) delete his own projects
            5) search for a project using date""")
        choice = MainInputValidation()
        if (choice == 1):
            createProject(user_id)
        elif (choice == 2):
            listALL()
        elif (choice == 3):
            editProject(user_id)
        elif (choice == 4):
            deleteProject(user_id)
        elif (choice == 5):
            search_by_Date()
        elif (choice == 'done'):
            break


def MainInputValidation():
    x = input("Enter Your Choice: ")
    if (x.isdigit() and int(x) in range(1, 6)):
        return int(x)
    return MainInputValidation()


def enterProjectName():
    x = input("Project Name: ")
    if (x.isalpha()):
        return x
    else:
        return enterProjectName()


def enterprojectDetails():
    x = input("project details: ")
    return x


def enterTotaltarget():
    x = input("Totaltarget: ")
    if (x.isdigit() and x != 0):
        return x
    else:
        return enterTotaltarget()


import datetime


def enterdate():
    inputDate = input("Enter the date in format 'dd/mm/yy' : ")
    day, month, year = inputDate.split('/')
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if (isValidDate):
        return inputDate
    else:
        return enterdate()


def inputProject(user_id):
    Title = enterProjectName()
    Details = enterprojectDetails()
    Totaltarget = enterTotaltarget()
    startDate = enterdate()
    endDate = enterdate()
    project_id = round(time.time())
    data = f"{user_id}:{project_id}:{Title}:{Details}:{Totaltarget}:{startDate}:{endDate}\n"
    return data


def createProject(user_id):
    data = inputProject(user_id)
    file = open("projects.txt", 'a')
    file.writelines(data)
    file.close()


def listALL():
    file = open("projects.txt", 'r')
    data = file.readlines()
    print(data)


def editProject(user_id):
    name = input("enter your project name: ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for i in data:
        d = i.split(":")
        if (d[2] == name and d[0] == user_id):
            data[index] = inputProject(user_id)

        index += 1
    file = open("projects.txt", 'w')
    file.writelines(data)
    file.close()


def deleteProject(user_id):
    name = input("enter your project name: ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for i in data:
        d = i.split(":")
        if (d[2] == name and d[0] == user_id):
            del data[index]
        index += 1
    file = open("projects.txt", 'w')
    file.writelines(data)
    file.close()
