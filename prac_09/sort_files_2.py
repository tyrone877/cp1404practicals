import os


def main():
    file_extension_name_to_category = {}
    os.chdir("FilesToSort")
    for file_name in os.listdir('.'):
        file_extension_name = file_name.split('.')[-1]
        if file_extension_name not in file_extension_name_to_category:
            category = input(f"What category would you like to sort {file_extension_name} files into? ")
            file_extension_name_to_category[file_extension_name] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(file_name, f"{file_extension_name_to_category[file_extension_name]}/{file_name}")


main()
