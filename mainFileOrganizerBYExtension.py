# File System Organizer project
import fileModules


def mainFunc():
    print("Welcome to File System Organizer by extension")
    name = input("Enter the name of the directory to be organized: ")
    workingDirName = fileModules.findFolder(dirName=name)
    try:
        if fileModules.verifyFolder(workingDirName) is False:
            raise fileModules.FolderNotVerified
        else:
            print("Folder is verified")
            print("Organizing the folder...")
            fileModules.getFileName(p=workingDirName)
            for extension in fileModules.fileExtensions:
                if extension == "No Extension":
                    continue
                folderName = extension + "_Files_FileOrganizer"
                fileModules.createFolder(folderName, workingDirName)

            fileModules.organizeFiles(workingDirName)
            fileModules.removeEmptyFolders(workingDirName)

    except fileModules.FolderNotVerified:
        print("Folder is not verified")
        return 1
    except Exception as e:
        print("Error Occurred: ", e)

    print("End of the program. The Folder has been organized.")
    return 0


if __name__ == "__main__":
    mainFunc()
