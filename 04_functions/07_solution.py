def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3))

def multiply_by_two(*args):
    for i in args:
        print(i*2 ) 

multiply_by_two(1,2,3)