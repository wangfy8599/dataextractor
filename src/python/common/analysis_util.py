import os.path


def script_dir():
    return os.path.dirname(os.path.abspath(__file__))


def write_csv_file(df, file_name):
    df.to_csv(file_name, index=False, lineterminator='\n', encoding='utf_8_sig')
