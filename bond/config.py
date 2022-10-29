import pandas as pd

CONFIG_FILE = "./config.xml"


def read_my_list():
    df = pd.read_xml(CONFIG_FILE, xpath="/bonds/my_list/bond", encoding="utf-8")
    return df["code"].tolist()


def read_watch_list():
    df = pd.read_xml(CONFIG_FILE, xpath="/bonds/watch_list/bond", encoding="utf-8")
    return df["code"].tolist()


if __name__ == "__main__":
    read_my_list()
