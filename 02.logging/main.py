import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

x = 4
y = 0

logging.info(f"The values of x and y are {x} and {y}.")
try:
    x/y
    logging.info(f"x/y successful with result: {x/y}.")
except:
    logging.error("ZeroDivisionError",exc_info=True)


# Multiple Loggers
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s {%(lineno)d}")
def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file, mode="w")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def close_logger(name):
    logger = logging.getLogger(name)
    for handler in logger.handlers:
        logger.removeHandler(handler)
        handler.close()