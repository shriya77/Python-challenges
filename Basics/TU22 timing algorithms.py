import datetime

print("How fast can you type? Find out now!")

start_time = datetime.datetime.now()

user_input = input("Type this sentence- 'the lazy fox jumped over the brown dog': ")

while user_input != "the lazy fox jumped over the brown dog":
 print("type it correctly 🥶")
 user_input = input("Type it out again: ")

time_taken = datetime.datetime.now()-start_time  
print(f"you managed to do it in {time_taken} s")
print("That was fast 🤓")
