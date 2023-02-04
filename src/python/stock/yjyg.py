import akshare as ak
from stock_helper import format_report
from common.analysis_util import write_csv_file
from common import constants
import pandas as pd


def generate_raw_report():
    df = ak.stock_yjyg_em(date="20221231")
    df = format_report(df)
    write_csv_file(df, constants.yjyg_raw_csv_file)


def generate_report():
    df = pd.read_csv(constants.yjyg_raw_csv_file)
    df = df.query(""" 预测指标 == '归属于上市公司股东的净利润' """)
    write_csv_file(df, constants.yjyg_csv_file)


if __name__ == "__main__":
    generate_raw_report()
    generate_report()
