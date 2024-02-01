from PIL import Image
from square_draw import draw_square
from mine_math import find_max_increase_and_decrease_indices, transpose, find_global_extremes, round_down
from white import is_mostly_white

PHOTO_PATH = '*** your photo path **'
PIXEL_SIZE = 40

def main(image, is_white):
    width, height = image.size

    resized_width = int(round_down(width / PIXEL_SIZE))
    resized_height = int(round_down(height / PIXEL_SIZE))
    image_cropped = image.crop((0, 0, PIXEL_SIZE * resized_width, PIXEL_SIZE * resized_height))
    w, h = image_cropped.size

    pixels = image_cropped.load()

    # Using list comprehensions with proper bounds checking
    r_list = [[pixels[x, y][0] for x in range(min(h, w))] for y in range(min(w, h))]
    g_list = [[pixels[x, y][1] for x in range(min(h, w))] for y in range(min(w, h))]
    b_list = [[pixels[x, y][2] for x in range(min(h, w))] for y in range(min(w, h))]

    r_list_t, g_list_t, b_list_t = transpose(r_list), transpose(g_list), transpose(b_list)

    r_tuples = [find_max_increase_and_decrease_indices(row) for row in r_list]
    g_tuples = [find_max_increase_and_decrease_indices(row) for row in g_list]
    b_tuples = [find_max_increase_and_decrease_indices(row) for row in b_list]

    r_tuples_t = [find_max_increase_and_decrease_indices(row) for row in r_list_t]
    g_tuples_t = [find_max_increase_and_decrease_indices(row) for row in g_list_t]
    b_tuples_t = [find_max_increase_and_decrease_indices(row) for row in b_list_t]

    result_col_r = find_global_extremes(r_tuples, is_white)
    result_col_g = find_global_extremes(g_tuples, is_white)
    result_col_b = find_global_extremes(b_tuples, is_white)

    result_row_r = find_global_extremes(r_tuples_t, is_white)
    result_row_g = find_global_extremes(g_tuples_t, is_white)
    result_row_b = find_global_extremes(b_tuples_t, is_white)

    result_col = find_global_extremes([result_col_r, result_col_g, result_col_b], is_white)
    result_row = find_global_extremes([result_row_r, result_row_g, result_row_b], is_white)

    return sorted(result_col), sorted(result_row)

if __name__ == "__main__":
    im = Image.open(PHOTO_PATH)
    IS_WHITE = is_mostly_white(PHOTO_PATH)
    col, row = main(im, IS_WHITE)
    start, end = (col[0], row[0]), (col[1], row[1])
    draw_square(im, start, end)