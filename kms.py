# -*- coding: utf-8 -*-
"""KMS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oidJ8pkzXAmG40h5JHA8BSHzQTCo1gBa
"""

print ("3개의 정수를 입력하시오.")
n1 = int(input("n1의 정수값을 입력:  "))
n2 = int(input("n1의 정수값을 입력:  "))
n3 = int(input("n1의 정수값을 입력:  "))

total = n1 + n2 + n3 ;
average = total /3 ;
print(average)

# 21페이지, 제곱 근 구하기
import math 
print("'a, b, c' 3개의 값을 입력하시오")
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))
d = math.sqrt(b*b) - (4*a*c); 
x1 = (-b+d) / (2 * a);
x2 = (-b-d) / (2 * a);
print(x1, x2)

import math
# 근의공식 구하기
a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))
c = int(input("c의 값을 입력하세요: "))

x1 = ( (-b + (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)
x2 = ( (-b - (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)

print("x1 = " , x1)
print("x2 = " , x2)

total = 0
counter = 1
while counter <= 10:
  grade=int(input ("Enter grade: "))
  total = grade + total
  counter = counter + 1
average = total / 10
print(average)

print("3개의 값을 입력하시오")
x = int(input("Enter the x: "))
y = int(input("Enter the y: "))
z = int(input("Enter the z: "))
x = x + 1
y = y + 1
z = z + 1
print("변경된 값 : ", x, y, z)

a = 10
b = 8750
c = a * b
print(c)

pay_rate = 8750
hours_worked = int(input("일을 한 전체 시간입력하세요!: " ))
monthly_pay = hours_worked * pay_rate
print(monthly_pay)

won = 100000
usd = won * 1130
print(usd)

exchange_rate = int(input("현재 환율입력: "))
won = 100000
usd = won * exchange_rate
print(usd)

fahrenheit = 100
celsius = fahrenheit-32
celsius = celsius * 5
celsius = celsius/9
print(celsius)

x = 0
y = 0
x = int(input("정수 x를 입력하시오: "))
y = int(input("정수 y를 입력하시오: "))
sum = x + y
print(sum)

price = int(input("상품의 가격을 입력하시오: "))
vat = price * 0.1
print(vat)

age = int(input("현재 나이를 입력하시오.: "))
age = age + 10
print("10년후면", age, " 세가 되시는 군요")

print("########################")
print("# 배송료 계산 프로그램 #")
print("########################")
price= int(input("상품의 가격을 입력하세요: "))
if price > 2000:
 shipping_cost = 0
else:
 shipping_cost = 3000
print(shipping_cost)

print("########################")
print("# 합격 불합격 프로그램 #")
print("########################")
grade = int(input("성적을 입력하시오.: "))
if grade >= 60 :
 print("합격")
else :
 print("불합격")

print("근무 시간을 입력하시오")
work_hour=int(input("근무시간 입력: "))
if work_hour > 72 :
 print("초과근무 하셨습니다.")
else: 
 print("정상근무하셨습니다.")

print("########################")
print("# 짝수와 홀수 판별 앱 #")
print("########################")
x = int(input("x값 정수를 입력하시오: "))
if (x % 2) != 0 :
 print("홀수입니다.")
else:
 print("짝수입니다.")

print("정수를 입력하시오.")
x= int(input("정수값 x를 입력하시오.: "))
y= int(input("정수값 y를 입력하시오.: "))
if x > y :
 print(x)
else:
 print(y)

print("########################")
print("# 이름, 나이, 답변 앱 #")
print("########################")
yu_name = str(input("이름: "))
yu_age = int(input("나이: "))
if yu_age <= 25 :
 print("와우!!! 프로그래밍을 완벽하게 배울수 있는 나이입니다.!")
else:
 print("포기하기에는 아직 늦지 않았습니다.")
print("\n")

price = int(input("상품의 가격을 입력하시오.:"))
if price > 100000:
  shipping_cost = 0
else:
  if price > 2000:
    shipping_cost = 3000
  else:
      shipping_cost = 5000

print("배송료는", shipping_cost, "입니다.")