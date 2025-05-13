#colby king module 3.2 cho-han#
import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

**Bonus Notice:** If you roll a **2 or 7**, you receive a **10 mon bonus!**
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('cdk: ')  # Changed input prompt
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('cdk: ').upper()
        if bet not in ['CHO', 'HAN']:
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = diceTotal % 2 == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Check for bonus condition:
    if diceTotal in [2, 7]:
        print(f'You rolled a total of {diceTotal}. You receive a **10 mon bonus!**')
        purse += 10  # Bonus applied

    # Display the bet results:
    if playerWon:
        print(f'You won! You take {pot} mon.')
        purse += pot  # Add the pot to the player's purse.
        house_fee = pot * 0.12  # House fee at 12%
        print(f'The house collects a {int(house_fee)} mon fee.')
        purse -= int(house_fee)  # Deduct house fee
    else:
        purse -= pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()