import akshare as ak
import constant
import pandas as pd


def download_report():
    df = ak.stock_yjbb_em(date="20220930")
    df.to_csv(constant.stock_result_file, index=False, lineterminator='\n', encoding='utf_8_sig')


def generate_report():
    fund_result = pd.read_csv(constant.fund_result_file)
    stock_result = pd.read_csv(constant.stock_result_file)
    df = pd.merge(fund_result, stock_result, how='left', on='股票代码')
    df = df.rename(columns=lambda s: s.replace("-", "").replace("/", ""))
    df = df[
        ["转债代码", "转债名称", "转债价格", "股价", "转股溢价率", "转债溢价率", "剩余年限",
         "转债余额", "税前收益率", "PB", "辰星双低", "辰星三低", "营业收入同比增长", "营业收入季度环比增长"
            , "净利润同比增长", "净利润季度环比增长", "净资产收益率", "每股经营现金流量"]]
    # print(df.dtypes)
    df = df.query(""" 转债价格 < 125 and 股价 > 3 and 剩余年限 > 1.0 and PB > 1.0 and 营业收入同比增长>-30 and 净利润同比增长>-30 and 净资产收益率>6 and 每股经营现金流量>0 """)

    df = df.sort_values(by=['净资产收益率'], ascending=False).head(3000)
    df.reset_index(drop=True, inplace=True)
    df.index = df.index + 1

    df = df.sort_values(by=['净利润同比增长'], ascending=False).head(3000)
    df.reset_index(drop=True, inplace=True)
    df.index = df.index + 1
    write_report(df, ["table_place_holder_1", "table_place_holder_2"])


def write_report(df, place_holder_list):
    html_content = df.to_html(classes='table table-stripped')

    # write html to file
    with open(constant.template_file, "r") as input_file, open(constant.report_file, "w") as output_file:
        template_content = input_file.read()
        for place_holder in place_holder_list:
            template_content = template_content.replace("<%{}%>".format(place_holder), html_content)
        output_file.write(template_content)


if __name__ == "__main__":
    # download_report()
    generate_report()
