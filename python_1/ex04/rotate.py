from load_image import ft_load_as_gray
from load_image import print_array
from load_image import print_2D_transpose
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def transpose(matrix) -> np.array:
    """
    Take a matrix
    Transpose the matrix
    Return the transposed matrix
    """
    transposedMatrix = [
        [matrix[x][y] for x in range(len(matrix))]
        for y in range(len(matrix[0]))
    ]
    return np.array(transposedMatrix)


def zoom_in(img_array) -> np.array:
    """
    Take an image array
    Zoom in on the image
    Return the new image array
    """
    height = img_array.shape[0]
    new_height, new_width = 400, 400
    height_start = round((height - new_height) / 4)
    width_start = round(new_width + 50)

    img_out = img_array[
        height_start:height_start + new_height,
        width_start:width_start + new_width
    ]

    return img_out


def main():
    """
    Load the animal image as gray
    Zoom in
    Show the new zoomed image
    """
    path = "../animal.jpeg"

    try:
        img_array = ft_load_as_gray(path)

        img_out = zoom_in(img_array)

        print(f"The shape of the image is: {img_out.shape}")
        print_array(img_out)

        img_out = transpose(img_out)  # Convert NumPy array to list

        print(f"New shape after Transpose: {img_out.shape}")
        print_2D_transpose(img_out)

        zoomed_img = Image.fromarray(np.array(img_out))
        plt.imshow(zoomed_img, cmap=plt.get_cmap('gray'))
        plt.show()

    except Exception as e:
        print(f"Exception: {e}")
        exit(1)


if __name__ == "__main__":
    main()
