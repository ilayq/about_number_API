import math


class Number:
    def __init__(self, number: int):
        self.number = number
        self.json = {
            'number': number,
            'digit_sum': int,
            'digit_mult_wo_zero': int,
            'dividers': list,
            'max_divider_from_pow_of_two': int,
            'amount_of_dividers': int,
            'dividers_sum': int,
            'is_simple': bool,
            'is_half_simple': bool,
            'opposite_number': int or str,
            # 'roman_write': str,
            'binary': str,
            'ternary': str,
            'oct': str,
            'hex': str,
            'is_fib': bool,
            'fib_index': int,
            'sin': float,
            'cos': float,
            'tg': float,
            'ln': float,
            'sqrt': float,
        }

        self.digit_sum()
        self.digit_mult()
        self.dividers()
        self.dividers_sum()
        self.max_divider_from_pow_of_two()
        self.amount_of_dividers()
        self.is_simple()
        self.is_half_simple()
        self.opposite_number()
        self.binary()
        self.ternary()
        self.oct()
        self.hex()
        self.fib()
        self.sin()
        self.cos()
        self.tg()
        self.ln()
        self.sqrt()

    def to_json(self) -> dict:
        return self.json

    def digit_sum(self):
        s = 0
        for i in str(self.number):
            s += int(i)
        self.json['digit_sum'] = str(s)

    def digit_mult(self):
        if self.number == 0:
            self.json['digit_mult_wo_zero'] = str(0)
            return
        p = 1
        for i in str(self.number):
            if i == '0':
                continue
            else:
                p *= int(i)
        self.json['digit_mult_wo_zero'] = str(p)

    def dividers(self):
        self.json['dividers'] = []
        if self.number == 0:
            self.json['dividers'] = []
            return
        for i in range(1, int(self.number ** 0.5)+1):
            if self.number % i == 0:
                self.json['dividers'].append(i)
                if i != self.number ** 0.5:
                    self.json['dividers'].append(self.number // i)
        self.json['dividers'].sort()
        self.json['dividers'] = self.json['dividers']

    def max_divider_from_pow_of_two(self):
        if self.number < 1:
            self.json['max_divider_from_pow_of_two'] = '0'
            return
        i = 0
        while 2 ** i <= int(self.number ** 0.5):
            if self.number % 2 ** i == 0:
                self.json['max_divider_from_pow_of_two'] = str(2 ** i)
            i += 1

    def amount_of_dividers(self):
        self.json['amount_of_dividers'] = str(len(self.json['dividers']))

    def dividers_sum(self):
        self.json['dividers_sum'] = str(sum(self.json['dividers']))
        self.json['dividers'] = str(self.json['dividers'])

    def is_simple(self):
        if self.json['amount_of_dividers'] == 2:
            self.json['is_simple'] = str(True)
            return
        self.json['is_simple'] = str(False)

    def is_half_simple(self):
        if self.json['amount_of_dividers'] != 3:
            self.json['is_half_simple'] = str(False)
            return
        c1 = 0
        c2 = 0
        div1 = self.json['dividers'][1]
        div2 = self.json['dividers'][2]
        for i in range(1, int(div1 ** 0.5)):
            if div1 % i == 0:
                c1 += 1
                if c1 > 1:
                    self.json['is_half_simple'] = str(False)
                    return
        for i in range(1, int(div2 ** 0.5)):
            if div2 % i == 0:
                c2 += 1
                if c2 > 1:
                    self.json['is_half_simple'] = str(False)
                    return
        self.json['is_half_simple'] = str(True)

    def opposite_number(self):
        if self.number == 0:
            self.json['opposite_number'] = 'infinity'
        else:
            self.json['opposite_number'] = str(1 / self.number)

    def binary(self):
        self.json['binary'] = bin(self.number)[2:]

    def ternary(self):
        r = ''
        n = self.number
        while n > 0:
            r += str(n % 3)
            n //= 3
        if self.number == 0:
            self.json['ternary'] = '0'
            return
        self.json['ternary'] = r[::-1]

    def oct(self):
        self.json['oct'] = oct(self.number)[2:]

    def hex(self):
        self.json['hex'] = hex(self.number)[2:]

    def fib(self):
        a0 = 0
        a1 = 1
        if self.number in (0, 1):
            self.json['is_fib'] = str(True)
            self.json['fib_index'] = str(self.number)
            return
        ind = 2
        while a0 + a1 <= self.number:
            temp = a1
            a1 = a0 + a1
            a0 = temp
            if a1 == self.number:
                self.json['is_fib'] = str(True)
                self.json['fib_index'] = str(ind)
                return
            ind += 1
        self.json['is_fib'] = str(False)
        self.json['fib_index'] = '-1'

    def sin(self):
        self.json['sin'] = str(math.sin(self.number))

    def cos(self):
        self.json['cos'] = str(math.cos(self.number))

    def tg(self):
        self.json['tg'] = str(math.tan(self.number))

    def ln(self):
        if self.number > 0:
            self.json['ln'] = str(math.log(self.number, math.e))
        else:
            self.json['ln'] = str(None)

    def sqrt(self):
        if self.number >= 0:
            self.json['sqrt'] = str(math.sqrt(self.number))
        else:
            self.json['sqrt'] = 'None'
