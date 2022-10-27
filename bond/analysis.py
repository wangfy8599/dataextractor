import pandas as pd


def format_data(df):
    df = df.rename(columns=lambda s: s.replace(" ", ""))
    return df


def write_report(df):
    html = df.to_html(classes='table table-stripped')

    # write html to file
    with open("report.html", "w") as text_file:
        text_file.write(html)


def main():
    with open(r"D:\github\dataextractor\bond\2022\10\27.html", "r") as f:
        df_tables = pd.read_html(f)
        df = format_data(df_tables[0])
        df = df[["转债代码", "转债名称", "转债价格", "转股溢价率", "纯债价值", "剩余年限", "转债余额", "税前收益率", "新式排名"]]
        df = df.query("转债价格 < 130").sort_values(by=['新式排名'], ascending=True)
        df.reset_index(drop=True, inplace=True)
        write_report(df)
        print(df)


if __name__ == "__main__":
    main()
