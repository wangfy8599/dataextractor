#-*- coding=utf-8 -*-

import log_config
import logging
import morning_star

logger = logging.getLogger()

watch_list = [
    "嘉实泰和混合",
    "嘉实研究精选",
    "嘉实增长",
    "嘉实服务",
    "嘉实优化红利股票",
    "华夏兴华混合",
    "华夏大盘精选",
    "华夏红利",
    "兴业社会责任",
    "兴业有机增长",
    "博时裕隆混合",
    "华宝多策略增长",
    "信诚盛世蓝筹",
    "富国天盛灵配混",
    "华商盛世成长",
]


def do_filter():
    pass


if __name__ == "__main__":
    try:
        log_config.init_logger()
        morning_star.download_data()
    except Exception as ex:
        logger.exception(ex)

