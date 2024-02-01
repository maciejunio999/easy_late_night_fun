from PIL import Image
from square_draw import draw_square
from mine_math import find_max_increase_and_decrease_indices, transpose, find_global_extremes, round_down
from white import is_mostly_white

PHOTO_PATH = '*** your photo path **'

im = Image.open(PHOTO_PATH)

width, height = im.size

piksel = 40 # size of the square we go around the image
resized = []

resized.append(int(round_down(width / piksel)))
resized.append(int(round_down(height / piksel)))

im_croped = im.crop((0, 0, piksel * resized[0], piksel * resized[1]))
w, h = im_croped.size

IS_WHITE = is_mostly_white(PHOTO_PATH)


def main(zdj, zdj_height, zdj_width):
    pixels = zdj.load()
    r_list, g_list, b_list = [], [], []
    try:
        for y in range(0, zdj_width):  # iteracja po rzedach
            helping_r, helping_g, helping_b = [], [], []
            for x in range(0, zdj_height):  # iteracja po kolumnach
                r, g, b = pixels[x, y]
                helping_r.append(r)
                helping_g.append(g)
                helping_b.append(b)
            r_list.append(helping_r)
            g_list.append(helping_g)
            b_list.append(helping_b)
    except IndexError:
        print(str(y) + " koniec " + str(x))

    # krotki wyciągnięte z wierszy
    r_tuples, g_tuples, b_tuples = [], [], []

    for i in range(0, len(r_list)):
        r_tuples.append(find_max_increase_and_decrease_indices(r_list[i]))
        b_tuples.append(find_max_increase_and_decrease_indices(b_list[i]))
        g_tuples.append(find_max_increase_and_decrease_indices(g_list[i]))

    r_list_t, g_list_t, b_list_t = transpose(r_list), transpose(g_list), transpose(b_list)

    # krotki wyciągnięte z kolumn
    r_tuples_t, g_tuples_t, b_tuples_t = [], [], []

    for i in range(0, len(r_list_t)):
        r_tuples_t.append(find_max_increase_and_decrease_indices(r_list_t[i]))
        b_tuples_t.append(find_max_increase_and_decrease_indices(b_list_t[i]))
        g_tuples_t.append(find_max_increase_and_decrease_indices(g_list_t[i]))

    result_col_r = find_global_extremes(r_tuples, IS_WHITE)
    result_col_b = find_global_extremes(b_tuples, IS_WHITE)
    result_col_g = find_global_extremes(g_tuples, IS_WHITE)

    result_row_r = find_global_extremes(r_tuples_t, IS_WHITE)
    result_row_b = find_global_extremes(b_tuples_t, IS_WHITE)
    result_row_g = find_global_extremes(g_tuples_t, IS_WHITE)

    result_col = find_global_extremes([result_col_r, result_col_b, result_col_g], IS_WHITE)
    result_row = find_global_extremes([result_row_r, result_row_b, result_row_g], IS_WHITE)

    return sorted(result_col), sorted(result_row)


col, row = main(im_croped, w, h)

start, end = (col[0], row[0]), (col[1], row[1])

draw_square(im_croped, start, end)