num = eval(input("enter any random number between 0 and 9999:"))
digit_1 = num % 10 
ext1 = num // 10 
digit_2 = ext1 % 10 
ext2 = num // 100 
digit_3 = ext2 % 10
digit_4 = num // 1000

son = digit_1 + digit_2 + digit_3 + digit_4
print("num1,num2,num3, num4:",digit_1,digit_2,digit_3,digit_4)
print("sum of digits of numbers::", son)



