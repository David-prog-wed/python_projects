def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
    return divisors


def run():
    num = int(input('ingresa un número: '))
    print(divisors(num))
    print('Termino mo programa')


if __name__ == '__main__':
    run()