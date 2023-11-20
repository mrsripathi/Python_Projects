import random
import pandas

MAX_LINE = 3
MIN_LINE = 1
COLA = 3
ROW = 3

symbol_count = {'A': 2, 'B': 4, 'C': 6, 'D': 8}

symbol_value = {'A': 5, 'B': 4, 'C': 2, 'D': 1}


def Check_Winings(colunms, lines, value, bet):
    winings = 0
    winings_line = []
    for line in range(lines):
        symble_to_check = colunms[0][line]
        for colunm in colunms[line]:
            if colunm != symble_to_check:
                break
        else:
          winings_line.append(line)
          winings += value[colunm] * bet

    return winings, winings_line


def Print_Slot_Machine(colunms):
    for row in range(len(colunms)):
        for i, colunm in enumerate(colunms):
            if i != len(colunms) - 1:
                print(colunm[row], end=" | ")
            else:
                print(colunm[row], end="")

        print()


def slot_mechien_spin(ROW, COLA, symbol_count):
    all_symbols = []
    colunms = []
    for key, value in symbol_count.items():
        for _ in range(value):
            all_symbols.append(key)

    for _ in range(COLA):
        colunm = []
        c_symbols = all_symbols[:]
        for _ in range(ROW):
            value = random.choice(c_symbols)
            c_symbols.remove(value)
            colunm.append(value)
        colunms.append(colunm)

    return colunms


def Get_bet():
    while True:
        amount = input("entr the bet amount: ")
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount:
                break
            else:
                print("enter the amount graeter than 0")
        else:
            print("enter the amount in number")
    return amount


def Get_line():
    while True:
        amount = input("enter the line you want to bet  ""(1-" + str(MAX_LINE) + "): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_LINE <= amount <= MAX_LINE:
                break
            else:
                print(f"enter the line is bitween {MIN_LINE}to {MAX_LINE}")
        else:
            print("pl... enter the line in number")
    return amount


def deposit():
    while True:
        amount = input("enter the deposit amount$: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(" pl... enter the valid amount$: ")
        else:
            print("Pl... enter the amount in number")
    return amount

def Spin(balanse):
    lines = Get_line()
    while True:
        bet = Get_bet()
        total_amount = (lines * bet)

        if total_amount <= balanse:
            print(f"your bet amount is {bet} on {lines} and the total amount is ${total_amount} ")
            result = slot_mechien_spin(ROW, COLA, symbol_count)
            # print(result)
            Print_Slot_Machine(result)
            winingsamount, winingsline = Check_Winings(result, lines, symbol_value, bet)
            print(f"your winings is${winingsamount}")
            print(f"your lines  is ", *winingsline)

            return winingsamount - total_amount

        else:
            break
        
        
    print(f"you not have the enough monkey in your balanse your balanse is ${balanse} and your bet is ${total_amount}")
    return 0

def main():
    balanse = deposit()
    while True:
      print(f"your current balance:  {balanse}")
      start = input("enter to play and (q to quit)")
      if start == 'q':
        break
      balanse += Spin(balanse)
                
    print(f"your left balanse is ${balanse}")


main()

