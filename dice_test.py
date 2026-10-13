import random

def cont():
    input("\033[90mPress Enter to continue...\033[0m")

def wait_to_roll():
    input("\033[90mPress Enter to roll...\033[0m")

def roll_d20():
    result = random.randint(1, 20)
    return result

str_dc = 12
dex_dc = 15
con_dc = 13

print('"Welcome traveller...!" - An old man welcomes you.')
cont()
print('"It appears you are in a little bit of a predicament... here, let me help you!" - The old man reaches out his hand.')
cont()
take_hand = input("Do you take his hand? Yes / No\n").lower().strip()
if take_hand == "yes":
    print("You grab the old man's hand... and suddenly... you feel weak! Roll for constitution!")
    wait_to_roll()
    roll_result = roll_d20()
    print(roll_result)
    if roll_result >= con_dc:
        print("\033[32mDC CHECK... SUCCESS!\033[0m")
        print("You notice something is off. His eyes are pitch black. His figure is shifting in dark smoke. He is a Wrath. "
              "He tried to consume your life force.")
    else:
        print("\033[31mDC CHECK... FAIL!\033[0m")
        print("You start to feel lightheaded and as if your soul was leaving your body. Suddenly, you pass out.")
elif take_hand == "no":
    print('"Those youngsters these days...! I see I got to teach you some manners!" - The old man attempts '
          "to swing a dagger into your ribs. Roll for dexterity!")
    wait_to_roll()
    roll_result = roll_d20()
    print(roll_result)
    if roll_result >= dex_dc:
        print("\033[32mDC CHECK... SUCCESS!\033[0m")
        print("You swiftly dodge and knock the dagger out of his hands. He is now disarmed, ha!")
    else:
        print("\033[31mDC CHECK... FAIL!\033[0m")
        print("You feel a sharp pain in the side of your torso. There's metallic taste in your mouth and you drop to the floor.")
else:
    print('"You think you are a smart fella, eh? I\'ll show ya!" - You see the old man swing the dagger that '
          'you block last moment. Make a strength save.')
    wait_to_roll()
    roll_result = roll_d20()
    print(roll_result)
    if roll_result >= str_dc:
        print("\033[32mDC CHECK... SUCCESS!\033[0m")
        print("You successfully take control of the blade and twist it. It is in your possession now. "
              "You point it at the old man.")
    else:
        print("\033[31mDC CHECK... FAIL!\033[0m")
        print("You struggle against the old man. He is surprisingly strong! Something isn't right... before you realise, "
              "the pitch black eyes are staring deep into your soul and you black out.")
