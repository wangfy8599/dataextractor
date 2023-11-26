import pandas as pd

import fund_util
from common import constants
from bond.config import read_my_list, read_watch_list, read_high_weightage_list, read_exclude_list
from common.constants import risk_place_holder, short_time_place_holder, short_time_html, risk_html
from common.analysis_util import write_csv_file


def write_report(df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11):
    html_0 = df_0.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_1 = df_1.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_2 = df_2.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_3 = df_3.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_4 = df_4.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_5 = df_5.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_6 = df_6.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_7 = df_7.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_8 = df_8.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_9 = df_9.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_10 = df_10.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)
    html_11 = df_11.to_html(classes='table table-stripped').replace(risk_place_holder, risk_html).replace(short_time_place_holder, short_time_html)

    # write html to file
    with open(constants.bond_template_file, "r") as input_file, open(constants.bond_report_file, "w") as output_file:
        template_content = input_file.read()
        final_html = template_content.replace("<%table_place_holder_0%>", html_0) \
            .replace("<%table_place_holder_1%>", html_1) \
            .replace("<%table_place_holder_2%>", html_2) \
            .replace("<%table_place_holder_3%>", html_3) \
            .replace("<%table_place_holder_4%>", html_4) \
            .replace("<%table_place_holder_5%>", html_5) \
            .replace("<%table_place_holder_6%>", html_6) \
            .replace("<%table_place_holder_7%>", html_7) \
            .replace("<%table_place_holder_8%>", html_8) \
            .replace("<%table_place_holder_9%>", html_9) \
            .replace("<%table_place_holder_10%>", html_10) \
            .replace("<%table_place_holder_11%>", html_11)
        output_file.write(final_html)


def highlight_risk(s):
    return ['background-color: blue']


def main():
    # round to two decimal places in python pandas
    pd.options.display.float_format = '{:.2f}'.format

    with open(constants.bond_input_file, "r", encoding="utf-8") as f:
        df_all = pd.read_html(f)
        df_all = fund_util.format_data(df_all[0])
        df_all = df_all[
            ["转债代码", "转债名称", "转债价格", "股票代码", "股价", "转股溢价率", "纯债价值", "转债溢价率", "剩余年限",
             "转债余额", "税前收益率", "PB", "辰星双低", "辰星三低", "辰星四低"]]

        write_csv_file(df_all, constants.bond_csv_file)

        # 自选 (低溢价)
        df_0 = df_all[df_all["转债代码"].isin(read_high_weightage_list())]
        df_0 = df_0.query(""" 转债价格 <= 125 """)
        df_0 = df_0.sort_values(by=['转股溢价率'], ascending=True)
        df_0.reset_index(drop=True, inplace=True)
        df_0.index = df_0.index + 1

        # 辰星双低
        df_1 = df_all[~df_all["转债代码"].isin(read_exclude_list())]
        df_1 = df_1.query(""" 股价 > 3 and 剩余年限 > "1.00" and PB > 1.05 """)
        df_1 = df_1.query(""" 转债价格 < 125 and not (转债名称.str.contains("\\*")) """).sort_values(by=['辰星双低'], ascending=True).head(30)
        df_1.reset_index(drop=True, inplace=True)
        df_1.index = df_1.index + 1

        # 自选 (双低排序)
        df_2 = df_all[df_all["转债代码"].isin(read_my_list())]
        df_2 = df_2.sort_values(by=['辰星双低'], ascending=True)
        df_2.reset_index(drop=True, inplace=True)
        df_2.index = df_2.index + 1

        # 观察
        df_3 = df_all[df_all["转债代码"].isin(read_watch_list())]
        df_3 = df_3.query(""" 转债价格 < 130 """).sort_values(by=['辰星双低'], ascending=True)
        df_3.reset_index(drop=True, inplace=True)
        df_3.index = df_3.index + 1

        # 自选 (三低排序)
        df_4 = df_all[df_all["转债代码"].isin(read_my_list())]
        df_4 = df_4.sort_values(by=['辰星三低'], ascending=True)
        df_4.reset_index(drop=True, inplace=True)
        df_4.index = df_4.index + 1

        # 观察
        df_5 = df_all[df_all["转债代码"].isin(read_watch_list())]
        df_5 = df_5.query(""" 转债价格 < 130 """).sort_values(by=['辰星三低'], ascending=True)
        df_5.reset_index(drop=True, inplace=True)
        df_5.index = df_5.index + 1

        # 辰星三低
        df_6 = df_all.query(""" 股价 > 3 and 剩余年限 > "1.00" and  PB > 0.3 """)
        df_6 = df_6.query(""" 转债价格 < 125 and not (转债名称.str.contains("\\*")) """).sort_values(by=['辰星三低'],
                                                                                                     ascending=True).head(
            30)
        df_6.reset_index(drop=True, inplace=True)
        df_6.index = df_6.index + 1

        # 税前收益率
        df_7 = df_all.query(""" 股价 > 3 and 剩余年限 > "1.00" and  PB > 0.3 """)
        df_7 = df_7.query(""" 转债价格 < 125 and not (转债名称.str.contains("\\*")) """).sort_values(by=['税前收益率'],
                                                                                                     ascending=False).head(
            30)
        df_7.reset_index(drop=True, inplace=True)
        df_7.index = df_7.index + 1

        # 重仓四低
        df_8 = df_all[df_all["转债代码"].isin(read_high_weightage_list())]
        df_8 = df_8.query(""" 股价 > 3 and 剩余年限 > "1.00" and  PB > 1 """)
        df_8 = df_8.query(""" 转债价格 < 127 and not (转债名称.str.contains("\\*")) """).sort_values(by=['辰星四低'], ascending=True).head(50)
        df_8.reset_index(drop=True, inplace=True)
        df_8.index = df_8.index + 1

        # 转债余额
        df_9 = df_all.query(""" 股价 > 3 and 剩余年限 > "1.00" and  PB > 0.3 """)
        df_9 = df_9.query(""" 转债价格 < 125 and not (转债名称.str.contains("\\*")) """).sort_values(by=['转债余额'],
                                                                                                     ascending=True).head(
            30)
        df_9.reset_index(drop=True, inplace=True)
        df_9.index = df_9.index + 1

        # 自选 (剩余年限)
        df_10 = df_all[df_all["转债代码"].isin(read_my_list())]
        df_10 = df_10.sort_values(by=['剩余年限'], ascending=True)
        df_10.reset_index(drop=True, inplace=True)
        df_10.index = df_10.index + 1

        # 自选 (剩余年限)
        df_11 = df_all[df_all["转债代码"].isin(read_my_list())]
        df_11 = df_11.query(""" 转债余额 < 6 and 税前收益率 > 0 """)
        df_11 = df_11.sort_values(by=['转债余额'], ascending=True)
        df_11.reset_index(drop=True, inplace=True)
        df_11.index = df_11.index + 1

        #
        write_report(df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11)


if __name__ == "__main__":
    main()
