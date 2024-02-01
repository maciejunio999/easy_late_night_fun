from PIL import ImageDraw

def draw_square(image, start_pixel, end_pixel, color=(255, 0, 0), thickness=2):
    """
    Rysuje kwadrat na obrazie.

    Parameters:
    - image: Obraz PIL.
    - start_pixel: Krotka zawierająca współrzędne (x, y) lewego górnego rogu kwadratu.
    - end_pixel: Krotka zawierająca współrzędne (x, y) prawego dolnego rogu kwadratu.
    - color: Kolor kwadratu w formacie RGB. Domyślnie czerwony.
    - thickness: Grubość linii kwadratu. Domyślnie 2.
    """
    draw = ImageDraw.Draw(image)
    draw.rectangle([start_pixel, end_pixel], outline=color, width=thickness)

    image.show()