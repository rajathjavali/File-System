import FileSystem
import EntityType


# Test Cases
def create_list_of_drives():
    print("\n\n~~~~~~~~~~~Testing: Creating Drives~~~~~~~~~\n\n")
    print("Creating List of Drives")
    file_system = FileSystem.FileSystem()
    file_system.add_drive("C")
    file_system.add_drive("D")
    file_system.add_drive("E")
    file_system.add_drive("F")
    file_system.ls("\\")


def create_folder():
    print("\n\n~~~~~~~~~~~Testing: Creating Folders~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Folders, "rajath", "\\C")
    print("Created folder `rajath` in drive C")
    file_system.create_entity(EntityType.EntityType.Folders, "github", "\\D")
    print("Created folder `github` in drive D")
    print("Calling `ls` on drive C")
    file_system.ls("\\C")
    print("Calling `ls` on drive D")
    file_system.ls("\\D")
    print("Calling `ls` on drive E")
    file_system.ls("\\E")
    print("Calling `ls` on drive F")
    file_system.ls("\\F")


def create_text_files():
    print("\n\n~~~~~~~~~~~Testing: Creating Files~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Text, "text.txt", "\\D", "this is a test file")
    print("Created Text file `text.txt` in drive D")
    file_system.create_entity(EntityType.EntityType.Text, "text.txt", "\\D\\github", "this is a test file 2")
    print("Created Text file `text.txt` in folder D\\github")
    print("Calling `ls` on drive D")
    file_system.ls("\\D")
    print("Calling `ls` on drive D\\github")
    file_system.ls("\\D\\github")


def create_zip_file():
    print("\n\n~~~~~~~~~~~Testing: Creating Zip File~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Zip, "test.zip", "\\E")
    print("Created Zip file `test.zip` in Drive E")
    file_system.create_entity(EntityType.EntityType.Zip, "test.zip", "\\D\\github")
    print("Created Zip file `test.zip` in folder D\\github")
    print("Calling `ls` on drive E")
    file_system.ls("E")
    print("Calling `ls` on drive D\\github")
    file_system.ls("\\D\\github")


def create_files_in_zip():
    print("\n\n~~~~~~~~~~~Testing: Creating file in Zip File~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Text, "text.txt", "\\E\\test.zip", "inside zip folder")
    print("Created Text file `test.txt` in file E\\test.zip")
    file_system.create_entity(EntityType.EntityType.Text, "text.txt", "\\D\\github\\test.zip", "inside zip folder")
    print("Created Text file `test.txt` in folder D\\github\\test.zip")
    print("Calling `ls` on drive E\\test.zip")
    file_system.ls("E\\test.zip")
    print("Calling `ls` on drive D\\github\\test.zip")
    file_system.ls("\\D\\github\\test.zip")
    file_system.ls("\\D\\github", True)


def getting_size_of_drives():
    print("\n\n~~~~~~~~~~~Testing: Drive Sizes~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.ls("", True)


def changing_contents_of_file():
    print("\n\n~~~~~~~~~~~Testing: Changing Text File Contents~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    print("Calling `ls` on drive E\\test.zip")
    file_system.ls("E\\test.zip", True)
    file_system.write_to_file("\\E\\test.zip\\text.txt", "New Contents of the text file")
    print("Changed the contents of the file E\\test.zip\\text.txt")
    print("Calling `ls` on drive E\\test.zip")
    file_system.ls("E\\test.zip", True)


def delete_text_file():
    print("\n\n~~~~~~~~~~~Testing: Deleting Text File~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.ls("", True)
    print("\n\n")
    print("Calling `ls` on drive  D\\github")
    file_system.ls("D\\github")
    file_system.delete_entity("D\\github\\text.txt")
    print("Deleting the file D\\github\\text.txt")
    print("Calling `ls` on drive D\\github")
    file_system.ls("D\\github")
    print("\n\n")
    file_system.ls("", True)
    print("\n\n")


def delete_folder():
    print("\n\n~~~~~~~~~~~Testing: Deleting Folder~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Folders, "test_delete_folder", "\\E\\test.zip")
    file_system.create_entity(EntityType.EntityType.Text, "text.txt", "\\E\\test.zip\\test_delete_folder",
                              "inside zip/test_delete_folder")

    print("Creating new folders and files to test delete operation")
    print("Created E\\test.zip\\test_delete_folder\nCreated E\\test.zip\\test_delete_folder\\text.txt\n\n")
    file_system.ls("", True)
    print("Calling `ls` on drive  E\\test.zip")

    file_system.ls("E\\test.zip")
    print("Deleting the folder E\\test.zip\\test_delete_folder and its contents")
    file_system.delete_entity("E\\test.zip\\test_delete_folder")
    print("Calling `ls` on drive E\\test.zip")
    file_system.ls("E\\test.zip")
    print("\n\n")
    file_system.ls("", True)


def move_file():
    print("\n\n~~~~~~~~~~~Testing: Moving File~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Text, "c_drive.txt", "C")
    print("Create new file c_drive.txt in drive C")
    print("Calling `ls` on drive  C")
    file_system.ls("C")
    print("\n\nMoving file c_drive.txt from C to F\n")
    file_system.move_entity("C\\c_drive.txt", "F")
    print("Calling `ls` on drive F")
    file_system.ls("F")
    print("Calling `ls` on drive C")
    file_system.ls("C")


def move_folder():
    print("\n\n~~~~~~~~~~~Testing: Moving Folder~~~~~~~~~\n\n")

    file_system = FileSystem.FileSystem()
    file_system.create_entity(EntityType.EntityType.Folders, "folder1", "C")
    print("Created new folder folder1 in drive C")
    file_system.create_entity(EntityType.EntityType.Text, "text1.txt", "C\\folder1", "contents of text1.txt")
    print("Created new file text1.txt at C\\folder1")
    print("\nCalling `ls` on drive  C")
    file_system.ls("C")
    print("Calling `ls` on drive  C\\folder1")
    file_system.ls("C\\folder1")
    print("\n\nMoving folder folder1 from C to F\n\n")
    file_system.move_entity("C\\folder1", "F")
    print("Calling `ls` on drive F")
    file_system.ls("F")
    print("Calling `ls` on drive F\\folder1")
    file_system.ls("F\\folder1")
    print("Calling `ls` on drive C")
    file_system.ls("C")


def main():
    # create drives
    create_list_of_drives()
    # create folders
    create_folder()
    # create text file
    create_text_files()
    # create zip files
    create_zip_file()
    # populate zip files
    create_files_in_zip()
    # display size details on all drives
    getting_size_of_drives()
    # modifying text file
    changing_contents_of_file()
    # checking the new dive size details
    getting_size_of_drives()
    # deleting text file
    delete_text_file()
    # deleting folder
    delete_folder()
    # moving text file
    move_file()
    # moving folder file
    move_folder()


if __name__ == "__main__":
    main()
