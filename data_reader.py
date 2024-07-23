import glob

class Reader:
    def __init__(self, meta):
        self.input_path = "./input"
        self.meta_data = meta

    def read_files(self):
        file_path_list = glob.glob(self.input_path)
        for file_path in file_path_list:
            file_number = self.get_file_number(file_path)
            self.meta_data.set_file(file_number, file_path)

    def get_file_number(file):
        return int(file.rsplit("/", 1)[-1].replace("file", ""))