#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import *
lists=["rock","paper","scissor"]
('''
WINNING CHANCES
rock vs scissor--->rock win
paper vs rock -->paper win
scissor vs paper ---> scissor win
''')
while True:
    print('''
    GAME START.....
    press 1 for play
    press 2 for exit
    ''')
    user_count=0
    com_count=0
    user_choice=input("Enter your choice:-")
    if user_choice=="1":
        name=input("Enter your name:-").lower()
        n=int(input("How many time you play:-"))
        for a in range(n):
            user_input=input('''select any one
            press 1 for rock
            press 2 for paper
            press 3 for scissor
            ''')
            if user_input=="1":
                uc="rock"
            elif user_input=="2":
                uc="paper"
            elif user_input=="3":
                uc="ssissor"
            c_choice=choice(lists)
            if uc==c_choice:
                print(f"{name} your choice is {uc}")
                print(f"computer choice is {c_choice}")
                print("Match Draw")
                user_count+=1
                com_count+=1
            elif (uc=="rock" and c_choice=="scissor") or (uc=="paper" and c_choice=="rock")or (uc=="scissor" and c_choice=="paper"):
                print(f"{name} your choice is {uc}")
                print(f"computer choice is {c_choice}")
                print(f"{name} you win")
                user_count += 2
            else:
                print(f"{name} your choice is {uc}")
                print(f"computer choice is {c_choice}")
                print(f"computer you win")
                com_count += 2
        if user_count==com_count:
            print(f"{name}you won match:{user_count}")
            print(f"computer won match:{com_count}")
            print("Finally match draw")
        elif user_count>com_count:
            print(f"{name}you won match:{user_count}")
            print(f"computer won match:{com_count}")
            print(f"Finally {name} you won")
        else:
            print(f"{name}you won match:{user_count}")
            print(f"computer won match:{com_count}")
            print("Finally computer won")
    else:
        break


# In[ ]:




