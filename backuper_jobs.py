# -*- coding: utf-8 -*-
from models import *
from backuper_server import app
from methods import *
from tools import *
from config import *


# sch.every(1).minute.do(data2)
# while True:
#     sch.run_pending()
with app.app_context():
    make_backup(modes=['daily', 'weekly'])
