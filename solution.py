def run(image, alpha):
    if not image or not image[0]:
        return []

    stretched = []
    for row in image:
        new_row = []
        for value in row:
            new_value = max(1, min(255, alpha * value))
            new_row.append(int(new_value))
        stretched.append(new_row)

    height = len(stretched)
    width = len(stretched[0])
    pad_value = 1
    padded = [[pad_value] * (width + 2)]
    for row in stretched:
        padded.append([pad_value] + row + [pad_value])
    padded.append([pad_value] * (width + 2))

    kernel_size = 3
    kernel_area = kernel_size * kernel_size
    output = []
    for i in range(height):
        out_row = []
        for j in range(width):
            pixel_sum = 0
            for row_offset in range(kernel_size):
                for col_offset in range(kernel_size):
                    pixel_sum += padded[i + row_offset][j + col_offset]
            out_row.append(pixel_sum // kernel_area)
        output.append(out_row)

    return output
