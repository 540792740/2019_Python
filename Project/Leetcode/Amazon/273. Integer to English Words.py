def numberToWords(num):
    to19 = [''] + 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    thousands = 'Billion Million Thousand'.split()
    res = []
    def findWord(n):
        nonlocal res
        if n < 20:
            res += [to19[n]]
            if res[-1] == '': res.pop()
            return

        # x * 10 + y
        if n < 100:
            res += [tens[n // 10 - 2]] + [to19[n % 10]]
            if res[-1] == '': res.pop()
            return

            # x Hundred + y * 10 + z
        if n < 1000:
            res += [to19[n // 100]] + ['Hundred']
            findWord(n % 100)
            return

        # Larger than 1000:
        if n >= 1000:
            # Billion
            cur = n // 10 ** 9
            if cur:
                findWord(cur)
                res +=  ['Billion']

            # Million
            n = n % 10 ** 9
            cur = n // 10 ** 6
            if cur:
                findWord(cur)
                res += ['Million']

            n = n % 10 ** 6
            cur = n // 1000
            if cur:
                findWord(cur)
                res += ['Thousand']

            findWord(n % 10 ** 3)
    findWord(num)
    return ' '.join(res) or 'Zero'


# print(numberToWords(24213))
print(numberToWords(20))