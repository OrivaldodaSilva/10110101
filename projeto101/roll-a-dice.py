import random
response='y'
while response=='y':
    non=random.randint(1,6)
    if non==1:
        print('[-----]')
        print('[-----]')
        print('[  0  ]')
        print('[-----]')
        print('[-----]')
    if non==2:
        print('[-----]')
        print('[ 0   ]')
        print('[     ]')
        print('[   0 ]')
        print('[-----]')
    if non==3:
        print('[-----]')
        print('[-----]')
        print('[ 000 ]')
        print('[-----]')
        print('[-----]')
    if non==4:
        print('[-----]')
        print('[ 0  0]')
        print('[     ]')
        print('[ 0  0]')
        print('[-----]')
    if non==5:
        print('[-----]')
        print('[ 0  0]')
        print('[  0  ]')
        print('[ 0  0]')
        print('[-----]')
    if non==6:
        print('[-----]')
        print('[0   0]')
        print('[0   0]')
        print('[0   0]')
        print('[-----]')
    response=input('pressione y pars recarrgar e n para vazar')
    print()