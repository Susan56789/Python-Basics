my_name = "Susan W. Macharia"
my_age = 22  # not a lie
my_height = 149  # cm
my_weight = 90  # kgs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

# the f before the double quote tell Python that the string needs to be formatted
print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall.")
print(f"She's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
