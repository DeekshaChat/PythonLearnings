def print_kwargs(name, power):
    print(f"Name: {name} Power: {power}")

print_kwargs(name="Superman", power= 90)
print_kwargs(power= 70, name="Batman")
#if we give named arguments then order wont matter
print('========')


def print_of_kwargs(**kwargs):
    for (key,value) in kwargs.items():
        print(f"{key}: {value}")

print_of_kwargs(name= "Superman", power= 90)
print('---------')
print_of_kwargs(power= 70, name= "Batman")
print('---------')
print_of_kwargs(name="Shaktiman", power=100, enemy="Dr. Jackal")
