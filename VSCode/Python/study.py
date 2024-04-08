"""
print("hello")

print(10)

print(10+5)

print(10-5)

print(10/5)
print(10//5)
print(10/3)

print(10%5)

print("10+5")

lang = "hello"
print(lang)

count_1 = 10
print(count_1)

count_2 = 5
print(count_2)

print(count_1+count_2)

hello = "hello"
world = "world"
print(hello,world)
print(hello + world)

def funk():
    #処理
    return
A = "hello "
print(A * 3)

name = "YUKI"
age = 37
print("my name is " + name + "my age is " + str(age))


AAA = "100"
BBB = 1
print(int(AAA)+BBB)

baka = ["unko","gohan"]

print(baka[0])
print(baka[1])

baka.append("omutsu")
print(baka[2])
print(baka)

profile = {"name":"yuki","age":"37"}
print(profile)
print(profile["name"])
print(profile["age"])

profile["ketsueki"]="AAAAA"
print(profile["ketsueki"])

#"""

for i in range(1,101):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

print("{}と{} is even".format(i,"AAA"))


for i in ["11111","22222","33333","44444"]:
    print(i)

data=[10,20,30]
sum=0
for i in data:
    sum += i
else:
    print(sum)

for index,name in enumerate("yuki"):
    print(index,name)

print(list(range(101)))

data = {"name":"yuki","age":37,"adress":"aichi"}
for key,value in data.items():
    print("{}:{}".format(key,value))

print("入力してください")
data = input()
print("入力した文字は"+data+"です")

def hello():
    print("hello!")

hello()

def say_hallo(name):
    print("こんにちは"+ str(name) +"さん")

say_hallo("yuki")

var = 1

def sample():
    global var
    var = 2

sample()
print(var)



import os
print(os.__file__)