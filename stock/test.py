import akshare as ak

stock_yjbb_em_df = ak.stock_yjbb_em(date="20220930")
with open("report.csv", "w") as f:
    f.write(stock_yjbb_em_df.to_csv())
with open("report.html", "w") as f:
    f.write(stock_yjbb_em_df.to_html())

