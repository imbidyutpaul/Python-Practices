# Ask user for their name
first_name = input ("What's Your First Name? ")
#remove white space from str
first_name = first_name.strip()
#capitalize user's name
first_name = first_name.capitalize()
print("Hello,",first_name)

middle_name = input ("What's Your Middle Name? ")
#input="hello world"    output="Hello World"
middle_name = middle_name.title()
print(f'Hello, "{middle_name}"')

#remove white space from str and capitalize user name
third_last_name = input ("What's Your Third Last Name? ").strip().title()
#input="world"    output="hello ??? world"
print("Hello,", third_last_name, sep=" ??? ")

second_last_name = input ("What's Your Second Last Name? ")
#remove white space from str and capitalize user name
second_last_name = second_last_name.strip().title()
print("Hello,", end=" ")
print(second_last_name)

last_name = input ("What's Your Last Name? ").strip().title()
first , last = last_name.split(" ")
print("Hello,", first)
print("Hello,", last)
