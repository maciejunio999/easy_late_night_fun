from PIL import Image

def is_mostly_white(image_path, threshold=200):
    """
    Określa, czy zdjęcie jest w większości białe.

    Parameters:
    - image_path: Ścieżka do pliku obrazu.
    - threshold: Próg jasności. Piksele o jasności poniżej tego progu są uważane za białe. Domyślnie 200.

    Returns:
    - True, jeśli zdjęcie jest w większości białe, w przeciwnym razie False.
    """
    # Wczytaj obraz
    img = Image.open(image_path)

    # Pobierz dane pikseli
    pixels = img.getdata()

    # Zlicz piksele, które są jasniejsze niż próg
    white_pixels = sum(1 for pixel in pixels if pixel[0] > threshold and pixel[1] > threshold and pixel[2] > threshold)

    # Określ, czy większość pikseli jest biała
    ratio_white = white_pixels / len(pixels)
    return ratio_white > 0.5  # Załóżmy, że jeśli więcej niż 50% pikseli jest jasnych, to jest to zdjęcie w większości białe
