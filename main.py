import random, time, os, schedule

def job():
    exec(open('./run.py').read())

schedule.every().day.at("21.00").do(job)

print("Script Started")

while True:
    schedule.run_pending()
    time.sleep(10)
