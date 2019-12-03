def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    Roma_alpha = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    res = ''
    index = 0
    while num:
        res += (num // values[index]) * Roma_alpha[index]
        num %= values[index]
        index += 1
    return res

print(intToRoman(876))
# print(intToRoman(3))