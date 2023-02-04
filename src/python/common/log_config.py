import logging
import logging.config
import os


def init_logger():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_dir, "logs")
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    dict_conf = {
        'version': 1,
        'formatters': {
            'simple': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s %(levelname)-8s %(message)s'
            },
            'classic': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'simple',
            },
            'message_log': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(log_dir, 'message.log'),
                'level': 'INFO',
                'formatter': 'classic',
                'maxBytes': 10 * 1024 * 1024 * 1024,
                'backupCount': 6,
            },
            'trace_log': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(log_dir, 'trace.log'),
                'level': 'DEBUG',
                'formatter': 'classic',
                'maxBytes': 10 * 1024 * 1024 * 1024,
                'backupCount': 6,
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'message_log', 'trace_log']
        },
    }
    logging.config.dictConfig(dict_conf)
