import random

in1 = "all mistakes are fixable, yet you aren’t."
in2 = "don’t be ashamed of who you are. That’s your parents’ job."
in3 = "i’ll never forget the first time we met. But I’ll keep trying."
in4 = " I thought of you today. It reminded me to take out the trash."
in5 = "when I look at you, I think to myself where have you been my whole life? Can you go back there?"
in6 = "you just might be why the middle finger was invented in the first place."
in7 = "somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology."
in8 = "the last time I saw something like you… I flushed."
in9 = "you are like a cloud. When you disappear, it’s a beautiful day."
in10 = "if laughter is the best medicine, your face must be curing the world."
in11 = "every time I think you can’t get any dumber, you prove me wrong."
in12 = "i would smack you, but I’m against animal abuse."
in13 = "Is your ass jealous of the amount of shit that comes out of your mouth?"
in14 = "I treasure the time I don’t spend with you."
in15 = "you’re the reason this country has to put directions on shampoo."


insults = [in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15]
n = random.randint(0,14)

trash = str(input("Enter who you would like to roast 😙: "))

print(trash+",", insults[n])
