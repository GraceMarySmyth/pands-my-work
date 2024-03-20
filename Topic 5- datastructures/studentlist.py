# Programme that stores a students name and a list of her courses and grades in a dictionary
# Programme should then print out her data
# Number of courses she has could change

student = {
    "name" : "Mary",
    "modules":[
        {
            "coursename":"programming",
            "grade": 45
        },
        {"coursename":"History",
         "grade": 99
         }
    ]
} 
print (student, {}.format(student["name"]))
for module in student["modules"]:
       print("\t: {} \t{}".format(module["coursename"], module["grade"]))