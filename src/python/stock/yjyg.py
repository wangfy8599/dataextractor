import akshare as ak
from stock_helper import format_report
from common.analysis_util import write_csv_file
from common import constants

df = ak.stock_yjyg_em(date="20221231")

df = format_report(df)

write_csv_file(df, constants.yjyg_csv_file)
