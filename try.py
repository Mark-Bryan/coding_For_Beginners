# name = input("Enter your name: ")

# if name.isalpha():
#     print("Thank you, " + name + "!")
# else:
#     print("Please enter a valid name (letters only).")


# string = input("Enter something: ")

# if string.isdigit():
#     print("You entered only digits.")
# elif string.isalpha():
#     print("You entered only letters.")
# else:
#     print("You entered a mix of characters.")


# user = ('John', 'Doe', 'Paris', '555-1234')
# print('Name: ', type(user))


# party_goers = {'Andrew', 'Barbara', 'Carole', 'David'}
# students = {'Andrew', 'Kelly', 'Lynn', 'David'}

# commons = party_goers.intersection(students)
# party_students = list(commons)
# print('Students at the party: ', party_students)
# print('First student at the party: ', party_students[0])


# for i in range(1,11):
#     print(i)

while True:  # Infinite loop
    user_input = input("Enter something (type 'stop' to exit): ")
    if user_input.lower() == "stop":
        break  # Exits the loop if user enters "stop"
