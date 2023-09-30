room = "entrance hall"
has_key = False
has_bag = False
gold_looted = False

print()
print('''You are lost in a mysterious maze, and your goal is to find the exit. 
Along the way, you will encounter different rooms with items and puzzles.''')
print()

while room != 'exit':
    print(
        '''
            &&&&&
            &&&&&
            &&&&&
        &&&&&&&&&&&&&
          &&&&&&&&&
            &&&&&
              &
        '''
    )
    print('you are currently in ',room)
    print()

    if room == 'entrance hall':
        choice = input('there is a corridor leading to the Library.\n Do you want to go there?(Yes/No)\n').lower().strip()
        print()
        if choice == 'yes':
            room = 'library'

    elif room == 'library':
        if not has_key:
            choice  = input('there are some dusty old books and a table with a key on it. \n do you want to pick up the key?(Yes/No)\n').lower().strip()
            print()
            if choice == 'yes':
                has_key = True

        choice = input('there is also another corridor leading to the Alchemy lab \n do you want to \n go back to entrance hall\t(type:back) \n or go to Alchemy lab\t\t(type:forward)\n').lower().strip()
        print()
        if choice == 'back':
            room = "entrance hall"
        elif choice == 'forward':
            room = 'alchemy lab'
        
    elif room == 'alchemy lab':
        if not has_bag:
            choice  = input('there are some strange potions and a bag. \n do you want to pick these up?(Yes/No)\n').lower().strip()
            print()
            if choice == 'yes':
                has_bag = True
        
        choice = input('there is also another corridor leading to the treasure room \n do you want to \n go back to library\t(type:back) \n or go to treasure room\t(type:forward)\n').lower().strip()
        print()
        if choice == 'back':
            room = 'library'
        elif choice == 'forward':
            choice = input('looks like the treasure room is locked.\nDo you want to open it?(Yes/No)')
            print()
            if choice == 'yes':
                if has_key:
                    room = 'treasure room'
                else:
                    print('must be feeling stupid for not picking up the key. Now go get it!!')
                    print()
                    choice = input('you should go back to library(yes/no)\n').lower().strip()
                    print()
                    if choice == 'yes':
                        room = 'library'
            
    elif room == 'treasure room':
        print('good thing you picked up the key')
        print()
        choice = input('WOW! there is so much gold here. might as well loot as much as you can.do yo agree(yes/no)').lower().strip()
        print()
        if choice == 'no':
            print('come on man, gold is gold. I know you are not Elon Musk')
        else:
            if has_bag:
                print('good thing you picked up that bag.\n\nNOW ALL THE GOLD IS OURS HAHAHAHA!')
                gold_looted = True
                print()
            else:
                print('must be feeling stupid for not picking up the bag. Now go get it!!')
                print()
                choice = input('you should go back to alcmeny lab(yes/no)\n').lower().strip()
                print()
                if choice == 'yes':
                    room = 'alchemy lab'
            
            if gold_looted:
                print('OMG! the exit is opening.')
                print()
                room = 'exit'
        
print('you are finally free\nNow go tell the TA to give me full marks because of my humor')
print()
