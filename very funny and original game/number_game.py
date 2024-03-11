import random
import keyboard
import time

numlist = [1,2,3,4,5,6,7,8,9,]
ansnum = random.choice(numlist)

print("Haii! Wanna play a game?")

resyn = str(input("Y/N: "))

if resyn == "Y":
    print("ALRIGHTT THEN LET'S START.")
    time.sleep(0.3)
    print("what? OH! Yes I said nothing about the game.")
    time.sleep(0.4)
    print("The game is called '𝐓𝐇𝐄 𝐍𝐔𝐌𝐁𝐄𝐑 𝐆𝐔𝐄𝐒𝐒𝐈𝐍𝐆 𝐆𝐀𝐌𝐄'.")
    time.sleep(0.4)
    print("Well all the game is you guessing the number that I will be thinking")
    time.sleep(0.4)
    print("Okay let's start")
    time.sleep(0.2)

    resnum = int(input("What is your guess??\n"))
    if resnum == ansnum:
        print("WOAAAHHH!!! IT'S TRUE. ARE YOU A GENIUS??")
        time.sleep(0.2)
        print("𝘯𝘰 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘺𝘰𝘶 𝘸𝘦𝘳𝘦 𝘫𝘶𝘴𝘵 𝘭𝘶𝘤𝘬𝘺")
        time.sleep(0.1)
        print("Anyways... Congrats!")
        time.sleep(0.5)
        print("Press 'Esc' to exit.")
        keyboard.wait('Esc')
    else:
        print("ooohhhhh noooooo!!!! it is wronk")
        time.sleep(0.2)
        print("Want a second chance? This time I will tell if your first guess is bigger or smaller than my number.")
        
        resyn1 = str(input("Y/N"))
        if resyn1 == "Y":
            print("oki:)")
            time.sleep(0.15)

            if resnum <= ansnum:
                print("Your guess is smaller than my number.")

                resnum1 = int(input("What is your second guess?\n"))
                if resnum1 == ansnum:
                    print("omg finnaly.")
                    time.sleep(0.2)
                    print("It took a while but CONGRATSSS!!!")
                    time.sleep(0.5)
                    print("Press 'Esc' to exit.")
                    keyboard.wait('Esc')
            else:
                print("Whoops! Your guess is wrong again.")
                time.sleep(0.2)
                print("It's sad:(")
                time.sleep(0.5)
                print("Okay I'm tired so I can't play another game.")
                time.sleep(0.3)
                print("Alright... I won't play because there isn't 'goto' in phyton")
                time.sleep(0.3)
                print("oki bai.")
                keyboard.press_and_release('alt + f4')

            if resnum >= ansnum:
                print("Your guess is smaller than my number.")

                resnum1 = int(input("What is your second guess?\n"))
                if resnum1 == ansnum:
                    print("omg finnaly.")
                    time.sleep(0.2)
                    print("It took a while but CONGRATSSS!!!")
                    time.sleep(0.5)
                    print("Press 'Esc' to exit.")
                    keyboard.wait('Esc')
            else:
                print("Whoops! Your guess is wrong again.")
                time.sleep(0.2)
                print("It's sad:(")
                time.sleep(0.5)
                print("Okay I'm tired so I can't play another game.")
                time.sleep(0.3)
                print("Alright... I won't play because there isn't 'goto' in phyton")
                time.sleep(0.3)
                print("oki bai.")
                keyboard.press_and_release('alt + f4')
                
        elif resyn == "N":
            print("Oki then. cya cry baby👋")
            time.sleep(0.3)
            keyboard.press_and_release('alt + f4')
        
        else:
            print("what??")
            time.sleep(0.2)
            print("ANALİZ EDİLİYOR...")
            time.sleep(1)
            print("Understandable have a good day!")
            print("Press 'Esc' to exit.")
            keyboard.wait('Esc')

elif resyn == "N":
    print("Really? Oki bai👋")
    time.sleep(0.3)
    keyboard.press_and_release('alt + f4')
else:
    print("what??")
    time.sleep(0.2)
    print("ANALİZ EDİLİYOR...")
    time.sleep(1)
    print("Understandable have a good day!")
    print("Press 'Esc' to exit.")
    keyboard.wait('Esc')
