# define a function that take list of words as argument and
# return list with reverse of every in that list..

def reverse_list(l):
    reversed = []
    for i in l:
        reversed.append(i[::-1])
    return reversed

x  = ['abc','def',"ghi",'jkl']
print(reverse_list(x))