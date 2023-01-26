import re

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
                raise
    return x


def change_premium_rate(x):
    x = x.replace("%", "")
    return "{:.02f}".format(float(x))


def format_data(df):
    df = df.rename(columns=lambda s: s.replace(" ", "").replace("/", ""))
    # process column
    df["剩余年限"] = df["剩余年限"].apply(change_remain_days)
    df["转债溢价率"] = df["转债价格"] - df["纯债价值"]
    df["转股溢价率"] = df["转股溢价率"].apply(change_premium_rate)
    df["辰星双低"] = df["转债溢价率"].astype(float) + df["转股溢价率"].astype(float)
    df["辰星三低"] = df["辰星双低"].astype(float) + df["转债余额"].astype(float) * 3
    df['股票代码'] = df['股票代码'].str.zfill(6)

    return df

