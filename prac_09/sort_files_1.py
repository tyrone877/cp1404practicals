import os


def main():
    os.chdir("FilesToSort")
    for file_name in os.listdir('.'):
        file_extension = file_name.split('.')[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        os.rename(file_name, f"{file_extension}/{file_name}")


main()
