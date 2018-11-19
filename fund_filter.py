#-*- coding=utf-8 -*-

import csv
import log_config
import logging
import morning_star
import os
import utils

logger = logging.getLogger()

watch_list = [
    "嘉实泰和混合",
    "嘉实研究精选",
    "嘉实增长混合",
    "嘉实服务",
    "嘉实优化红利",
    "华夏兴华混合",
    "华夏大盘精选",
    "华夏红利",
    "兴全社会责任混合",
    "兴全有机增长混合",
    "博时裕隆",
    "华宝多策略增长",
    "信诚盛世蓝筹",
    "富国天盛",
    "华商盛世成长",
]


def do_filter():
    result_dir = os.path.join(utils.script_dir(), "results")
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    in_path = os.path.join(result_dir, "morning_star.csv")
    out_path = os.path.join(result_dir, "morning_star_mine.csv")
    logger.info("writing fund to " + in_path)

    index = 0
    with open(in_path, "r", encoding='utf-8-sig') as in_file, open(out_path, "w", encoding='utf-8-sig') as out_file:
        for line in in_file:
            if index == 0:
                out_file.write(line)
            else:
                for key in watch_list:
                    if line.find(key) != -1:
                        out_file.write(line)
                        break
            index += 1


if __name__ == "__main__":
    try:
        log_config.init_logger()
        do_filter()
    except Exception as ex:
        logger.exception(ex)

