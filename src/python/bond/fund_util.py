import re
from common import constants

pattern_year_day = re.compile("([\\d\\.]+)year([\\d\\.]+)day")
pattern_year = re.compile("([\\d\\.]+)year")
pattern_day = re.compile("([\\d\\.]+)day")


def change_remain_days(x):
    x = x.replace("年", "year").replace("天", "day")
    m = pattern_year_day.match(x)
    if m:
        year = float(m.group(1))
        day = float(m.group(2))
        x = "{:.02f}".format(year + day/366)
    else:
        m = pattern_year.match(x)
        if m:
            year = float(m.group(1))
            x = "{:.02f}".format(year)
        else:
            m = pattern_day.match(x)
            if m:
                day = float(m.group(1))
                x = "{:.02f}".format(day/366)
            else:
                print(x)
                raise
    return x


def change_premium_rate(x):
    x = x.replace("%", "")
    return float(x)


def change_interest_rate(x):
    x = x.replace("%", "").replace("<", "")
    return float(x)


def format_data(df):
    df = df.rename(columns=lambda s: s.replace(" ", "").replace("/", ""))
    # process column
    df["剩余年限"] = df["剩余年限"].apply(change_remain_days)
    df["转债溢价率"] = (df["转债价格"] - df["纯债价值"]).astype(float) / df["纯债价值"] * 100
    df["转股溢价率"] = df["转股溢价率"].apply(change_premium_rate)
    df["税前收益率"] = df["税前收益率"].apply(change_interest_rate)
    df["辰星双低"] = df["转债溢价率"].astype(float) + df["转股溢价率"].astype(float)
    df["辰星三低"] = df["辰星双低"].astype(float) + df["转债余额"].astype(float) * 5
    df["辰星四低"] = df["辰星三低"].astype(float) - df["税前收益率"].astype(float) * 100
    df['股票代码'] = df['股票代码'].astype(str).str.zfill(6)
    df.loc[(df['股价'] < 3) | (df['转债名称'] == "正邦转债") | (df['转债名称'].str.contains("长证转债")), '转债名称'] = df['转债名称'] + constants.risk_place_holder
    df.loc[(df['剩余年限'].astype(float) < 1), '转债名称'] = df['转债名称'] + constants.short_time_place_holder

    return df

