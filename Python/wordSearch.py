import os
import os.path
import sys

def main(sourceDirectory, findMe, notMe):
    for path, folders, fileNames in os.walk(sourceDirectory):
        for file in fileNames:
            #if file.endswith(".php"):
            with open(os.path.join(path, file), 'r', encoding='latin1') as sourceFile:
                lines = sourceFile.readlines()
                for line in lines:
                    words = line.split()
                    for word in words:
                        if word == findMe and word != notMe:
                            with open(file, 'a') as writePath:
                                writePath.write(line)
                                print(sourceFile)

main("/path/to/directory", "WordToSearch", "WordToExclude")
