import os

def wordSearch_And_Write(source_directory, find_me, not_me):
    for path, _, filenames in os.walk(source_directory):
        for filename in filenames:
            file_path = os.path.join(path, filename)
            with open(file_path, 'r', encoding='latin1') as source_file:
                lines = source_file.readlines()

            for line in lines:
                if find_me in line and not_me not in line:
                    with open(filename, 'a') as write_file:
                        write_file.write(line)
                        print(f"Found in: {file_path}")
                        break  # Break after the first match per file for efficiency

if __name__ == "__main__":
    wordSearch_And_Write("/path/to/directory", "WordToSearch", "WordToExclude")
