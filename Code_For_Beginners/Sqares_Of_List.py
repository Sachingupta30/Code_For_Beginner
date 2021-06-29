# define a function which will take list contaning numbers as input
# and return list contaning square of every elements.

n = [1,2,3,4,5,6,7,8,9,10]

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
print(square_list(n))