rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

position = input("Enter vacuum position (A/B): ").upper()

while True:
    print("\nCurrent position:", position)
    print("Room A:", rooms['A'])
    print("Room B:", rooms['B'])

    if rooms[position] == 'Dirty':
        print("Action: SUCK")
        rooms[position] = 'Clean'

    elif rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("Goal achieved! Both rooms are clean.")
        break

    else:
        if position == 'A':
            position = 'B'
            print("Action: MOVE RIGHT")
        else:
            position = 'A'
            print("Action: MOVE LEFT")