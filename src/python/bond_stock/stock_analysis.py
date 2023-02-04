from bond import config
from common import constants
import pandas as pd
from bond_stock_helper import write_stock_report


def generate_report():
    fund_result = pd.read_csv(constants.bond_csv_file)
    stock_result = pd.read_csv(constants.yjbg_csv_file)
    df_all = pd.merge(fund_result, stock_result, how='left', on='股票代码')
    df_all = df_all.rename(columns=lambda s: s.replace("-", "").replace("/", ""))
    df_all = df_all.rename(columns=lambda s: s.replace("营业收入同比增长", "营收同比").replace("营业收入季度环比增长", "营收环比"))
    df_all = df_all.rename(columns=lambda s: s.replace("净利润同比增长", "利润同比").replace("净利润季度环比增长", "利润环比"))
    df_all = df_all.rename(columns=lambda s: s.replace("净资产收益率", "ROE").replace("每股经营现金流量", "每股现金流"))
    df_all = df_all[
        ["转债代码", "转债名称", "转债价格", "股价", "转股溢价率", "转债溢价率", "剩余年限",
         "转债余额", "税前收益率", "PB", "辰星双低", "辰星三低", "营收同比", "营收环比"
            , "利润同比", "利润环比", "ROE", "每股现金流"]]

    df_0 = df_all[df_all["转债代码"].isin(config.read_high_weightage_list())]
    df_0 = df_0.query(""" 转债价格 < 125 and 股价 > 3 and 剩余年限 > 1.0 and PB > 1.0 and 营收同比>0 and 利润同比>0 and ROE>5 and 每股现金流>0 """)
    df_0 = df_0.sort_values(by=['辰星双低'], ascending=True)
    df_0.reset_index(drop=True, inplace=True)
    df_0.index = df_0.index + 1

    df_1 = df_all[df_all["转债代码"].isin(config.read_all_watch_list())]
    df_1 = df_1.sort_values(by=['ROE'], ascending=False)
    df_1.reset_index(drop=True, inplace=True)
    df_1.index = df_1.index + 1

    df_2 = df_all[df_all["转债代码"].isin(config.read_all_watch_list())]
    df_2 = df_2.sort_values(by=['利润同比'], ascending=False)
    df_2.reset_index(drop=True, inplace=True)
    df_2.index = df_2.index + 1

    df_3 = df_all[df_all["转债代码"].isin(config.read_all_watch_list())]
    df_3 = df_3.sort_values(by=['辰星双低'], ascending=True)
    df_3.reset_index(drop=True, inplace=True)
    df_3.index = df_3.index + 1

    df_4 = df_all.query(""" 转债价格 < 130 and 股价 > 3 and 剩余年限 > 1.0 and PB > 1.0 and 营收同比>0 and 利润同比>10 and ROE>9 and 每股现金流>0 """)
    df_4 = df_4.sort_values(by=['ROE'], ascending=False).head(3000)
    df_4.reset_index(drop=True, inplace=True)
    df_4.index = df_4.index + 1

    df_5 = df_all.query(""" 转债价格 < 130 and 股价 > 3 and 剩余年限 > 1.0 and PB > 1.0 and 营收同比>0 and 利润同比>10 and ROE>9 and 每股现金流>0 """)
    df_5 = df_5.sort_values(by=['利润同比'], ascending=False).head(3000)
    df_5.reset_index(drop=True, inplace=True)
    df_5.index = df_5.index + 1

    df_6 = df_all.query(""" 转债价格 < 130 and 股价 > 3 and 剩余年限 > 1.0 and PB > 1.0 and 营收同比>0 and 利润同比>10 and ROE>9 and 每股现金流>0 """)
    df_6 = df_6.sort_values(by=['辰星双低'], ascending=True).head(3000)
    df_6.reset_index(drop=True, inplace=True)
    df_6.index = df_6.index + 1

    df_7 = df_all.query(""" 转债价格 < 125 and 股价 > 3 and 剩余年限 > 1.0 and PB > 1.0 and 营收同比>0 and 利润同比>10 and ROE>9 """)
    df_7 = df_7.sort_values(by=['辰星三低'], ascending=True).head(3000)
    df_7.reset_index(drop=True, inplace=True)
    df_7.index = df_7.index + 1

    write_stock_report([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7], constants.bond_stock_report_file)


if __name__ == "__main__":
    generate_report()
