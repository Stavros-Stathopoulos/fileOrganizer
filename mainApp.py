# File System Organizer project
import mainFileOrganizerBYExtension
import mainFindDIRORFile
import mainRemoveFilesBYExtension
import mainRemoveEmptyFolders


def driverFunc():
    print("Welcome to File System Organizer")
    print("Select the operation to be performed: ")
    print("1. Organize files by extension")
    print("2. Remove files by extension")
    print("3. Remove empty folders")
    print("4. Find a file")
    print("5. Find a folder")
    print("6. Exit")
    operation = int(input("Enter the operation to be performed: "))

    if operation == 1:
        mainFileOrganizerBYExtension.mainFunc()
    elif operation == 2:
        mainRemoveFilesBYExtension.mainFunc()
    elif operation == 3:
        mainRemoveEmptyFolders.mainFunc()
    elif operation == 4:
        mainFindDIRORFile.mainFunc(typein="file")
    elif operation == 5:
        mainFindDIRORFile.mainFunc(typein="folder")
    elif operation == 6:
        print("Exiting the program")
        return 0
    else:
        print("Invalid operation")
        return 1


if __name__ == "__main__":
    driverFunc()
