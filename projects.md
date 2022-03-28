{% include navigation.html %}
## Data Structures Project

GitHub page that documents Data Structures project, using code snippets for key learnings, and links to  GitHub for code and Replit for runtime.

### Python Menu

You can see the [code used](https://github.com/zachye111/zach_individual_tri3/blob/main/menu.py) in the python menu.

Creating a Python menu with data structures and try/except statements - the lazy programmer way.

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zachye111/menu"></iframe>

```
main_menu = [
    ["Swaps", "swaps.py"],
    ["Matrix", "matrix.py"],
    ["Fibonacci", "fibonacci.py"],
    ["Health", "health.py"],
    ["MNMS", "mnms.py"]
]

sub_menu = [
    ["Swaps", "swaps.py"],
    ["Matrix", "matrix.py"],
]

patterns_sub_menu = [
    ["Health", "health.py"],
]

```

- Main list of [Prompts, Actions] 
- Two styles are supported to execute abstracted logic 
- File names will be run by exec(open("filename.py").read()) 
- Function references will be executed directly file.function()

```
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Swaps and Matrix", submenu])
    menu_list.append(["Create Task", patterns_submenu])
    buildMenu(title, menu_list)

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")
 
```

- def menu
- using main_menu list:
- main menu and submenu reference are created [Prompts, Actions]
- menu_list is sent as parameter to menuy.menu function that has logic for menu control
- def submenu
- using sub menu list above:
- sub_menu works similarly to menu()
- header for menu
- build dictionary
- get user choice

```
  try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
```

- validate choice and run
- execute selection
- convert to number

```
   buildMenu(banner, options) 
```

- recursion, start menu over again

### Animation

A more efficient way of using functions to achieve the same results.

You can see the [code used](https://github.com/zachye111/zach_individual_tri3/blob/main/menu.py) in the animation.

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zachye111/random-animation"></iframe>

```
ANSI_CLEAR_SCREEN =  lambda: print('\n' * 150)
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u""
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
```
- terminal print commands

```
def Animation_print(position):
    print('\n' * 100)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + " ____")
    print(sp + "|    |")
    print(sp + "|O  O|")
    print(sp + "|  L |")
    print(sp + "| UU |")
    print(sp + "|    |")
    print(sp + "|    |")
    print(sp + "|    |")
    print(sp + "|    |")
    print(sp + " ____")
    print(RESET_COLOR)
```

- print image with colors and leading spaces

```
def animation():

    start = 0  
    distance = 75  
    step = 2  

    for position in range(start, distance, step):
        Animation_print(position) 
        time.sleep(.1)

animation()
```
- loop control variables
- start at zero
- how many times to repeat
- count by 2
- loop purpose is to animate ship sailing
- call to function with parameter

### Tree

Christmas tree with * s or a pattern.

You can see the [code used](https://github.com/zachye111/zach_individual_tri3/blob/main/menu.py) in the project.

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zachye111/tree"></iframe>

```
def tree(x):
    print("\n".join([f"{'*'*(2* n + 1):^{2*x+1}}" for n in range(x)]))
def trunk(n):
    for i in range(n):
        for j in range(n-1):
            print('      ', end=' ')
        print('***')
tree(15)
trunk(3)
print("        Here is the Tree.")
```

### Lists

InfoDB lists, InfoDB loops, and Fibonacci.

You can see the [code used](https://github.com/zachye111/zach_individual_tri3/blob/main/menu.py) in the project.

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zachye111/list"></iframe>

```
InfoDb = []
InfoDb.append({
    "FirstName": "John",
    "LastName": "Mortensen",
    "DOB": "October 21",
    "Residence": "San Diego",
    "Email": "jmortensen@powayusd.com",
    "Owns_Cars": ["2015 Fusion", "2011 Ranger", "2003 Excursion", "1997 F-350", "1969 Cadillac"]
})
InfoDb.append({
    "FirstName": "Zachary",
    "LastName": "Ye",
    "DOB": "January 19",
    "Residence": "San Diego",
    "Email": "zacharyy04338@stu.powayusd.com",
    "Owns_Cars": ["None",]
})


InfoDb.append({
    "FirstName": "Sunny",
    "LastName": "Naidu",
    "DOB": "August 2",
    "Residence": "San Diego",
    "Email": "snaidu@powayusd.com",
    "Owns_Cars": ["A", "B", "C"]
})
```

- Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars
- List with dictionary records placed in a list

```
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"]) 
    print("\t", "Cars: ", end="")  
    print(", ".join(InfoDb[n]["Owns_Cars"]))  
    print()
```

- given an index this will print InfoDb content
- using comma puts space between values
- \t is a tab indent, end="" make sure no return occurs
- join allows printing a string list with separator
- Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
- hack 2a: def for_loop()
- hack 2b: def while_loop(0)
- hack 2c : def recursive_loop(0)

```
def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  
    print("Recursive loop")
    recursive_loop(0)  

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return  
```

- requires initial index to start while
- requires initial index to start recursion
- for loop iterates on length of InfoDb
- while loop contains an initial n and an index incrementing statement (n += 1)
- recursion simulates loop incrementing on each call (n + 1) until exit condition is met
- exit condition

```
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)

def tester():
    num = int(input("Enter a number for factorial: "))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

def Fibonacci(n):
  nterms = int(input("Enter a number for Fib: ")) + 1
  # first two terms
  n1, n2 = 0, 1
  count = 0
  # check if the number of terms is valid
  if nterms <= 0:
     print("Please enter a positive integer")
  # if there is only one term, return n1
  elif nterms == 1:
     print("Fibonacci sequence upto",nterms,":")
     print(n1)
  # generate fibonacci sequence
  else:
     print("Fibonacci sequence:")
     while count < nterms:
         print(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1
def fibtester():
    Test = 1
    # check if the number is negative
    if Test < 0:
        print("Sorry, Fib does not exist for negative numbers")
    else:
        print( Fibonacci(Test))
```

- Factorial of a number using recursion
- this is test driver or code that plays when executed directly, versus import which will not run these statements
- check if the number is negative
- Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling for invalid input
- Function for nth Fibonacci number
- Check if input is 0 then it will
- print incorrect input
- Check if n is 0
- then it will return 0
- Check if n is 1,2
- it will return 1

### Factorial 

Write Factorial function using classes, providing implementation of call.

You can see the [code used](https://github.com/zachye111/zach_individual_tri3/blob/main/factorial.py) in the project.

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zachye111/list"></iframe>

```
class Factor:

    def fact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


n = int(input("Enter a number: "))
while n >= 1:
    obj = Factor()
    f = obj.fact(n)
    print("Factorial is of", n, "is", f)
    n -= 1
 ```
    

### Fibonacci

Write Factorial function using classes, providing implementation of call.

You can see the [code used](https://github.com/zachye111/zach_individual_tri3/blob/main/fibonacci.py) in the project.

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zachye111/list"></iframe>

```
class Fib:
    def fact(self, n):
        if n<= 0:
            return "Incorrect Output"
        data = [0, 1]
        if n > 2:
            for i in range (2, n):
                data.append(data[i-1] + data[i-2])
        return data[n-1]


n = int(input("Enter a number: ")) + 1
while n >= 1:
    obj = Fib()
    f = obj.fact(n)
    print("Fib of", n - 1, "is", f)
    n -= 1
    ```
    
    
