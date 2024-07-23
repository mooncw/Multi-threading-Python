class MetaData:
    def __init__(self):
        self.file_dict = {}
        self.total_file_cnt = 0

    def set_file(self, file_number, file_path):
        self.file_dict[file_path] = file_number
        self.total_file_cnt += 1

    def get_file_number(self, file_path):
        return self.file_dict[file_path]
    
    def get_total_file_cnt(self):
        return self.total_file_cnt