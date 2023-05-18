list = [[],[]]
print('\033[;36m@=@'*15)
for c in range(0,7):
    num = int(input(f'\033[;33mDigite o °{c+1} valor: '))
    if num % 2 == 0:
        list[0].append(num)
    else:
        list[1].append(num)
list[0].sort()
list[1].sort()
print('\033[;36m@=@'*15)
print(f'\033[;32mOs valores pares digitados foram: {list[0]}.')
print(f'Os valores impares digitados foram: {list[1]}.')
print('\033[;36m@=@'*15)