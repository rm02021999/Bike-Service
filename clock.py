from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from message import automate_message

sched = BlockingScheduler()

sched.add_job(automate_message, 'date', run_date='2021-09-10 10:00:00') 

sched.start()