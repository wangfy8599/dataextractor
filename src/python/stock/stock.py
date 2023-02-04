from common import constants
import pandas as pd
from stock_helper import write_html_report
from common.analysis_util import write_csv_file


def generate_report():
    df_yjbg = pd.read_csv(constants.yjbg_csv_file)
    df_yjkb = pd.read_csv(constants.yjkb_csv_file)
    df = pd.concat([df_yjbg, df_yjkb]).drop_duplicates(["股票简称"], keep="last")

    df_1 = df.query("营收同比 > 30 and 利润同比 > 30 and 净利润 > 1 and ROE > 9 and 每股现金流 > 0")
    df_1.reset_index(drop=True, inplace=True)
    df_1.index = df_1.index + 1

    write_html_report([df_1, df], constants.stock_report_file)
    write_csv_file(df, constants.stock_csv_file)


if __name__ == "__main__":
    generate_report()
