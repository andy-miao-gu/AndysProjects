"""# Task 1: Collect Number of Employees
Enter the number of employees:

# Task 2 and 6: Get Employee Information and Repeat for Each Employee
For each employee:
    Enter employee name:
    Enter employee ID:

# Task 3: Calculate Total Hours Worked
For each day (Monday to Friday):
    Enter hours worked on Monday:
    Enter hours worked on Tuesday:
    Enter hours worked on Wednesday:
    Enter hours worked on Thursday:
    Enter hours worked on Friday:

# Task 4: Display Total Hours Worked
Total hours worked for {employee_name} (ID: {employee_id}): {total_hours} hours

# Task 5: Check for Bonus, Warning, or Work Hard Notice
If total hours > 40:
    This person deserves a bonus!
Else if total hours < 30:
    Warning: Employee should receive a warning for fewer hours worked.
Else if 30 <= total hours <= 35:
    Work Hard Notice: Employee should receive a work hard notice for extra effort.
else: 



alright
# Task 8: End Program
End of program."""
numemp=input("How many employees")
numemp=int(numemp)
names=list()
IDs=list()
Hours=list()
for each in range(numemp):
    name=input("Enter employee name:")
    names.append(name)
    ID=input("Enter employee ID:")
    IDs.append(ID)
result = {}
final = {}
for each in names:
    Mon=eval(input(f"Enter hours worked on Monday for {each}:"))
    Tues=eval(input(f"Enter hours worked on Tuesday for {each}:"))
    Wednes=eval(input(f"Enter hours worked on Wednesday for {each}:"))
    Thurs=eval(input(f"Enter hours worked on Thursday for {each}:"))
    Fri=eval(input(f"Enter hours worked on Friday for {each}:"))
    result[each] = [Mon,Tues,Wednes,Thurs,Fri ]
    final[each] = sum(result [each])
print(final)
