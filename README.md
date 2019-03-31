# File-System
Main.py has test cases showcasing the basic operations available.


Problem Statement:
The assignment is to design and implement an in-memory file system. This file-system consists of 4 types of entities: Drives, Folders, Text files, Zip files.

These entities, very much like their “real” file-system counterparts, obey the following relations.

a. A folder, a drive or a zip file, may contain zero to many other folders, or files (text or zip).

b. A text file does not contain any other entity.

c. A drive is not contained in any entity.

d. Any non-drive entity must be contained in another entity.

If entity A contains entity B then we say that A is the parent of B.

Every entity has the following properties:

* Type – The type of the entity (one of the 4 type above).

* Name - An alphanumeric string. Two entities with the same parent cannot have the same name. Similarly, two drives cannot have the same name.

* Path – The concatenation of the names of the containing entities, from the drive down to and including the entity. The names are separated by ‘\’.

* A text file has a property called Content which is a string.

* Size – an integer defined as follows:

* For a text file – it is the length of its content.

* For a drive or a folder, it is the sum of all sizes of the entities it contains.

* For a zip file, it is one half of the sum of all sizes of the entities it contains.

The system should be capable of supporting file-system like operations

1) Create – Creates a new entity.

Arguments: Type, Name, Path of parent.

Exceptions: Path not found; Path already exists; Illegal File System Operation (if any of the rules a-d above is violated).

2) Delete – Deletes an existing entity (and all the entities it contains).

Arguments: Path

Exceptions: Path not found.

3) Move – Changing the parent of an entity.

Arguments: Source Path, Destination Path.

Exceptions: Path not found; Path already exists, Illegal File System Operation.

4) WriteToFile – Changes the content of a text file.

Arguments: Path, Content

Exceptions: Path not found; Not a text file.

Tasks:

a. Come up with the design for this system. Full implementation is not required, but only to the level which you feel is a “proof of concept”.

b. Show a sketch of implementation of the Move operation.

c. Explicitly implement the property Size.
