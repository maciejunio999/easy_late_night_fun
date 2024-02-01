import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def transpose(matrix):
    # Uzyskaj liczbę wierszy i kolumn
    rows, cols = len(matrix), len(matrix[0])

    # Wygeneruj transponowaną macierz przy użyciu list comprehension
    transposed = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

    return transposed

def find_global_extremes(data, is_white):
    if not data:
        return None

    if is_white:
        # Znajdź globalne minimum i maksimum z dwóch różnych miejsc w każdej krotce
        global_min = min(filter(lambda x: x[0] != 0, data), key=lambda x: x[0], default=(0, 0))[0]
        global_max = max(filter(lambda x: x[1] != 0, data), key=lambda x: x[1], default=(0, 0))[1]
    else:
        # Znajdź globalne minimum i maksimum z dwóch różnych miejsc w każdej krotce
        global_min = max(data, key=lambda x: x[0])[0]
        global_max = min(data, key=lambda x: x[1])[1]

    return (global_min, global_max)

def find_max_increase_and_decrease_indices(data):
    if len(data) < 3:
        raise ValueError("List must have at least three elements.")

    max_increase_index = None
    max_increase_value = 0
    max_decrease_index = None
    max_decrease_value = 0

    for i in range(1, len(data) - 1):
        increase = data[i] - data[i - 1]
        decrease = data[i + 1] - data[i]

        if increase > max_increase_value:
            max_increase_value = increase
            max_increase_index = i - 1  # Poprzedni indeks przed wzrostem

        if decrease < max_decrease_value:
            max_decrease_value = decrease
            max_decrease_index = i

    if max_increase_index is not None and max_decrease_index is not None:
        return tuple(sorted([max_increase_index, max_decrease_index]))
    else:
        return (0,0)