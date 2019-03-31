import EntityType as Type
import Exceptions


class Entity:
    # parent here acts as a link from sub files link to parent entity
    # ( for back tracking )( represented by `..` in linux)
    def __init__(self, entity_type, entity_name, entity_path, parent=None, content=""):
        self.eType = entity_type
        self.name = entity_name
        self.path = entity_path
        self.subComponents = {}
        self.parent = parent
        self.size = 0
        self.content = ""
        if self.eType is Type.EntityType.Text:
            self.content = content

    def get_name(self):
        return self.name

    def set_name(self, entity_name):
        self.name = entity_name

    def get_path(self):
        return self.path

    def get_type(self):
        return self.eType

    def get_parent(self):
        return self.parent

    # TODO: modification of this method:
    # have a status variable to check if new files were created or data modified in files
    # use parent pointer to update size of parent on file changes
    # avoids recursive calling every time
    def calculate_size(self):
        if self.eType == Type.EntityType.Text:
            self.size = len(self.content)

        else:
            self.size = 0
            for _, component in self.subComponents.items():
                self.size += component.calculate_size()

            if self.eType is Type.EntityType.Zip:
                self.size /= 2

        return self.size

    def create_sub_entity(self, entity_type, entity_name, content=""):
        entity_path = self.path + '\\' + entity_name

        if self.eType is Type.EntityType.Text:
            raise Exceptions.IllegalFileSystemOperation("Cannot create sub component for a text file.")

        if entity_name in self.subComponents:
            raise Exceptions.PathAlreadyExists("Entity " + entity_name + " already exists.")

        if entity_type is not Type.EntityType.Text:
            content = ""
        self.subComponents[entity_name] = Entity(entity_type, entity_name, entity_path, self, content)

    def move_entity(self, entity_object, new_name=""):
        if entity_object.get_type is Type.EntityType.Drives:
            raise Exceptions.IllegalFileSystemOperation("Drive cannot be made as a sub component.")
        if new_name == "":
            new_name = entity_object.get_name()
        self.subComponents[new_name] = entity_object
        self.subComponents[new_name].set_name(new_name)
        self.subComponents[new_name].modify_path(self.path)

    def get_component(self, entity_name):
        if entity_name in self.subComponents:
            return self.subComponents[entity_name]
        return None

    def write_content_to_file(self, content):
        if self.eType == Type.EntityType.Text:
            self.content = content
        else:
            raise Exceptions.NotATextFile("Cannot write contents to Entity other than a text file.")

    def ls(self, with_details=False):
        if len(self.subComponents) == 0:
            print("`empty`")

        for name, entity in self.subComponents.items():
            if with_details:
                print("Name: " + name + " Type: " + str(entity.get_type())
                      + " Size: " + str(entity.calculate_size()))
            else:
                print(name)

    def __delete_sub_components(self):
        temp_dict = dict(self.subComponents)
        for name, entity in self.subComponents.items():
            entity.__delete_sub_components()
            print("Deleting: " + self.path + "\\" + name)
            del temp_dict[name]
        self.subComponents = temp_dict

    def delete_sub_component(self, entity_name):
        self.subComponents[entity_name].__delete_sub_components()
        print("Deleting: " + self.path + "\\" + entity_name)
        del self.subComponents[entity_name]

    def get_sub_component(self, entity_name):
        if entity_name in self.subComponents:
            return self.subComponents[entity_name]
        return None

    def modify_path(self, parent_path):
        self.path = parent_path + "\\" + self.name
        for name, entity in self.subComponents.items():
            entity.modify_path(self.path)

    def remove_sub_component(self, entity_name):
        print("Deleting: " + self.path + "\\" + entity_name + "\n")
        del self.subComponents[entity_name]
