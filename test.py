# fibonacci series
# alist = [1,1]

# for x in range(0,10):
#     k = alist[x]+alist[x+1]
#     alist.append(k)

# print(alist)   

# factorial by recursion

# x = int(input('number de: '))
def factorial(i):
    if(i == 0):
        return 1
    else:
        return i * factorial(i-1)
num = 3
print(factorial(num))