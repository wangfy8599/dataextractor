import pandas as pd


def format_data(df):
    df = df.rename(columns=lambda s: s.replace(" ", ""))
    return df


def main():
    with open(r"D:\github\dataextractor\bond\2022\10\23.html", "r") as f:
        df_tables = pd.read_html(f)
        df = format_data(df_tables[0])
        print(df)


if __name__ == "__main__":
    main()
