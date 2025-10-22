import random
import time


def is_black(number):
    if number == 0:
        return False
    if number == 10 or number == 28:
        return True
    reduced = reduce_number(number)
    return reduced % 2 == 0


def is_even(number):
    return number % 2 == 0 and number != 0


def reduce_number(number):
    if number < 10:
        return number
    
    digits = [int(digit) for digit in str(number)]
    sum_digits = sum(digits)
    return reduce_number(sum_digits)


def simulate(spins):
    init_time = time.time()

    # Cantidad de pares e impares
    even_count = 0
    odd_count = 0

    # Cantidad de tiradas por docenas
    dozen_counts = [0, 0, 0]

    # Porcentaje de ceros sobre el total de tiradas
    zero_count = 0

    # Cantidad de rojos y negros
    red_count = 0
    black_count = 0

    for i in range(spins):
        number = random.randint(0, 37)

        if number == 0:
            zero_count += 1
        
        if is_even(number):
            even_count += 1
        odd_count += 1

        if number >= 1 and number <= 12:
            dozen_counts[0] += 1
        elif number >= 13 and number <= 24:
            dozen_counts[1] += 1
        else:
            dozen_counts[2] += 1

        if is_black(number):
            black_count += 1
        else:
            red_count += 1
    
    time_elapsed = time.time() - init_time
    print_results(even_count, odd_count, dozen_counts, zero_count, red_count, black_count, time_elapsed, spins)


def print_results(even_count, odd_count, dozen_counts, zero_count, red_count, black_count, time_elapsed, spins):
    print(f'\nSimulación completada en {time_elapsed:.4f} segundos.')

    print(f'\nResultados de la simulación:')
    
    print('\nCantidad de pares e impares:')
    print(f'\t• Pares: {even_count}')
    print(f'\t• Impares: {odd_count}')

    print('\nCantidad de tiradas por docenas:')
    print(f'\t• Docena 1: {dozen_counts[0]}')
    print(f'\t• Docena 2: {dozen_counts[1]}')
    print(f'\t• Docena 3: {dozen_counts[2]}')

    print(f'\nPorcentaje de ceros:')
    print(f'\t• Ceros: {zero_count * 100 / spins:.2f}% ({zero_count} de {spins})')

    print('\nCantidad de rojos y negros:')
    print(f'\t• Rojos: {red_count}')
    print(f'\t• Negros: {black_count}')


if __name__ == "__main__":
    
    spins = 1000
    simulate(spins)
