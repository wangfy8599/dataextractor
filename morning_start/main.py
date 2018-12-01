
import logging
from common import log_config
from . import morning_star, fund_filter

logger = logging.getLogger()


if __name__ == "__main__":
    try:
        log_config.init_logger()
        morning_star.download_data()
        fund_filter.do_filter()
    except Exception as ex:
        logger.exception(ex)

