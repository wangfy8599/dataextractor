import akshare as ak
import pandas as pd
from stock_helper import write_html_report, format_report
from common import constants
from common.analysis_util import write_csv_file


def generate_report(report_days):
    df_arr = []
    for report_day in report_days:
        df_arr.append(ak.stock_yjbb_em(date=report_day))
    df = pd.concat(df_arr).drop_duplicates(["股票简称"], keep="last")
    df = format_report(df)
    df = df[
        ["股票代码", "股票简称", "每股收益", "营业收入", "营收同比", "营收环比", "净利润",
         "利润同比", "利润环比", "每股现金流", "ROE", "所处行业", "公告日期"]]
    df_arr[0] = df.query("营收同比 > 30 and 利润同比 > 30 and 净利润 > 1 and ROE > 9 and 每股现金流 > 0")
    df_arr[0].reset_index(drop=True, inplace=True)
    df_arr[0].index = df_arr[0].index + 1

    write_html_report([df_arr[0], df], constants.yjbg_report_file)
    write_csv_file(df, constants.yjbg_csv_file)
    files = [constants.yjbg_csv_1_file, constants.yjbg_csv_2_file, constants.yjbg_csv_3_file]
    for i in range(len(df_arr)):
        df_x = df_arr[i]
        rf = files[i]
        write_csv_file(df_x, rf)


if __name__ == "__main__":
    generate_report(["20230331"])
