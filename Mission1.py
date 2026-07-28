print("==== HR Employee Entry ====")
print("Do you want to Add Employee Details? (Y/N)")
Emplist = []
reply = input()
while reply == "Y" or reply == "y":
    empdet = []
    print("Enter Employee Name: ")
    name = input()
    empdet.append(name)
    print("Enter Employee Age: ")
    age = input()
    empdet.append(age)
    print("Enter Employee Department: ")
    dept = input()
    empdet.append(dept)
    print("Enter Employee Salary: ")
    salary = input()
    empdet.append(salary)
    Emplist.append(empdet)
    print("Do you want to Add Employee Details? (Y/N)")
    reply = input()
else:
    for i in range(len(Emplist)):
        print(Emplist[i])
    print("Total Employees : " ,len(Emplist))
    sallist = []
    for i in range(len(Emplist)):
        sallist.append(int(Emplist[i][3]))
    print("Average Salary of Employees : ", sum(sallist)/len(sallist))
    print("Highest Salary of Employees : ", max(sallist))
    print("Lowest Salary of Employees : ", min(sallist));