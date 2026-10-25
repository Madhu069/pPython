def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="Madhu",power = "flying")
print_kwargs(power = "flying")
print_kwargs(name="Madhu" )