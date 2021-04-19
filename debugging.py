def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            dividors.append(i)
    return divisors


def run():
    num = int(input('ingresa un número: '))
    print(divisors(num))
    print('Termino mi programa')


if __name__ == '__main__':
    run()