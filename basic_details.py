details = {}

details["name"] = input("What is your name? ")
details["age"] = input("How old are you? ")
details["color"] = input("What is your favourite color? ")
 
print(details)

question = input("What do you want to change? ")

if question in details:
    new_value = input("Enter the new value ")
    print("Here are the updated details? ")
    details[question] = new_value 
    print("Changes have been made")
    print(details)

else:
    print("It isn't there")



