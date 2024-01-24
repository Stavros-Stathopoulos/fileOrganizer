# File System Organizer project
import fileModules


def mainFunc():
    print("Welcome to Empty Folder Remover")
    name = input("Enter the name of the directory to be checked for empty folders: ")
    workingDirName = fileModules.findFolder(dirName=name)
    try:
        if fileModules.verifyFolder(workingDirName) is False:
            raise fileModules.FolderNotVerified
        else:
            print("Folder is verified")
            print("Removing empty folders...")
            fileModules.removeEmptyFolders(workingDirName)

    except fileModules.FolderNotVerified:
        print("Folder is not verified")
        return 1
    except Exception as e:
        print("Error Occurred: ", e)
