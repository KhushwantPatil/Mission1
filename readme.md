Hi,

We have 27 employees joining tomorrow.

I don't want Excel.

I need a small program that runs in the terminal.

It should help our HR intern enter employee information quickly.

It must be ready before 7 PM today.


Build a Python program.

When it starts, it should display:

==== HR Employee Entry ====
Then repeatedly ask the HR intern to enter:

Employee Name
Age
Department
Salary
After one employee is entered, ask:

Add another employee? (y/n)

If yes → repeat.

If no →

Print all employees in a clean format.

Finally print:


Total Employees
Average Salary
Highest Salary
Lowest Salary . 


How i Solved it 
I clearly saw a decision loop here , so first i drew a graph on paper and i need to solve it in python . so first i searched how to print . then search whhich kind of datastructure i can store data . Saw that list has better way to add elements and i can access them . then i saww we have yes and no condition to add employee or not so i google how to put condition . first i use if else but saw it doesnt loop so used while and else . i encountred problem of thing where when selected no i was getting double lists and was not getting the needed values . then i saw i was using for loop and the values calacualtion was within it . thats why values were getting printed . also initilaly i realise i will need list in lists so i can add employee details list and add that list in bigger list .

What I learned.
I learned how to break task in steps . then see what i need to do execute that step , ask google the python function to do that step , check codes how that function is used in other code and see how can i use that for my problem . execute it and see if i am getting that result or there is error , google again till i have proper solution. 