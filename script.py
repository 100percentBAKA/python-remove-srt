import os


def delete_srt_files(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".srt"):
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        print("All .srt files deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    directory = input("Enter the directory path: ")

    if os.path.isdir(directory):
        delete_srt_files(directory)
    else:
        print("The provided path is not a directory.")
