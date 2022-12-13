print("Welcome to the Joke shop!")

user_input = input("Enter any text: ")
l=len(user_input)
print(user_input[-1:-l-1:-1])

while user_input != "":
  user_input = input("Enter any text: ")
  l=len(user_input)
  print(user_input[-1:-l-1:-1])
