from decimal import Decimal

x = 0.1 + 0.1 + 0.1
# print(x)

y = 0.1 + 0.1 + 0.1 - 0.3
# print(y)


# To solve this problem use decimal library
p = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# print(p)

q = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') -Decimal('0.3')
# print(q)



setone = {1,2,3,4}
setone = setone & {1,0, 9}  #intersection
# print(setone)

settwo = {1,2,3,4}
settwo = settwo | {1,0, 9} #union
# print(settwo)

setthree = {1,2,3,4}
setthree = setthree - {1,2,3,4} #subtraction
# print(setthree)

#important--------
# print(type(setthree))
# print(type({}))


user = "Deeksha"
print(user)
print(repr(user))
print(str(user))