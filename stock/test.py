import akshare as ak
import pandas as pd


def format_report(df):
    df = df.rename(columns=lambda s: s.replace("-", "").replace("/", ""))
    df = df.rename(columns=lambda s: s.replace("营业收入营业收入", "营业收入").replace("净利润净利润", "净利润"))
    df = df.rename(columns=lambda s: s.replace("营业收入同比增长", "营收同比").replace("营业收入季度环比增长", "营收环比"))
    df = df.rename(columns=lambda s: s.replace("净利润同比增长", "利润同比").replace("净利润季度环比增长", "利润环比"))
    df = df.rename(columns=lambda s: s.replace("净资产收益率", "ROE"))
    df = df.rename(columns=lambda s: s.replace("每股经营现金流量", "每股现金流"))
    df = df.rename(columns=lambda s: s.replace("最新公告日期", "公告日期"))
    df["营业收入"] = df["营业收入"].astype(float) / 100000000
    df["净利润"] = df["净利润"].astype(float) / 100000000
    df = df[
        ["股票代码", "股票简称", "每股收益", "营业收入", "营收同比", "营收环比", "净利润",
         "利润同比", "利润环比", "每股净资产", "ROE", "所处行业", "公告日期"]]
    df = df.sort_values(by=['利润同比'], ascending=False)
    return df


def format_forecast_report(df):
    df = df.rename(columns=lambda s: s.replace("-", "").replace("/", ""))
    df = df.rename(columns=lambda s: s.replace("营业收入营业收入", "营业收入").replace("净利润净利润", "净利润"))
    df = df.rename(columns=lambda s: s.replace("营业收入同比增长", "营收同比").replace("营业收入季度环比增长", "营收环比"))
    df = df.rename(columns=lambda s: s.replace("净利润同比增长", "利润同比").replace("净利润季度环比增长", "利润环比"))
    df = df.rename(columns=lambda s: s.replace("净资产收益率", "ROE"))
    df["营业收入"] = df["营业收入"].astype(float) / 100000000
    df["净利润"] = df["净利润"].astype(float) / 100000000
    df = df[
        ["股票代码", "股票简称", "每股收益", "营业收入", "营收同比", "营收环比", "净利润",
         "利润同比", "利润环比", "每股净资产", "ROE", "所处行业", "公告日期"]]
    df = df.sort_values(by=['利润同比'], ascending=False)
    return df


def write_report(df_list, report_file):
    # write html to file
    with open("report.tpl", "r") as input_file, open(report_file, "w") as output_file:
        template_content = input_file.read()
        index = 0
        for df in df_list:
            place_holder = "table_place_holder_{}".format(index)
            index += 1
            html_content = df.to_html(classes='table table-stripped')
            template_content = template_content.replace("<%{}%>".format(place_holder), html_content)
        output_file.write(template_content)


if __name__ == "__main__":

    # round to two decimal places in python pandas
    pd.options.display.float_format = '{:.2f}'.format

    stock_yjbb_em_df = ak.stock_yjbb_em(date="20221231")
    with open("report.csv", "w") as f:
        stock_yjbb_em_df = format_report(stock_yjbb_em_df)
        f.write(stock_yjbb_em_df.to_csv())

    write_report([stock_yjbb_em_df], "report.html")

    stock_yjkb_em_df = ak.stock_yjkb_em(date="20221231")
    with open("forecast_report.csv", "w") as f:
        stock_yjkb_em_df = format_forecast_report(stock_yjkb_em_df)
        f.write(stock_yjkb_em_df.to_csv())

    write_report([stock_yjkb_em_df], "forecast_report.html")

