import pandas as pd
from common.constants import bond_config_file


def read_all_watch_list():
    df_mine = pd.read_xml(bond_config_file, xpath="/bonds/my_list/bond", encoding="utf-8")
    df_watch = pd.read_xml(bond_config_file, xpath="/bonds/watch_list/bond", encoding="utf-8")
    df = pd.concat([df_mine, df_watch])
    return df["code"].tolist()


def read_high_weightage_list():
    df_mine = pd.read_xml(bond_config_file, xpath="/bonds/my_list/bond", encoding="utf-8")
    df_watch = pd.read_xml(bond_config_file, xpath="/bonds/watch_list/bond", encoding="utf-8")
    df_mine = df_mine.query("weightage > 0")
    df_watch = df_watch.query("weightage > 0")
    df = pd.concat([df_mine, df_watch])
    return df["code"].tolist()


def read_my_list():
    df = pd.read_xml(bond_config_file, xpath="/bonds/my_list/bond", encoding="utf-8")
    return df["code"].tolist()


def read_watch_list():
    df = pd.read_xml(bond_config_file, xpath="/bonds/watch_list/bond", encoding="utf-8")
    return df["code"].tolist()


if __name__ == "__main__":
    read_my_list()
