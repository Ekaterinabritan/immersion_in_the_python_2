
num = int(input('число = '))

DIV_HEX = 16

result = ' '

while num >= 1:
    res = num % DIV_HEX
    if res == 10:
        res = 'a'
    if res == 11:
        res = 'b'
    if res == 12:
        res = 'c'
    if res == 13:
        res = 'd'
    if res == 14:
        res = 'e'
    if res == 15:
        res = 'f'
    result += str(res)
    num = num // DIV_HEX
    result = result[::-1]

print(result,hex(num))


