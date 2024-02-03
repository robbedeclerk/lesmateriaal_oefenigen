#oefening seizoen

maand = int(input('Welke maand is het?\n'))
dag = int(input('Welke dag is het?\n'))

if maand in range(1,3): #januari februari
    print('Het is winter!')
elif maand in range(3,4) and dag in range(1,20): #maart
    print('Het is winter!')
elif maand in range(3,4) and dag in range(20,32): #maart
    print('Het is lente!')
elif maand in range(4,6): #april mei
    print('Het is lente!')
elif maand in range(6,7) and dag in range(1,21):# juni 
    print('Het is lente!')
elif maand in range(6,7) and dag in range(21,31):#juni
    print('Het is zomer!')
elif maand in range(8,9): #juli augustus
    print('Het is zomer!')
elif maand in range(9,10) and dag in range(1,22):
    print('Het is zomer!')
elif maand in range(9,10) and dag in range(22,31):
    print('Het is herfst!')
elif maand in range(10,12):
    print('Het is winter!')
elif maand in range(12,13) and dag in range(1,21):
    print('Het is herfst!')
elif maand in range(12,13) and dag in range(22,32):
    print('Het is winter!')
else:
    print('Deze data bestaan niet!')