import random

MAX_LINES=3
MAX_BET=1000
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "$" : 1,
    "L" : 6,
    "@" : 4,
    "W" : 2,
}

symbol_value = {
    "$" : 5,
    "W" : 4,
    "@" : 3,
    "L" : 2
}

def get_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    coloumns=[]
    for _ in range(cols):
        current_symbols=all_symbols[:]
        coloumn=[]
        for _ in  range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)
        coloumns.append(coloumn)
    return coloumns

def get_winnings(coloumns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=coloumns[0][line]
        for coloumn in coloumns:
            symbol_check=coloumn[line]
            if symbol!=symbol_check:
                break
        else:
            winning_lines.append(line)
            winnings+=values[symbol]*bet
    return winnings,winning_lines

def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i,coloumn in enumerate(coloumns):
            if i!=len(coloumns)-1:
                print(coloumn[row],end=" | ")
            else:
                print(coloumn[row],end="")
        print()

def deposit():
    while True:
        amount=input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greater than 0.")    
        else:
            print("Enter a number.")
    return amount

def get_lines():
    while True:
        lines=input("How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 0<lines<=MAX_LINES:
                break
            else:
                print("Amount should be between the given range.")
        else:
            print("Enter a number.")
    return lines

def get_bet():
    while True:
        amount=input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount should be between ${MIN_BET} - {MAX_BET}.")    
        else:
            print("Enter a number.")
    return amount

def spin(balance):
    lines=get_lines()
    bet=get_bet()
    total_bet=bet*lines
    while True:
            if total_bet>balance:
                print(f"LOW BALANCE : {balance}")
            else:
                break
    print(f"You are betting ${bet} on {lines} lines: Your bet is: ${total_bet}")
    slots=get_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=get_winnings(slots,lines,bet,symbol_value)
    print("You won $",winnings,".")
    print("You won lines : ",*winning_lines)
    return winnings-total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer=input("Press Enter to play ,q to quit.")
        if answer=='q':
            break
        balance+=spin(balance)
    print(f"You left with ${balance}.")

main()
