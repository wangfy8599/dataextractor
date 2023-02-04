
import logging
from src.python.common import log_config
from src.python.morning_start import morning_star, fund_stat

logger = logging.getLogger()


if __name__ == "__main__":
    try:
        log_config.init_logger()
        morning_star.download_data()
        fund_stat.do_clean()
        fund_stat.do_sort()
        fund_stat.do_filter()
    except Exception as ex:
        logger.exception("Unknown Exception in main:")

