import akshare as ak
from stock_helper import write_html_report
from common import constants
from common.analysis_util import write_csv_file

"""
股东增减持
"""
stock_ggcg_em_df = ak.stock_ggcg_em(symbol="全部")
write_csv_file(stock_ggcg_em_df, constants.ggzjc_csv_file)
