from PIL import Image
import numpy as np


def print_3D_array(array):
    """
    Prints a formatted output of the first and last rows of the image array.
    """
    print("[[[" + " ".join(map(str, array[0][0])) + "]")
    print("  [" + " ".join(map(str, array[0][1])) + "]")
    print("  [" + " ".join(map(str, array[0][2])) + "]")
    print("    ...")
    print("  [" + " ".join(map(str, array[-1][-3])) + "]")
    print("  [" + " ".join(map(str, array[-1][-2])) + "]")
    print("  [" + " ".join(map(str, array[-1][-1])) + "]]]")


def check_image(path: str) -> bool:
    """
    Check if a path to an image is valid
    """
    with Image.open(path) as img:
        img.verify()
        return True
    return False


def ft_load(path: str) -> list:
    """
    Assert that the path is valid
    Print the dimension of the image
    Return the RGB value of every pixel
    """
    try:
        assert check_image(path), "image is not valid"

        img = Image.open(path)

        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return (img_array)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except FileNotFoundError:
        print(f"FileNotFoundError: The file \"{path}\" was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
