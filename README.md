# Python Learning
This repo is for my internship as a python developer.
## Day 1
## What is python and why we use it?
Python is a high-level programming language that is simple, easy to read, and widely used in fields like web development, data science, automation, artificial intelligence, app development, and more. Its syntax is similar to English, which makes it beginner-friendly.

We use Python because:
It’s easy to learn and understand.
It works for many types of projects.
It has lots of ready-made tools (called libraries).
It helps us build applications faster and with less code.
It is portable language for all operating system.

On Day one i have learned about what is python and why we use it and also i am able to write the python program to take input from user.

## Day 2
## Python Data Types
Python has the following built-in data types:

a. Numeric Types
    
    int → Integer numbers
    a = 10

    float → Decimal numbers
    b = 3.14

    complex → Complex numbers
    c = 2 + 3j

b. String Type
        str → String (text)
        name = "neha"
        print(name)

c. Sequence Types
        list → Ordered, changeable, allows duplicates
        fruits = ["apple", "banana", "mango"]
        print(fruits)

        tuple → Ordered, unchangeable, allows duplicates
        colors = ("red", "green", "blue")
        print(colors)

        range → It generates a sequence of numbers
        numbers = range(5) 
        (0, 1, 2, 3, 4)

d. Set Types
        set → Unordered, no duplicates
        my_set = {1, 2, 3, 4}

e. Mapping Type
        dict → Key-value pairs
        student = {"name": "neharika", "age": 21}

f. Boolean Type
    bool → True or False
        a = 10
        b = 5

        print(a > b)        # Output: True
        print(a == b)       # Output: False




## List in Python
-> A list is a collection which is ordered and mutable (changeable). 
-> It allows duplicate members.
-> list is denoted by [].


## Creating a list

    my_list = ["neha","roshni","shruti"]
    print(my_list)
    print(my_list[0])   
    print(my_list[-1])

### List Methods:

my_list.append(50)      
my_list.insert(1, 15)   
my_list.remove(20)       
my_list.pop()            
my_list.clear()          
 class_list = ["neha", "shruti", "Srijana", "neha", "Santosh"]

    print( class_list)                    #for all class_list
    print( len(class_list))               # To get the length of the class_list
    print( class_list.count("neha"))      #to count how many times repeated item are there in list.

    class_list.pop()                      #To remove the last and return from class_list
    print( class_list)

    class_list.reverse()#To reversed class_list
    print( class_list)

    new_students = ["Ram", "Shyam"]
    class_list.extend(new_students)       #here class_list extends the properties of new_students.

### list slicing
    my_list = ['m', 'a', 'n', 'g', 'o']
    print (my_list)          #output: ['m', 'a', 'n', 'g', 'o']
    print(my_list[0:3])     # Output: ['m', 'a', 'n']
    print(my_list[-2:])     # Output: ['g', 'o']
    print(my_list[:-1])     # Output: ['m', 'a', 'n', 'g']
    print(my_list[::-1])    # Output: ['o', 'g', 'n', 'a', 'm']
    print(my_list[1:4])     # Output: ['a', 'n', 'g']

## Python Variables.
    Variable is the container to store a data ,in python we can declare a variable by following way.

### integer variable declaration.
    my_var=5
    print(my_var)

### string variable
    my_var="hello"
    print(my_var)

### list variables
    my_var=["neha","roshni","santosh" ,"sruti"]
    print(my_var)

### Assigning variable
    my_var=["neha","roshni","santosh" ,"sruti"]
    a,b,c,d=my_var
    print(a)
    print(b)
    print(c)
    print(d)

### Same value for multiple variables
    x=y=z="neha"
    print(x)
    print(y)
    print(z)

### variable addition and concatenate
    x="python"
    y="Is"
    z="Awesome"
    print(x,y,z)
    print(x+y+z)

    x="python "
    y="Is "
    z="Awesome "
    print(x+y+z)

### Global variables  
    #This is a global variable
        greet = "Hello"

        def my_name():
        print(greet)  

        my_name()
        print(greet)  #####Using the global variable outside the function

        def my_name():
        greet = "Hello"  #####This is a local variable
        print(greet)

        my_name()
        print(greeting) #####This won't work because local variable can not run outside the function.

## python Arithmetic and comparison operators

### Arithmetic operators
        a = 10
        b = 3

        print(a + b)         
        print(a - b)       
        print(a * b)   
        print(a / b)        
        print(a // b)  
        print(a % b)          
        print(a ** b) 


### Comparison operators 
        x = 5
        y = 8
        Equal to      (x == y)                # False
        Not equal to  (x != y)                # True
        Greater than  (x > y)                 # False
        Less than     (x < y)                 # True
        Greater than or equal (x >= y)         # False
        Less than or equal     (x <= y)        # True

 ## Day 3
 ###   String and String Methods
    Strings are sequence of character which is denoted by single double or triple quotation.Strings are immutable.
        
 ### String Methods
    ####Indexing
    my-name = "neha" 
    print(my_name[0])    (1st letter)
    print(my_name[1])    (2nd letter)
    print(my_name[-1])   (last letter)
     

  #### .lower()
    changes to a lower letter
 #### .Upper()
    It changes all the word into small letter.  
#### .Strip()
    It removes the unnecessary white space from the word(i.e not from the each words after the ending of word.)
####  .replace() 
    Changes one word or letter to another (We can change or replace after defining also).
 #### .Count()
    It counts how many times words are repeated.
 #### .Capitalize()
     It help to capitalize initial word only.
#### .Splits() 
    It turns all the strings into list .

 ####  Slicing
    Slicing is the process of getting desirable position only. for an example:            

    print(my_name[0:2])   (from index 0 to 1)
    print(my_name[1:])    (from index 1 to end)
    print(my_name[:3])    (from start to index 2)
    print(my_name[:])     (whole string)
    print(my_name[::-1])  (reversed string)
    print(my_name[::2])   (every 2nd character: index 0, 2)


#### fstring
    fstring in python is formatted way of string. It simply give clear and better understanding way in output, For an example:
    
    name = "Neha"
    age = 24
    print(f"My name is {name} and I am {age} years old.")
    {Output: My name is Neha and I am 24 years old.}
    We can also add and other mathematical operations also.
