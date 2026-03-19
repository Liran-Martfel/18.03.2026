import random
import time

rate = [    2,     3,     9,    7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
my_money = 50
reset_color = '\033[0m'
light_purple = '\033[38;2;179;136;255m'
red = '\033[31m'
green = '\033[38;2;57;255;20m'
print(f"{light_purple}=== SLOT MACHINE ==={reset_color}")


def rules():
    print(f"{light_purple} === RULES ==={reset_color}")
    print("each symbols worth")
    for i in range(len(rate)):
        print(f"   {symbols[i]} = {rate[i]}")
    print("\nCan you make money?")
    print(
        f"🍒 🍋 ⭐ = all different → {red}You lost Your money{reset_color}\n💎 💎 🍋 = 2 of the same kind → {green}winner{reset_color} → you won (bet * 11)")
    print(
        f"⭐ ⭐ ⭐ = 3 of the same kind → {green}winner{reset_color} → you won (bet * 777 * 9)\n🔔 🍒 🔔 = 2 of the same kind → {green}winner{reset_color} → you won (bet * 7)\n")


def gamble(money):
    print(f'you have {my_money} money left.')
    bet = int(input("How much will you bet: "))
    def slot_machine(bet):
        chance_win = []
        for i in range(3):
            chance = random.choice(symbols)
            chance_win.append(chance)
            print(chance, end=" | ")
            time.sleep(1)
        return chance_win,bet
    chance_win,slot = slot_machine(bet)

    def check_win_or_lose(chance_win: list):
        if len(set(chance_win)) == 2:
            return 2
        if len(set(chance_win)) == 1:
            return 3
        else:
            return None
    winning = check_win_or_lose(chance_win)

    def winning_money(result,money: int,rate: list,chance_win: list,bet: int):
        if result == 3:
            winning_symbol = chance_win[0]
            i = symbols.index(winning_symbol)
            multiplier = rate[i]
            money = money + ((bet * 777 * multiplier) - bet)
            print(f'\n{green}Winner! now you have {money}{reset_color}')
            return money
        if result == 2:
            for symbol in chance_win:
                if chance_win.count(symbol) == 2:
                    money = money + ((bet * 11) - bet)
                    print(f'\n{green}Winner! now you have {money}{reset_color}')
                    return money
        if result is None:
            money = money - bet
            print(f'\n{red}You lost! now you have {money}{reset_color}')
        return money
    money = winning_money(winning,money,rate,chance_win,bet)
    return  money

while True:
    print('press 1 to see the rules\npress 2 to play\npress 3 to exit\n')
    choice = int(input("please choose your option: "))
    match choice:
        case 1:
            rules()
        case 2:
            my_money = gamble(my_money)
            while True:
                if my_money == 0:
                    print('\nYou have no more money!')
                    break
                again = input('\nwould you like to play again?\npress (y/n)\n')
                if again == 'y':
                    gamble(my_money)
                else:
                    print('Returning to main menu...')
                    break
        case 3:
            print('Thank you for playing')
            break