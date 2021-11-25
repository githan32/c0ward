#experiment1

#1
'''
str = input("What is the temperature?")


temp = eval(str[0:-1])

if 'C' in str:
    F = temp*1.8 + 32
    print("The converted temperature is {}F".format(int(F)))
elif 'F' in str:
    C = (temp - 32)/1.8
    print("The converted temperature is {}C".format(int(C)))
'''
#2
'''
str1 = input("Please enter your first name:")
str2 = input("Please enter your last name:")
uersname = str1[0] + str2[:7]
print("Your username is:",uersname)
'''
#3
'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = eval(input("Enter a month number (1-12):"))
pos = (n-1)*3
str = months[pos:pos + 3]
print("The month abbreviation is {}.".format(str))
'''

#experiment2
#1
'''
x = eval(input())
n = 1
sum = x
a = x
while True:
    a = a*x*x*(-1)/((n+1)*(n+2))
    sum = sum + a
    n = n + 2
    if  abs(a) < 1e-6:
        print("{:.6f}".format(sum))
        break


'''


# experiment2

#2

'''
arr = [] 
arr = eval(input())

odd = []
even = []
for i in arr:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
if even:
    print(", ".join(repr(e) for e in even))
else :
    print("NONE")
if odd:
    print(", ".join(repr(e) for e in odd))
else:
    print("NONE")

'''
'''
s = input()
s1 = s.replace(' ','')
s2 = [eval(i) for i in s1]m
result = [0]*10
for i in s2:
    result[i] += 1       
print(" ".join(repr(i) for i in result))

'''
'''
s = input()
s1 = s.replace(',','')
s2 = [eval(i) for i in s1]
s2 = (list(set(s2)))
s2 = sorted(s2,reverse = True)
print(" ".join(str(i) for i in s2))
'''

def getNum():
    nums=[]
    iNumStr=input("Enter a number (<Enter> to quit):")
    while iNumStr!='':
        nums.append(eval(iNumStr))
        iNumStr=input("Enter a number (<Enter> to quit):")
    return nums
def mean(numbers):
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size %2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
n=getNum()
print("The mean is {:.6f}".format(mean(n)))
print("The median is {:.6f}".format(median(n)))



