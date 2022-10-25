from PIL import Image, ImageDraw

def sliding_window(x, y, values, n):
    l = []
    for a in range(-1, 2):
        for b in range(-1, 2): # posun okna
            windows = []
            middle_pixel = values[x + a, y + b]
            for i in range(-n, n + 1):
                for j in range(-n, n + 1):  # procházení pixelů v okně
                    other_pixel = values[x + i + a, y + j + b]
                    windows.append((other_pixel - middle_pixel)**2)
            l.append(sum(windows))
    return min(l)

def moravec(im, px_val, window_size): # def goes through each pixel of image (except edges)
    window_diameter = window_size // 2
    values = []
    for x in range(window_diameter, im.width - window_diameter - 1): # going through x-coords of image
        for y in range(window_diameter, im.height - window_diameter - 1): # going through y-coords of img
            rohovitost = sliding_window(x, y, px_val, window_diameter) # počítá rohovitost
            values.append(((x, y), rohovitost))
    return values

def draw(values, image, threshold): # def for visualizing edge pixels
    for pix in values:
        if pix[1] > threshold:
            pts = ImageDraw.Draw(image)
            pts.point(pix[0], fill="red")
    return image

if __name__ == "__main__":

    image_name = "lena.tif"
    im = Image.open(image_name)
    px_values = im.load() # load pixel values - list of tuples ((x, y), value)

    T = 500  # threshold value
    window_size = 3  # window size

    # counting edge pixels
    val = moravec(im, px_values, window_size)

    # saving x and y coordinates of edge pixels into list - TADY TO JE VÝSLEDEK ZADÁNÍ
    hrany = []
    for v in val:
        if v[1] > T:
            hrany.append(v[0])

    print(hrany)

    image = draw(val, im, T)
    # image.save(f"view_{str(window_size)}_{str(T)}.png")
