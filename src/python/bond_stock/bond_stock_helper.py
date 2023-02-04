from common import constants
import pandas as pd


def write_html_report(df_list, report_file):
    # round to two decimal places in python pandas
    pd.options.display.float_format = '{:.2f}'.format

    # write html to file
    with open(constants.bond_stock_template_file, "r") as input_file, open(report_file, "w") as output_file:
        template_content = input_file.read()
        index = 0
        for df in df_list:
            place_holder = "table_place_holder_{}".format(index)
            index += 1
            html_content = df.to_html(classes='table table-stripped')
            template_content = template_content.replace("<%{}%>".format(place_holder), html_content)
        output_file.write(template_content)
