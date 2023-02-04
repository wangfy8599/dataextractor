import akshare as ak
from common.analysis_util import write_csv_file
from common import constants
from stock_helper import write_html_report, format_report

df = ak.stock_yjkb_em(date="20221231")

df = format_report(df)
df["每股现金流"] = df["每股净资产"].astype(float) * 0
df = df[
        ["股票代码", "股票简称", "每股收益", "营业收入", "营收同比", "营收环比", "净利润",
         "利润同比", "利润环比", "每股现金流", "ROE", "所处行业", "公告日期"]]

df_1 = df.query("营收同比 > 30 and 利润同比 > 30")

write_html_report([df_1, df], constants.yjkb_report_file)
write_csv_file(df, constants.yjkb_csv_file)
