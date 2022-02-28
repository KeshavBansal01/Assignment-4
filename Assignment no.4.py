#Question no. 1


print("Question 1")
def tower_of_hanoi(n , source, destination, auxiliary):
    step_number=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)
disk=int(input("Enter the  number of disks in the  tower of Hanoi:"))
print("\nThese  disks are numbered starting from  the top of  tower."
      "\n Some steps to move the disks from Source Tower to a Destination Tower "
      "is given below:\n")
tower_of_hanoi(disk,"Source Tower","Destination","Auxiliary")


    # Question no.2

print('\nQuestion 2\n')
n = int(input("Enter the number of rows for Pascal's Triangle: "))
print("Using recursions to create pascal's triangle: ")


def pascal(n, initial_n=n):
    if n == 0:
        return

    pascal(n-1, initial_n)
    print('  '*(initial_n-n), end='')
    a = 1
    for i in range(1, n+1):
        print(a, end='   ')
        a = a * (n - i) // i
    print()


pascal(n)


print("Using loops to create pascal's triangle:")
for line in range(1, n+1):
    print('  '*(n - line), end='')
    b = 1
    for i in range(1, line+1):
        print(b, end='   ')
        b = b * (line - i) // i
    print()


   #Question no.3
    print("Question #3")
print(" ")

print(" ")
x=int(input("Enter your first integer: "))
y=int(input("Enter yourfirst integer: "))
z=x%y
d=x//y
print("Remainder is: ", z)
print("Quotient is: ",d)
if(z!=0):
    if (d!=0):
        print("Both the  values are non zero")
    else:
        print("One of  the value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=z+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")



   #Question no. 4


print("\n[Question.4]\n")
class student:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def pfun(self):
        print(f"Hello, Myself   {self.name} and my "
              f"roll no. is {self.roll_no}")
    
    def __del__(self):
        print("Destructor Called")
keshav=student("Keshav",21105096)
keshav.pfun()
del keshav


    #Question no..5
 

print("\n[Question.5]\n")
class employees:
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
Emp_1=employees("Mehak",40000)
Emp_2=employees("Ashok",50000)
Emp_3=employees("Viren",60000)
Emp_1.pfun()
Emp_2.pfun()
Emp_3.pfun()
print("\nQue.5a")
Emp_1.salary=70000
print("Mehak salary Updated to 70000")
Emp_1.pfun()
print("\nQue.5b")
del Emp_3
print("Employee Viren's data has been removed.")


 #Question 6


print(" ")
word = input("Enter  first word: ")
testword = input("\nYou are supposed to enter a new meaningful word to test your friendship: ")

def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

if count_in_dict(word) != count_in_dict(testword):
    print("These letters aren't exact,  your friendship is fake!!")

def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("This word doesn't make sense,your friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print("")

 

