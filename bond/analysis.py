import pandas as pd



if __name__ == "__main__":
    with open(r"D:\github\dataextractor\bond\2022\10\23.html", "r") as f:
        df_table = pd.read_html(f)
        print(df_table)