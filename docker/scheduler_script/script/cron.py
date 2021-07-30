from loguru import logger as LOGGER
from crontab import CronTab
import os

LOGGER.info("STARTING CRONJOB ...")
mem_cron = CronTab(user='root', tab="""%s python3 main.py""" % os.environ.get('CRON_SCHEDULE'))
for result in mem_cron.run_scheduler():
    LOGGER.info("This was printed to stdout by the process.")
