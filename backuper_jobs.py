from methods import *
import schedule as sch
from backuper_server import app
import time

with app.app_context():
    sch.every(1).day.at("01:00").do(lambda: make_backup(modes=['daily']))
    sch.every(1).sunday.at("01:00").do(lambda: make_backup(modes=['weekly']))
    sch.every(1).day.at("01:00").do(lambda: delete_backup())

    while True:
        sch.run_pending()
        time.sleep(60)

