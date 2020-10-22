import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    delimited_name = list(new_name)
    count = 0
    while len(delimited_name) != count:
        for i, character in enumerate(delimited_name):
            if i == 0:
                new_character = delimited_name[0]
                delimited_name[0] = new_character.upper()
            try:
                if character == "_" and delimited_name[(i + 1)].islower():
                    new_character = delimited_name[(i + 1)]
                    delimited_name[(i + 1)] = new_character.upper()
            except IndexError:
                pass
            try:
                if character == "(" and delimited_name[(i + 1)].islower():
                    new_character = delimited_name[(i + 1)]
                    delimited_name[(i + 1)] = new_character.upper()
            except IndexError:
                pass
            try:
                if character.islower() and delimited_name[(i + 1)].isupper():
                    delimited_name = delimited_name[:i + 1] + ["_"] + delimited_name[(i + 1):]
            except IndexError:
                pass
        count += 1
    new_name = ''.join(delimited_name)
    return new_name


main()

