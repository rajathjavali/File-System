import Entity
import EntityType
import Exceptions
import helper


class FileSystem(object):
    class __FileSystem:
        def __init__(self):
            self.list_of_drives = {}

        def add_drive(self, drive_name):
            if drive_name in self.list_of_drives:
                raise Exceptions.PathAlreadyExists("Dive " + drive_name + " already exists.")
            self.list_of_drives[drive_name] = Entity.Entity(EntityType.EntityType.Drives, drive_name, "\\" + drive_name)

        def __trace_path__(self, path, entity):
            # default case if we trying to find an entity in a null path
            if path is None or len(path) == 0:
                return None

            sub_entity = entity.get_component(path[0])

            # either sub_entity is None and we couldn't find parent entity
            # or we found the parent entity and returning the object
            if len(path) == 1:
                return sub_entity
            # path hasn't reached the parent and we couldn't find an entity on the way
            elif sub_entity is None:
                raise Exceptions.PathNotFound(entity.get_name() + " has no component: " + path[0])

            return self.__trace_path__(path[1:], sub_entity)

        def get_entity_at_path(self, path_list):
            if path_list is None or len(path_list) == 0:
                return None
            if path_list[0] in self.list_of_drives:
                if len(path_list) == 1:
                    return self.list_of_drives[path_list[0]]
                return self.__trace_path__(path_list[1:], self.list_of_drives[path_list[0]])
            return None

        def ls(self, ls_path, with_details=False):
            path = helper.get_path_list(ls_path)
            if len(path) == 0:
                drives = ""
                for drive in self.list_of_drives:
                    if with_details:
                        drives += drive + " Size: " + str(self.list_of_drives[drive].calculate_size()) + "\n"
                    else:
                        drives += drive + " "
                if drives == "":
                    print("`empty`")
                print(drives)
            else:
                entity = self.get_entity_at_path(path)
                entity.ls(with_details)

        def write_to_file(self, file_path, contents):
            path = helper.get_path_list(file_path)
            text_file = self.get_entity_at_path(path)
            text_file.write_content_to_file(contents)

        def create_entity(self, entity_type, entity_name, parent_path="", content=""):
            if entity_type is EntityType.EntityType.Drives:
                if parent_path is not None or parent_path != "\\" or parent_path != "":
                    raise Exceptions.IllegalFileSystemOperation("Drive cannot be a sub component")
                return self.add_drive(entity_name)

            path = helper.get_path_list(parent_path)

            parent = self.get_entity_at_path(path)
            if parent:
                parent.create_sub_entity(entity_type, entity_name, content)
                return True
            else:
                raise Exceptions.PathNotFound("No Drive named: " + path[0])

        def delete_entity(self, path):
            entity_path = helper.get_path_list(path)
            entity = self.get_entity_at_path(entity_path)
            parent = entity.get_parent()
            parent.delete_sub_component(entity.get_name())

        # TODO: have made assumption of source path has the folder or file or zip included in the path
        # destination source: first I assume the destination path doesn't include the name of the file to be renamed
        # if I dont find the path I try to find the full destination path assume the user wants to retain the name of
        # source file. For Ex: mv C\github\text.txt D ( here file name should be retained as text.txt )
        def move_entity(self, source_path, dest_path):
            source_path_list = helper.get_path_list(source_path)
            dest_path_list = helper.get_path_list(dest_path)

            source_parent = self.get_entity_at_path(source_path_list[:-1])

            if not source_parent:
                raise Exceptions.PathNotFound("Parent Entity not found: " + source_path)

            dest_parent = self.get_entity_at_path(dest_path_list[:-1])
            dest_name = dest_path_list[-1]
            if not dest_parent:
                dest_parent = self.get_entity_at_path(dest_path_list)
                dest_name = source_path_list[-1]
            if not dest_parent:
                raise Exceptions.PathNotFound("Parent Entity not found: " + source_path)

            entity = source_parent.get_sub_component(source_path_list[-1])
            if entity is None:
                raise Exceptions.PathNotFound("Entity not found: " + source_path)

            dest_entity = dest_parent.get_sub_component(dest_name)
            if dest_entity is not None:
                raise Exceptions.PathAlreadyExists("Entity already exists: " + dest_path)

            dest_parent.move_entity(entity, dest_name)
            source_parent.remove_sub_component(source_path_list[-1])

    instance = None

    def __new__(cls, *args, **kwargs):
        if not FileSystem.instance:
            FileSystem.instance = FileSystem.__FileSystem()
        return FileSystem.instance
