import itertools
import string

i = 0

my_list = string.digits + string.ascii_lowercase
for i in range(4):
    my_iter = itertools.combinations(my_list, i)

    #print(list(my_iter))
for q in range(i):
    my_string = ''.join(next(my_iter))
    print(my_string)



