import os
import shutil


def main():
    """Demo of os module functions."""
    print(f"Starting directory is: {os.getcwd()}")

    os.chdir('Lyrics/Christmas')

    print(f"Files in {os.getcwd()}:\n{os.listdir('.')}\n")

    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for file_name in os.listdir('.'):
        if os.path.isdir(file_name):
            continue

        new_file_name = get_fixed_filename(file_name)
        print(f"Renaming {file_name} to {new_file_name}")

        # TODO: Try these options one at a time
        # os.rename(file_name, new_file_name)
        shutil.move(file_name, 'temp/' + new_file_name)


def get_fixed_filename(file_name):
    new_file_name = file_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_file_name


def demo_walk():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print(f"Directory: {directory_name}")
        print(f"\tcontains subdirectories: {subdirectories}")
        print(f"\tand files: {filenames}")
        print(f"Current working directory is: {os.getcwd()}")

        # TODO: add a loop to rename the files
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


main()
# demo_walk()
