exp = []
v = '\033[;35m'
print(f'{v}§=§'*15)
exp.append(str(input('\033[;33mDigite a expressão: ')))
c = p = 0
print(f'{v}§=§'*15)
for c in range(0,len(exp[0])):
    if exp[0][c] == '(':
        p += 1
    if exp[0][c] == ')':
        p -= 1
    c += 1
if p == 0:
    print('\033[;32mA expressão e VALIDA!')
else:
    print('\033[;31mA expressão e INVALIDA!')
print(f'{v}§=§'*15)


