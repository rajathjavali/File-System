

# helps generate list of entities give a path
# trims out the empty entities
# ( this works since in linux /drive/folder//subfolder - is assumed as /drive/folder/./subfolder)
def get_path_list(path):
    path_list = path.split("\\")
    path_list = [x for x in path_list if x]
    return path_list
