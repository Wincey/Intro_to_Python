right = input("Which assignment would you like to test? (P)i (V)alues (N)ame (C)ake (L)ists: ").upper()

if right == ("P"):
    pi = 3.14 
    r = 5
    area = pi * r * r # multiplies the value of variable "pi" by the value of variable "r" and once more by variable "r"
    print (area)
if right == ("V"):
    values = (4.50, 9.99, 2.35) #holds all three numbers in an array
    total = 0
    for i in range (0,3): #declares i with the range (0,3) which starts at the first character and ends one after the last
       total += values[i]  #takes each value of values and adds them together by cycling through the range of i
    print (total)
if right == ("C"):
    cake = 7//3 #  // means divide no remainders or nearest whole number
    remain = 7 - cake * 3
    print(remain)
if right == ("N"):
    fname = "dylan"
    lname = "fish"
    fullname = str(fname.upper() + " " + lname.upper())
    print (fullname)
if right == ("L"):
    onetoten = [1,2,3,4,5,6,7,8,9,10]
    print(onetoten[0], onetoten[4], onetoten[9])
    onetoten.append(11)
    print (onetoten)