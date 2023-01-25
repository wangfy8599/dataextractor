import akshare as ak
import constant

stock_yjbb_em_df = ak.stock_yjbb_em(date="20220930")
with open(constant.stock_result_file, "w") as f:
    f.write(stock_yjbb_em_df.to_csv(lineterminator='\n'))
