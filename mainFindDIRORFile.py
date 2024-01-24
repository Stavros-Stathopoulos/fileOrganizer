# File System Organizer project
import fileModules


def mainFunc(typein):
    if typein == "file":
        print("Welcome to File Finder")
        name = input("Enter the name of the file to be found: ")
        pathOfFile = fileModules.findFolder(fileName=name)
        if pathOfFile is None:
            print("File not found")
        else:
            print("File found at: ", pathOfFile)

    elif typein == "folder":
        print("Welcome to Folder Finder")
        name = input("Enter the name of the folder to be found: ")
        pathOfFolder = fileModules.findFolder(dirName=name)
        if pathOfFolder is None:
            print("Folder not found")
        else:
            print("Folder found at: ", pathOfFolder)
    else:
        print("Invalid input")
    pass
