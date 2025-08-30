import datetime as dab

a = "This is a calculator made by Suhas"
a += " It can do basic calculations and some advanced calculations."
a += " The current date and time is: " + str(dab.datetime.now()) + "."
a += " This calculator was made on 20th June 2024."
a += " This calculator was last updated on 26th June 2024." 
print(a)

a = 1
A = 2
b = 3
B = 4
c = 5
C = 6
d = 7
D = 8
e = 9
E = 10
f = 11
F = 12
g = 13
G = 14
h = 15
H = 16
i = 17
I = 18
j = 19
J = 20
k = 21
K = 22
l = 23
L = 24
m = 25
M = 26
n = 27
N = 28
o = 29
O = 30
p = 31
P = 32
q = 33
Q = 34
r = 35
R = 36
s = 37
S = 38
t = 39
T = 40
u = 41
U = 42
v = 43
V = 44
w = 45
W = 46
x = 47
X = 48
y = 49
Y = 50
z = 51
Z = 52
sp = 53
fu = 54  
ex = 55

code = "This is a code language. It is designed to be easy to learn and use. It is also very powerful. It is made by Suhas."

print(code)
print(H,e,l,l,o)
print(T,h,i,s,sp,i,s,sp,a,sp,c,o,d,e,sp,l,a,n,g,u,a,g,e)

print("Enter any sentence: ")
sentence = input()

for char in sentence:
    if char == " ":
        print(sp,end=",")
    elif char == ".":
        print(fu,end=",")
    elif char.islower():
        print(eval(char),end=",")
    elif char.isupper():
        print(eval(char),end=",") 

print("\n")
