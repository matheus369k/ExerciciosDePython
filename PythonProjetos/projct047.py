from time import sleep
print('\033[0;36mANALIZANDO....')
sleep(1)
print('\033[0;33mPAR...\033[4;31m')
for c in range(2,51,2):
    print(c,end=' ')
    sleep(0.5)
print('\033[0;34mFIM...')
