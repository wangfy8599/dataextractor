import pandas as pd
import re

pattern_year_day = re.compile("([\\d\\.]+)year([\\d\\.]+)day")
pattern_year = re.compile("([\\d\\.]+)year")
pattern_day = re.compile("([\\d\\.]+)day")


def change_remain_days(x):
    x = x.replace("年", "year").replace("天", "day")
    m = pattern_year_day.match(x)
    if m:
        year = float(m.group(1))
        day = float(m.group(2))
        x = "{:.02f}".format(year + day/366)
    else:
        m = pattern_year.match(x)
        if m:
            year = float(m.group(1))
            x = "{:.02f}".format(year)
        else:
            m = pattern_day.match(x)
            if m:
                day = float(m.group(1))
                x = "{:.02f}".format(day/366)
    return x


def format_data(df):
    df = df.rename(columns=lambda s: s.replace(" ", ""))
    # process column
    df["剩余年限"] = df["剩余年限"].apply(change_remain_days)
    return df


def write_report(df):
    html = df.to_html(classes='table table-stripped')

    # write html to file
    with open("report.tpl", "r") as input_file, open("report.html", "w") as output_file:
        template_content = input_file.read()
        final_html = template_content.replace("<%table_place_holder%>", html)
        output_file.write(final_html)


def main():
    with open(r"D:\github\dataextractor\bond\2022\10\27.html", "r") as f:
        df_tables = pd.read_html(f)
        df = format_data(df_tables[0])
        df = df[["转债代码", "转债名称", "转债价格", "转股溢价率", "纯债价值", "剩余年限", "转债余额", "税前收益率", "新式排名"]]
        df = df.query("""转债价格 < 130 and not (转债名称.str.contains("\\*")) """).sort_values(by=['新式排名'], ascending=True)
        df.reset_index(drop=True, inplace=True)
        write_report(df)
        print(df)


if __name__ == "__main__":
    main()
