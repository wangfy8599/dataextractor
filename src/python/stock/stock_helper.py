from common import constants
import pandas as pd


def format_report(df):
    df = df.rename(columns=lambda s: s.replace("-", "").replace("/", ""))
    df = df.rename(columns=lambda s: s.replace("营业收入营业收入", "营业收入").replace("净利润净利润", "净利润"))
    df = df.rename(columns=lambda s: s.replace("营业收入同比增长", "营收同比").replace("营业收入季度环比增长", "营收环比"))
    df = df.rename(columns=lambda s: s.replace("净利润同比增长", "利润同比").replace("净利润季度环比增长", "利润环比"))
    df = df.rename(columns=lambda s: s.replace("净资产收益率", "ROE"))
    df = df.rename(columns=lambda s: s.replace("每股经营现金流量", "每股现金流"))
    df = df.rename(columns=lambda s: s.replace("最新公告日期", "公告日期"))
    if "营业收入" in df:
        df["营业收入"] = df["营业收入"].astype(float) / 100000000
        df["净利润"] = df["净利润"].astype(float) / 100000000
        df = df.sort_values(by=['利润同比'], ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index = df.index + 1
    return df


def write_html_report(df_list, report_file):
    # round to two decimal places in python pandas
    pd.options.display.float_format = '{:.2f}'.format

    # write html to file
    with open(constants.stock_template_file, "r", encoding="utf-8") as input_file, open(report_file, "w", encoding="utf-8") as output_file:
        template_content = input_file.read()
        index = 0
        for df in df_list:
            place_holder = "table_place_holder_{}".format(index)
            index += 1
            html_content = df.to_html(classes='table table-stripped')
            template_content = template_content.replace("<%{}%>".format(place_holder), html_content)
        output_file.write(template_content)
