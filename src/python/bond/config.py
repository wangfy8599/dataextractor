import pandas as pd

CONFIG_FILE = "config.xml"


def read_all_watch_list():
    df_mine = pd.read_xml(CONFIG_FILE, xpath="/bonds/my_list/bond", encoding="utf-8")
    df_watch = pd.read_xml(CONFIG_FILE, xpath="/bonds/watch_list/bond", encoding="utf-8")
    df = pd.concat([df_mine, df_watch])
    return df["code"].tolist()


def read_high_weightage_list():
    df_mine = pd.read_xml(CONFIG_FILE, xpath="/bonds/my_list/bond", encoding="utf-8")
    df_watch = pd.read_xml(CONFIG_FILE, xpath="/bonds/watch_list/bond", encoding="utf-8")
    df_mine = df_mine.query("weightage > 0")
    df_watch = df_watch.query("weightage > 0")
    df = pd.concat([df_mine, df_watch])
    return df["code"].tolist()


def read_my_list():
    df = pd.read_xml(CONFIG_FILE, xpath="/bonds/my_list/bond", encoding="utf-8")
    return df["code"].tolist()


def read_watch_list():
    df = pd.read_xml(CONFIG_FILE, xpath="/bonds/watch_list/bond", encoding="utf-8")
    return df["code"].tolist()


if __name__ == "__main__":
    read_my_list()
