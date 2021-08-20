from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from message import automate_message

sched = BlockingScheduler()

sched.add_job(automate_message, 'cron', year=2021, month=9, day=12, hour=10, timezone='Asia/Kolkata') 

sched.start()