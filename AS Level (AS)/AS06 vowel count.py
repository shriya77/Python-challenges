def vowel_count(text):
  count = 0
  for character in text: 
   if (character in "aAeEiIoOuU"):
     count+=1

  return count

text = input("Enter your text: ")

count = vowel_count(text)

print("Number of vowels: ", count)
