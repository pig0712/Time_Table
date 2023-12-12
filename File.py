import pandas as pd

class ExcelFile:
    @classmethod
    def read(cls, path):
        excel_data = pd.read_excel(path)
        return excel_data

    @classmethod
    def save(cls, name, data):
        data.to_excel(name, index=False)
        return cls

if __name__ == "__main__":
    df = ExcelFile.read("./save.xlsx")
    print(df)
    
    