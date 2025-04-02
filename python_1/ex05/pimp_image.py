import numpy as np
from PIL import Image


def ft_invert(array):
    """
    Take an image array
    Substract every pixel value from 255 to get the inverted color
    Show the new image
    """
    try:
        image = 255 - array

        Image.fromarray(image).show()

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def ft_red(array):
    """
    Takes an image array
    Creates a black image of the same size
    Keeps only the red color channel of the image
    Show the new image
    """
    try:
        red_channel = array[:, :, 0]

        image = np.zeros_like(array)
        image[:, :, 0] = red_channel

        Image.fromarray(image).show()

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def ft_green(array):
    """
    Takes an image array
    Creates a black image of the same size
    Keeps only the green color channel of the image
    Show the new image
    """
    try:
        green_channel = array[:, :, 0]

        image = np.zeros_like(array)
        image[:, :, 1] = green_channel

        Image.fromarray(image).show()

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def ft_blue(array):
    """
    Takes an image array
    Creates a black image of the same size
    Keeps only the blue color channel of the image
    Show the new image
    """
    try:
        blue_channel = array[:, :, 2]

        image = np.zeros_like(array)
        image[:, :, 2] = blue_channel

        Image.fromarray(image).show()

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def ft_grey(array):
    """
    Converts the image to grayscale.
    """
    try:
        grey_channel = (0.2989 * array[:, :, 0] +
                        0.5870 * array[:, :, 1] +
                        0.1140 * array[:, :, 2])

        image = np.zeros_like(array)
        image[:, :, 0] = grey_channel
        image[:, :, 1] = grey_channel
        image[:, :, 2] = grey_channel

        Image.fromarray(image).show()

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
