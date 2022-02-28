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


print("\nQuestion.3")
n1=int(input("\nEnter a Integer:"))
n2=int(input("Enter a different Integer:"))
list1=list(divmod(n1,n2))
q=list1[0]
r=list1[1]
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")


print("\nQue3.a")
c1=callable(divmod(n1,n2))
if c1==True:
    print(f" the function is callable")
if c1==False:
    print(f"The function is Not-callable")
print("\nQue3.b")
listv=[q,r]
zero=False
if zero in listv:
    zero=True
else:
    zero=False
if zero==True:
    print("All  the result values are NOT 'non-zero'")
elif zero==False:
    print("All the result values are 'non-zero'")
print("\nQue3.c")
listr=[q,r]
for i in range (4,7):
    listr.append(i)
print(f"Appended (4,5,6) in the values ({q},{r})")
listv2=[]
for i in listr:
    if i>4:
        listv2.append(i)
listv3=list(map(str,listv2))
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
print("\nQue3.d")
set1={1,2}
set1.clear()
for el in listv2:
    set1.add(el)
print(" The above result in the set form is shown below:")
print(set1)
print("\nQue3.e")
frozenset(set1)
print(" Above set have been converted to immutable.")
print("\nQue3.f")
print(f"Max value from set is {max(set1)}")
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")


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


print("\n[Question 6]")
gap=" "*10
print(f"\n{gap}WELCOME TO A FRIENDSHIP GAME")
def anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()

    list1=[]
    list2=[]
    for e in word1:
        list1.append(e)
    for el in word2:
        list2.append(el)
    
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False


player1=str(input("\nEnter the name of Player1 :"))
player2=str(input("Enter  the name of Player2 :"))
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
result=anagram(word_player1,word_player2)
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")

