from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

while michelangelo.health > 0 and jack_sparrow.health > 0:
    player_input = ""
    choice_input = ""
    while not choice_input == "Pirate" and not choice_input == "Ninja":
        choice_input = input("Choose a character class:\nPirate\nNinja\n")
        if choice_input == "Ninja":
            print("\nYou picked Michelangelo!\n")
            while not player_input == "1" and not player_input == "2":
                player_input = input("Choose an action:\n1) Attack\n2) Shuriken Attack\n")
                if player_input == "1":
                    michelangelo.attack(jack_sparrow)
                    jack_sparrow.attack(michelangelo)
                    michelangelo.show_stats()
                    jack_sparrow.show_stats()
                elif player_input == "2":
                    michelangelo.shuriken(jack_sparrow)
                    jack_sparrow.pistol(michelangelo)
                    michelangelo.show_stats()
                    jack_sparrow.show_stats()
                else:
                    print("\nChoose a valid action\n") 
        elif choice_input == "Pirate":
            print("You picked Jack Sparrow!")

        else:
            print("Choose a valid character class!")
        # while not player_input == "1" and not player_input == "2":
        #     player_input = input("Choose an action:\n1) Attack\n2) Shuriken Attack\n")
        #     if player_input == "1":
        #         michelangelo.attack(jack_sparrow)
        #     elif player_input == "2":
        #         michelangelo.shuriken(jack_sparrow)
        #     else:
        #         print("\nChoose a valid action\n")

print("Game Over!")


