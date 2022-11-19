import pandas as pd
import re
from config import read_my_list, read_watch_list

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
            else:
                raise
    return x


def change_premium_rate(x):
    x = x.replace("%", "")
    return "{:.02f}".format(float(x))


def format_data(df):
    df = df.rename(columns=lambda s: s.replace(" ", ""))
    # process column
    df["剩余年限"] = df["剩余年限"].apply(change_remain_days)
    df["转债溢价率"] = df["转债价格"] - df["纯债价值"]
    df["转股溢价率"] = df["转股溢价率"].apply(change_premium_rate)
    df["辰星双低"] = df["转债溢价率"].astype(float) + df["转股溢价率"].astype(float)
    df["辰星三低"] = df["辰星双低"].astype(float) + df["转债余额"].astype(float)

    return df


def write_report(df_1, df_2, df_3, df_4):
    html_1 = df_1.to_html(classes='table table-stripped')
    html_2 = df_2.to_html(classes='table table-stripped')
    html_3 = df_3.to_html(classes='table table-stripped')
    html_4 = df_4.to_html(classes='table table-stripped')

    # write html to file
    with open("report.tpl", "r") as input_file, open("report.html", "w") as output_file:
        template_content = input_file.read()
        final_html = template_content.replace("<%table_place_holder_1%>", html_1)\
            .replace("<%table_place_holder_2%>", html_2)\
            .replace("<%table_place_holder_3%>", html_3)\
            .replace("<%table_place_holder_4%>", html_4)
        output_file.write(final_html)


def main():
    with open(r"D:\github\dataextractor\bond\2022\11\18.html", "r") as f:
        df_all = pd.read_html(f)
        df_all = format_data(df_all[0])
        df_all = df_all[["转债代码", "转债名称", "转债价格", "股价", "转股溢价率", "纯债价值", "转债溢价率", "剩余年限", "转债余额", "税前收益率", "辰星双低", "辰星三低"]]

        # 辰星双低
        df_1 = df_all.query(""" 股价 > 3 and 剩余年限 > "1.00" """)
        df_1 = df_1.query(""" 转债价格 < 125 and not (转债名称.str.contains("\\*")) """).sort_values(by=['辰星双低'], ascending=True).head(30)
        df_1.reset_index(drop=True, inplace=True)
        df_1.index = df_1.index + 1

        # 自选 (双低排序)
        df_2 = df_all[df_all["转债代码"].isin(read_my_list())]
        df_2 = df_2.sort_values(by=['辰星双低'], ascending=True)
        df_2.reset_index(drop=True, inplace=True)
        df_2.index = df_2.index + 1

        # 自选 (三低排序)
        df_4 = df_all[df_all["转债代码"].isin(read_my_list())]
        df_4 = df_4.sort_values(by=['辰星三低'], ascending=True)
        df_4.reset_index(drop=True, inplace=True)
        df_4.index = df_4.index + 1

        # 观察
        df_3 = df_all[df_all["转债代码"].isin(read_watch_list())]
        df_3 = df_3.query(""" 转债价格 < 130 """).sort_values(by=['辰星双低'], ascending=True)
        df_3.reset_index(drop=True, inplace=True)
        df_3.index = df_3.index + 1
        write_report(df_1, df_2, df_3, df_4)


if __name__ == "__main__":
    main()
