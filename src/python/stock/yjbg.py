import akshare as ak
from stock_helper import write_html_report, format_report
from common import constants
from common.analysis_util import write_csv_file


if __name__ == "__main__":
    df = ak.stock_yjbb_em(date="20220930")
    df = format_report(df)

    df_1 = df.query("营收同比 > 30 and 利润同比 > 30")
    write_html_report([df_1, df], constants.yjbg_report_file)
    write_csv_file(df, constants.yjbg_csv_file)
