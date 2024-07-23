class Processor:
    def __init__(self, file_path, meta_data, shared_data):
        self.file_path = file_path
        self.meta_data = meta_data
        self.shared_data = shared_data
        self.file_number = meta_data.get_file_number(file_path)
        self.total_file_cnt = meta_data.get_total_file_cnt()
     
    def read_file(self):
            with open(self.file_path, "r", encoding="utf8") as file:
                lines = file.readlines()

                for id, line in enumerate(lines):
                    word = line.rstrip()
                    word_number = self.file_number + self.total_file_cnt * (id - 1)

                    self.shared_data.set_word(word_number, word)