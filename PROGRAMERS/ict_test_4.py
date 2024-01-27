def closestColor(pixels):
    closest_color_list = []
    for i in range(len(pixels)):
        pixel = pixels[i]
        r, g, b = pixel[:8], pixel[8:16], pixel[16:]
        r, g, b = int(r, 2), int(g, 2), int(b, 2)

        colors = {
            "Black": (0, 0, 0),
            "White": (255, 255, 255),
            "Red": (255, 0, 0),
            "Green": (0, 255, 0),
            "Blue": (0, 0, 255)
        }
        def calculate_distance(rgb1, rgb2):
            return ((rgb1[0] - rgb2[0]) ** 2 + (rgb1[1] - rgb2[1]) ** 2 + (rgb1[2] - rgb2[2]) ** 2) ** 0.5

        closest_color = None
        min_distance = 100000
        for color, rgb in colors.items():
            distance = calculate_distance((r, g, b), rgb)
            if distance == min_distance:
                closest_color = 'Ambiguous'
                min_distance = distance
            elif distance < min_distance:
                min_distance = distance
                closest_color = color
        closest_color_list.append(closest_color)
    return closest_color_list

pixels = ["000000001111111100000110"]
print(closestColor(pixels))
