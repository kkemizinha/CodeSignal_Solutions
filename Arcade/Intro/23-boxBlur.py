def boxBlur(image):
    # Final result img
    output_img = []
    # Row to be added to output_img
    row_aux = []
    # 3x3 Box img to process
    square_aux = []
    height, width = len(image)-1, len(image[0]) -1

    for i in range(1,height):
        row_aux = []
        for j in range(1, width):
            square_aux = [[image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
                          [image[i][j-1], image[i][j], image[i][j+1]],
                          [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]]
            value = square_matrix(square_aux)
            row_aux.append(value)
        output_img.append(row_aux)
    return output_img
    

def square_matrix(square):
    tot_sum = 0
    # Sum of all pixels
    for i in range(3):
        for j in range(3):
            tot_sum += square[i][j]
    # Round average number down
    return tot_sum // 9