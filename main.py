import random, time, os, schedule
os.environ['TZ'] = 'Asia/Singapore'

def job():
    exec(open('./run.py').read())

schedule.every().day.at("06:00").do(job)

print("Script Started")

while True:
    schedule.run_pending()
    time.sleep(10)
