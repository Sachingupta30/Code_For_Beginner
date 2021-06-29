# Armstrong Numbers..
# number of n digit which are equal to sum of nth power of its digit..
# examples : 5--> 
# (a) find no of digit(n) : n = 1
# (b) 5**1 = 5==5(original num) so it is armstrong number.
# examples : 153-->
# (a) n = 3
# (b) 1**3 + 5**3 + 3**3 == 1+125+27 == 153 == 153 (original num)
# so it is armsstrong number..

# print armstrong numbers between 0 to 1000.... 
for i in range(1001):
    num = i #this variable stored because in last we compared the num to result..
    result = 0
    n = len(str(i))
    while i!=0:
        digit = i%10
        result+=digit**n
        i = i//10
    if num == result:
        print(num)