class DataReader:
    def __init__(self,filename):
        self.filename = filename
    def read_lines(self):
        try :
            with open(self.filename) as f:
                lines = []
                for line in f:
                    lines.append(line)
                return lines
        except FileNotFoundError:
            print("文件不存在。")
            return []
