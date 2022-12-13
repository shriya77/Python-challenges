myarray = ['1','3','5','7','9','11','20','25','100','200']
pos = 0
found = False

user_input = input("What are you searching for? ")
while pos < len(myarray) and found == False:
    if myarray[pos] == user_input:
        found = True
        print("found at position", pos)
    else:
        pos = pos + 1

if found == False:
    print("what you're looking for isnt here!")
