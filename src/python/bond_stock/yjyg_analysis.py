from bond import config
from common import constants
import pandas as pd
from bond_stock_helper import write_stock_2_report


def generate_report():
    fund_result = pd.read_csv(constants.bond_csv_file)
    stock_result = pd.read_csv(constants.yjyg_csv_file)
    df_all = pd.merge(fund_result, stock_result, how='left', on='股票代码')
    df_all = df_all[
        ["转债代码", "转债名称", "转债价格", "股价", "转股溢价率", "转债溢价率", "剩余年限",
         "转债余额", "税前收益率", "PB", "辰星双低", "辰星三低", "业绩变动幅度", "公告日期"]]

    df_0 = df_all[df_all["转债代码"].isin(config.read_high_weightage_list())]
    df_0 = df_0.query(""" 转债价格 < 130 and 业绩变动幅度>-1000 """)
    df_0 = df_0.sort_values(by=['辰星双低'], ascending=True)
    df_0.reset_index(drop=True, inplace=True)
    df_0.index = df_0.index + 1

    df_1 = df_all[df_all["转债代码"].isin(config.read_my_list())]
    df_1 = df_1.query(""" 转债价格 < 150 and 业绩变动幅度>-1000 """)
    df_1 = df_1.sort_values(by=['业绩变动幅度'], ascending=False)
    df_1.reset_index(drop=True, inplace=True)
    df_1.index = df_1.index + 1

    df_2 = df_all[df_all["转债代码"].isin(config.read_watch_list())]
    df_2 = df_2.query(""" 转债价格 < 1000 and 业绩变动幅度>-1000 """)
    df_2 = df_2.sort_values(by=['业绩变动幅度'], ascending=False)
    df_2.reset_index(drop=True, inplace=True)
    df_2.index = df_2.index + 1

    df_3 = df_all.query(""" 转债价格 < 125 and 业绩变动幅度>0 """)
    df_3 = df_3.sort_values(by=['业绩变动幅度'], ascending=False)
    df_3.reset_index(drop=True, inplace=True)
    df_3.index = df_3.index + 1

    write_stock_2_report([df_0, df_1, df_2, df_3], constants.bond_yjyg_report_file)


if __name__ == "__main__":
    generate_report()
