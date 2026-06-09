import threading

class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def read(self):
        return self.content

    def write(self, content):
        self.content = content


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.directories = {}
        self.lock = threading.Lock()
        self.parent = None

    def add_file(self, file):
        with self.lock:
            self.files[file.name] = file

    def add_directory(self, directory):
        self.directories[directory.name] = directory
        directory.parent = self

    def delete_file(self, file_name):
        if file_name in self.files:
            del self.files[file_name]

    def delete_directory(self, dir_name):
        if dir_name in self.directories:
            del self.directories[dir_name]

    def list_contents(self):
        return {
            "files": list(self.files.keys()),
            "directories": list(self.directories.keys())
        }
    
    def pwd(self):

        current = self
        path = []

        while current:
            path.append(current.name)
            current = current.parent

        path.reverse()

        return "/" + "/".join(path[1:])


class FileSystem:
    def __init__(self):
        self.root = Directory("root")

    def create_file(self, directory, file_name, content=""):
        file = File(file_name, content)
        directory.add_file(file)
        return file

    def create_directory(self, parent_directory, dir_name):
        directory = Directory(dir_name)
        parent_directory.add_directory(directory)
        return directory

    def delete_file(self, directory, file_name):
        directory.delete_file(file_name)

    def delete_directory(self, parent_directory, dir_name):
        parent_directory.delete_directory(dir_name)

    def read_file(self, directory, file_name):
        file = directory.files.get(file_name)

        if file is None:
            return "File not found"

        return file.read()

    def write_file(self, directory, file_name, content):
        file = directory.files.get(file_name)

        if file is None:
            return "File not found"

        file.write(content)

    def list_directory(self, directory):
        return directory.list_contents()