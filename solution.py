def run(image, alpha):
    if not image or not image[0]:
        return []

    stretched = []
    for row in image:
        new_row = []
        for value in row:
            new_value = alpha * value
            if new_value < 1:
                new_value = 1
            elif new_value > 255:
                new_value = 255
            new_row.append(new_value)
        stretched.append(new_row)

    height = len(stretched)
    width = len(stretched[0])
    pad_value = 1
    padded = [[pad_value] * (width + 2)]
    for row in stretched:
        padded.append([pad_value] + row + [pad_value])
    padded.append([pad_value] * (width + 2))

    output = []
    for i in range(height):
        out_row = []
        for j in range(width):
            total = 0.0
            for di in range(3):
                for dj in range(3):
                    total += padded[i + di][j + dj]
            out_row.append(int(total / 9))
        output.append(out_row)

    return output
