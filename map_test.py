import log_config
import logging

logger = logging.getLogger()
log_config.init_logger()
lst = [1, 2, 3]

lst2 = map(lambda x: "{}a".format(x), lst)

logger.info(list(lst2))
