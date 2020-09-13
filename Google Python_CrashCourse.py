print("Hello World")
print(3+8)
print("3+8")
print("3"+"8");

name="Sidhant"
age=20
decimalTest=22.53
booleen=True
print("Hello "+name)
print(type(name))
print(type(age))
print(type(decimalTest))
print(type(booleen))

base= 6
height=3 
area=(base*height)/2
print("The area of the triangle is: "+ str(area))
print(base+height)

def greeting(name, department):
    print("Wlecome, "+name)
    print("YOu are part of "+department+" department")
greeting("Samant", "Science")

def convert_seconds(seconds):
    hours = seconds//3600
    minutes= (seconds-hours*3600)//60
    remaining_seconds= seconds- hours*3600 -minutes*60
    return hours,minutes,remaining_seconds
hours,minutes,seconds = convert_seconds(5000)
print(hours,minutes,seconds)

def greeting(name):
    print("Wlecome, "+ name)
result=greeting("Sidhu")
print(result)

def luckyNumber(name):
    number=len(name)*9
    print("Hello "+name+". Your lucky number is "+str(number))
luckyNumber("Sidhant")
luckyNumber("sidhu")

def circleArea(radius):
    pi=3.14
    area=pi*(radius**2)
    print(area)
circleArea(5)

print(10>5)
print("cat"=="dog")
print(1 != 2)
print(1 == "1")
print("Yellow" > "Cyan")
print("Brown" > "Magenta")
print(1<2 and 5>3)
print(25>50 or 1 != 2)
print(42 == "Ans")
print(not 42 == "Ans")

def hint_username(username):
    if len(username)<3:
        print("Invalid user name. MUst be at least 3 characters long")
    elif len(username)>15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valud username")
hint_username("Sidhant")

def is_even(number):
    if number % 2 == 0:
        return True
    return False
is_even(6)

x=0
while (x<5):
    print("Not there yet, x=" + str(x))
    x=x+1
print("x=" + str(x))

def attempts(n):
    x=1
    while(x<=n):
        print("Attemp "+str(x))
        x += 1
    print("Done")
attempts(10)

for x in range(5):
    print(x)

def sum_square(x):
    sum=0
    for n in range(x):
        sum += n*n
    return sum
print(sum_square(10))

product = 1
for n in range(1,10):
    product = product * n
print(product)

def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*(i)
    return result
print(factorial(5))

def to_clsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("temp in Faranhite:"+str(x)+" and in celsius:"+str(to_clsius(x)))

for x in range(5):
    print(str(x))
for x in range(5):
    print(str(x),end=" ")
print()
for x in range(5):
    print(str(x),end="  ")

for left in range(7):
    for right in range(left,7):
        print("["+str(left)+"|"+str(right)+"]", end=" ")
    print()


def factorial(n):
    if(n<2):
        return 1
    return n*factorial(n-1)
print(factorial(4
))

name ="Sidhant"
print(name[0])
print(name[1])
msg="Hey there"
print(msg[-1])
print(msg[-2])
print(msg[-3])

color="Orange"
print(color[1:4])
print(color[0:2])
print(color[2:len(color)])

fruit="Pineapple"
print(fruit[:4])
print(fruit[4:])

pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"),pets.index("D"))
print("Dragon" in pets)
print("Cats" in pets)

answer="YES"
 if answer.lower() == "yes":
     print("User said yes")
 answer="No"
 if answer.upper == "NO":
     print("User said NO")

msg="   Hello ppl   "
print(msg)
print(msg.strip())

msg="Hello There"
print(msg.count("e"))

mssg="Forest"
print(mssg.endswith("rest"))

num="1234"
print(num.isnumeric())

print(int("111")+int("222"))

msg1=" ".join(["This","is","joined", "by",'spaces'])
print(msg1)
msg2="...".join(["This","is","joined", "by",'dots'])
print(msg2)

splited_msg="This is a message"
print(splited_msg.split())

name="Sidhant"
number=19
print("Hello {}, your lucky number is {}".format(name,number))

name="Sidhant"
number=19
print("Hello {name}, your lucky number is {number}".format(name=name,number=number))

price=5
with_tax=5*1.18
print(price,with_tax)
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price,with_tax))

def to_clsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_clsius(x)))

x=["I","am",19,"years","old"]
print(type(x),len(x))
print(x)
print(x[2])
print(x[0:3])
y=["hello","there."]
print(y+x)

fruits=["apple","mango","orange"]
fruits.append("kiwi")
print(fruits)
fruits.insert(0,"pineapple")
print(fruits)
fruits.insert(2,"strawberry")
print(fruits)
fruits.insert(50,"peach")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop(2)
print(fruits)
fruits[2]="melon"
print(fruits) 

winners=["Raju","Sanju","Manju"]
for index,person in enumerate(winners):
    print("{} - {}".format(index+1,person))

def full_email(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_email([("sid@mali.co", "Sidhant Samant"),("raj@mail.com","RAjendra naik")]))

multiples=[]
for x in range(1,11):
    multiples.append(x*7)
print(multiples)
### or by using
multiples=[ x*7 for x in range(1,11)]
print(multiples)

languages=["Python","java","C", "Go"]
lengths=[len(language) for language in languages]
print(lengths)

z=[ x for x in range(0,101) if x%3==0]
print(z) 

x={}
print(type(x))

file_count={"jpg":10,"txt":14,"csv":2,"py":23}
print(file_count)
print(file_count["txt"])
print("jpg" in file_count)
print("html" in file_count)
file_count["png"]=10
print(file_count)
file_count["csv"]=15
print(file_count)
del file_count["csv"]
print(file_count)

file_count={"jpg":10,"txt":14,"csv":2,"py":23}
for extension in file_count:
    print(extension)

for ext,amount in file_count.items():
    print("There are {} files with .{} extension".format(amount,ext))

print(file_count.keys())
print(file_count.values())

for value in file_count.values():
    print(value)

def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letters("aaaaaaabbbbbb"))
print(count_letters("Sidhant Samant"))
print(count_letters("A1B2"))


class Fruit:
    color=""
    flavor=""

apple=Fruit()
apple.color="red"
apple.flavor="sweet"
print(apple.color)
print(apple.flavor)
print(apple.color.upper())
print()

mango=Fruit()
mango.color="yellow"
mango.flavor="super sweet"
print(mango.color)
print("one has {} color and other has {} color".format(apple.color,mango.color))

class Piglet():
    def speak(self):
        print("oink oink")
hamlet=Piglet()
hamlet.speak()

class Piglet:
    name="piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
    year=0
    def pig_years(self):
        return self.years*18
hamlet=Piglet()
hamlet.name="Hamlet"
hamlet.speak()
dukar=Piglet()
dukar.name='Dukar'
dukar.speak()
dukar.years=2
print(dukar.pig_years())

class Fruit:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
    def __str__(self):
        return "this fruit is {} and its flavor is {}".format(self.color,self.flavor)
orange=Fruit("orange","sour")
print(orange.color)
print(orange)

##help(Fruit)


class Animal:
    sound=""
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("{sound} I'm {name}! {sound}!".format(name=self.name,sound=self.sound))

class Piglet(Animal):
    sound="Oink"
hamlet=Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound="Moooo"
milky=Cow("Milky White")
milky.speak()


import random
print(random.randint(1,10))
print(random.randint(10,100))

import datetime
date_time_now=datetime.datetime.now()
print(date_time_now)
print(type(date_time_now))
print(date_time_now.year)
print(date_time_now+datetime.timedelta(days=28))



def get_event_date(event):
    return event.date

def current_user(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machine[event.machine]= set()
        if event.type="login":
            machines[event.machine].add(event.user)
        elif event.type="logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users)>0:
            user_list=", ".join(users)
            print("{}: {}".format(machine, user_list))


