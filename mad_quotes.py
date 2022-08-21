name = input("Enter your name: ")
print("""Hello """ + name, """Welcome and thanks for taking part in this mini-quiz
I hope you will enjoy, and maybe even learn something""""\n")


score = 0
print("Guess the name of authors of the following quotes,""\n")

madquotes = f"If it is not right do not do it, if it is not true do not say it.".upper()
print(madquotes)
author = "Marcus Aurelius"
author = True

author = input("""
a) Marcus Aurelius, 
b) Plato, 
c) Seneca, 
d) Cicero
Type the name of the author: """)

if "Marcus Aurelius" in author:
    print("You are correct!")
    score += 1
    print("Your score is", score,"/4""\n")
else:
    print("That's wrong!")
    score = 0
    print("Your score is", score,"/4""\n")

print("Next...""\n")



madquotes2 = f"Only the dead have seen the end of war.".upper()
print(madquotes2)
author1 = "Plato"
author1 = True
author1 = input("""
a) Marcus Aurelius, 
b) Plato, 
c) Seneca, 
d) Cicero
Type the name of the author: """)

if "Plato" in author1:
    print("You are correct, well done!")
    score += 1
    print("Your score is", score,"/4""\n")
else:
    print("That's not correct")
    if score == 1:
        print("Your score is 1 /4""\n")
    elif score == 0:
        print("Your score is 0 /4""\n")



print("Let's see the third quote...""\n")




madquotes3 = f"As is a tale, so is life: not how long it is, but how good it is, is what matters".upper()
print(madquotes3)
author3 = "Seneca"
author3 = True
author3 = input("""
a) Marcus Aurelius, 
b) Plato, 
c) Seneca, 
d) Cicero
Type the name of the author: """)

if "Seneca" in author3:
    print("Great, your answer is correct!")
    score += 1
    print("Your score is", score,"/4""\n")
else:
    print("Your answer is wrong")
    if score == 2:
        print("Your score is 2/4""\n")
    elif score == 1:
        print("Your score is 1/4""\n")
    elif score == 0:
        print("Your score is 0/4""\n")



print("Last one...""\n")



madquotes4 = "If you have a garden and a library, you have everything you need".upper()
print(madquotes4)
author4 = "Cicero"
author4 = True
author4 = input("""
a) Marcus Aurelius, 
b) Plato, 
c) Seneca, 
d) Cicero
Type the name of the author: """)

if "Cicero" in author4:
    print("Your answer is correct, well done!")
    score += 1
    print("Your score is", score,"/4""\n")
else:
    print("That's not correct")
    if score == 3:
        print("Your score is 3/4""\n")
    elif score == 2:
        print("Your score is 2/4""\n")
    elif score == 1:
        print("Your score is 1/4""\n")
    else:
        print("Your score is 0/4""\n")
