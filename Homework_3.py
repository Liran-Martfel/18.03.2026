import random
import time

rate = [    2,     3,     9,    7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
reset_color = '\033[0m'
light_purple = '\033[38;2;179;136;255m'
red = '\033[31m'
green = '\033[32m'
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


def gamble():
    print(f'Welcome - you have {money} money left.')
    bet = int(input("How much will you bet: "))
    def slot_machine():
        chance_win = []
        for i in range(3):
            chance = random.choice(symbols)
            chance_win.append(chance)
            print(chance, end=" | ")
            time.sleep(1)
        return chance_win,bet
    slot_machine()

    def check_win_or_lose(chance_win: list):

        winning_by_3 = (chance_win[0] == chance_win[1] == chance_win[2])
        winning_by_2 =  (chance_win[0] == chance_win[1] != chance_win[2] or
                        chance_win[0] == chance_win[2] != chance_win[1] or
                        chance_win[1] == chance_win[2] != chance_win[0])
        if len(set(chance_win)) == 2:
            return winning_by_2
        if len(set(chance_win)) == 1:
            return winning_by_3
        else:
            return None
    winning = check_win_or_lose

    def winning_money(winning_by_2,winning_by_3: list,money: int,rate: list,chance_win: list,bet: int):
        if winning_by_3:
            for i in range(len(chance_win)):
                if chance_win[i] == rate[i]:
                    new_rate = rate[i]
                    money = money + (bet * 777 * new_rate)
            print(f'Winner! now you have {money}')
        if winning_by_2:
            money = money + (bet * 11)
            print(f'Winner! now you have {money}')
        return money
    winning_money(winning,money,rate,chance_win,bet)





while True:
    print('press 1 to see the rules\npress 2 to play\npress 3 to exit\n')
    choice = int(input("please choose your option: "))
    match choice:
        case 1:
            rules()
        case 2:
            gamble()
            again = input('\nwould you like to play again?\npress (y/n)\n')
            if again == 'y':
                gamble()
            else:
                print('Thank you for playing')
                break
        case 3:
            print('Thank you for playing')
            break
