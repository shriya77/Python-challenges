import random
prompt = ""

def rockpapsci():
  print("rock, paper, scissors shoot!")
  player = input("pick one! (r/p/s): ")
  ai = random.randint(1,3)
  if ai == 1:
    ai_player = "r"
  if ai == 2:
    ai_player = "p"
  if ai == 3:
    ai_player = "s"

  print("computer went for: " + ai_player)
  print("you went for: " + player)

  if ai_player == player:
    print("its a draw 😔")
    prompt = input("play again? 🤠 (y/n): ")
  elif (ai_player == "r" and player == "s") or (ai_player == "p" and player == "r") or (ai_player == "s" and player == "p"):
    print("you lost 🥲")
    prompt = input("play again? 🤠 (y/n): ")
  else:
    print("you won 🎊🎉🥳")
    prompt = input("play again? 🤠 (y/n): ")
  return prompt

while prompt != "n":
 prompt = rockpapsci()

  
  
