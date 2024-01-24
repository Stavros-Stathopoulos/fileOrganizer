# File System Organizer project
import fileModules


def mainFunc():
    print("Welcome to delete files by extension")
    name = input("Enter the name of the directory to be organized by removing the files: ")
    workingDirName = fileModules.findFolder(dirName=name)
    try:
        if fileModules.verifyFolder(workingDirName) is False:
            raise fileModules.FolderNotVerified
        else:
            print("Folder is verified")
            fileExtensionToRemove = input("Enter the extension of the files to be removed( .pdf ) : ")
            print("Removing the files...")
            success = fileModules.removeFiles(workingDirName, fileExtensionToRemove)
            if success == 0:
                print("Files removed successfully")
            else:
                print("Files not removed")

    except fileModules.FolderNotVerified:
        print("Folder is not verified")
        return 1
    except Exception as e:
        print("Error Occurred: ", e)
