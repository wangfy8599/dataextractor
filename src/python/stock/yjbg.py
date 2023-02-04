import akshare as ak
import pandas as pd
from stock_helper import write_html_report, format_report
from common import constants
from common.analysis_util import write_csv_file


if __name__ == "__main__":
    df_1 = ak.stock_yjbb_em(date="20220930")
    df_2 = ak.stock_yjbb_em(date="20221231")
    df = pd.concat([df_1, df_2]).drop_duplicates(["股票简称"], keep="last")
    df = format_report(df)
    df = df[
        ["股票代码", "股票简称", "每股收益", "营业收入", "营收同比", "营收环比", "净利润",
         "利润同比", "利润环比", "每股现金流", "ROE", "所处行业", "公告日期"]]
    df_1 = df.query("营收同比 > 30 and 利润同比 > 30 and 净利润 > 1 and ROE > 9 and 每股现金流 > 0")
    df_1.reset_index(drop=True, inplace=True)
    df_1.index = df_1.index + 1

    write_html_report([df_1, df], constants.yjbg_report_file)
    write_csv_file(df, constants.yjbg_csv_file)
    write_csv_file(df_1, constants.yjbg_csv_1_file)
    write_csv_file(df_2, constants.yjbg_csv_2_file)
