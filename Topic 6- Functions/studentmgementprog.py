# Create a programme to allow user to create new students and to view students
# Big programme!
# Author: Grace Mary Smyth

def displaymenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View student")
    print("\t(s) Save student")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q): ").strip()
    return choice 
# test the function
'''
choice = displaymenu()
print(f"you chose: {choice}")
'''
def readmodules():
    modules = []
    modulename = input("\tEnter the first module name (blank to quit) :").strip()

    while modulename != "":
        module = {}
        module["name"] = modulename
        # error handling
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # now read the next module name
        modulename = input("\tEnter the next module name (blank to quit) :").strip()
    return modules

def displaymodules(modules):
    print ("\tName  \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))


def doadd(students):
    currentstudent = {}
    currentstudent["name"] = input("Enter name: ")
    currentstudent["modules"] = readmodules()
    students.append(currentstudent)


def doview(students):
    for currentstudent in students:
        print(currentstudent["name"])
        print("modules: ")
        displaymodules(currentstudent["modules"]);

def dosave(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"Student Name: {student['name']}\n")
            file.write("Modules:\n")
            for module in student['modules']:
                file.write(f"\t{module['name']}: {module['grade']}\n")
            file.write("\n")
    print("Student data saved successfully.")

# Main programme
students = []
choice = displaymenu()
while(choice != 'q'):
    if choice == 'a':
        doadd(students)
    elif choice == 'v':
        doview(students)
    elif choice == 's':
        dosave(students)    
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice = displaymenu()
'''
# Test
doadd(students) 
doadd(students)
print(students)
'''
'''
students = []
def readmodules():
    return []
'''
