from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import Client 

sched = BlockingScheduler()
account_sid = 'AC5e7d9b0bdf266ba786913630b8a0d8d4' 
auth_token = '201b9f8460882601cda85667d0427202'
client = Client(account_sid, auth_token) 

@sched.scheduled_job('cron', year=2021, month=9, day=12, hour=5, timezone='Asia/Kolkata')
def automate_message():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Good Morning Rohit, This alert message from Samol Automobile Bike Servicing. Kindly come and have your bike service by 12/09/21 for better performance.We are happy to serve you.',      
                                to='whatsapp:+918581803536' 
                            ) 
    
    print(message.sid)()

sched.start()


