# File System Organizer project
import os


class FolderNotVerified(Exception):
    pass


class OrganizeFolderDoesNotExcists(Exception):
    pass


fileExtensions = []
files = []


def removeFiles(workingDirName, fileExtensionToRemove=None):
    success = 1
    if fileExtensionToRemove is None:
        print("Unknown file extension")
        return 1
    for file in os.listdir(workingDirName):
        if os.path.isdir(os.path.join(workingDirName, file)):
            # print("Skipping folder: " + str(file))
            continue
        else:
            # print("File: " + str(file))
            # print("Extension: " + str(getExtension(file)))
            if "." + str(getExtension(file)) == fileExtensionToRemove:
                os.remove(os.path.join(workingDirName, file))
                print("Removed file: " + str(file))
                success = 0
            else:
                continue
    return success


def verifyFolder(workingDirName):
    verify = input("Are you sure you want to organize the folder {}? (Y/N): ".format(workingDirName))
    if verify == "Y" or verify == "y":
        return True
    return False


def doesNotExistsInFiles(file):
    if file in files:
        return False
    return True


def organizeFiles(workingDirName):
    for file in os.listdir(workingDirName):
        if os.path.isdir(os.path.join(workingDirName, file)):
            continue
        else:
            extension = getExtension(file)
            if extension == "No Extension":
                continue
            else:
                folderName = extension + "_Files_FileOrganizer"
                if not os.path.exists(os.path.join(workingDirName, folderName)):
                    raise OrganizeFolderDoesNotExcists
                os.rename(os.path.join(workingDirName, file), os.path.join(workingDirName, folderName, file))


def getFileName(p=os.getcwd(), count=0):
    try:
        print("Current working directory is: " + str(p))
        # print("Files in the directory {} are:".format(os.path.basename(p)))
        if not os.listdir(p):
            # print("No files in the directory")
            return 0
        for file in os.listdir(p):
            # for file
            # print(file + "\t\tExtension:  " + getExtension(file))
            if doesNotExistsInFiles(file) is True:
                files.append(file)
            else:
                filename = file
                extension = getExtension(file)
                newFileName = filename + "(" + str(files.count(file)) + ")." + extension
                files.append(newFileName)

            # If folder
            if getExtension(file) == "Folder":  # If folder
                getFileName(p=os.path.abspath(os.path.join(p, file)), count=count + 1)
    except Exception as e:
        print("Error: " + str(e))

    # print("End of the directory {}".format(os.path.basename(p)))
    return 0


def fileExtensionExists(extension):
    if extension in fileExtensions:
        return True
    return False


def getExtension(file):
    if file == "venv":
        return "No Extension"
    elif file == "__pycache__":
        return "No Extension"
    extension = file.split(".")[-1]
    if extension == file:
        return "Folder"
    elif extension == "":
        return "No Extension"
    elif extension == "idea":
        return "No Extension"

    if extension not in fileExtensions:
        fileExtensions.append(extension)

    return extension


def findFolder(fileName=None, dirName=None, path=r"C:\Users\sstav"):
    if dirName is None:
        print('File name :    ', os.path.basename(fileName))
        print("Path of the file is:\t", end='')
    else:
        print('Directory name :    ', os.path.basename(dirName))
        print("Path of the directory is:\t", end='')

    for root, dirs, file in os.walk(path):
        if dirName is not None:
            for Name in dirs:
                if Name == dirName:
                    pathFound = os.path.abspath(os.path.join(root, Name))
                    # print(pathFound)
                    return pathFound
        if fileName is not None:
            for Name in file:
                if Name == fileName:
                    pathFound = os.path.abspath(os.path.join(root, Name))
                    # print(pathFound)
                    return pathFound
    return None


def createFolder(folderName, parentName):
    try:
        if not os.path.exists(os.path.join(parentName, folderName)):
            os.mkdir(os.path.join(parentName, folderName))
            print("Folder {} created successfully".format(folderName))
    except Exception as e:
        print("Error: " + str(e))


def removeEmptyFolders(path):
    for folders in os.listdir(path):
        foldersPath = os.path.join(path, folders)
        if os.path.isdir(foldersPath):
            if not os.listdir(foldersPath):
                print("Removing empty folder: " + str(foldersPath))
                os.rmdir(foldersPath)
            else:
                removeEmptyFolders(foldersPath)


if __name__ == "__main__":
    print("Welcome to File System Organizer")
    name = input("Enter the name of the directory to be organized: ")
    print(getFileName(p=findFolder(dirName=name)))
    print(fileExtensions)
