import random, time, os, schedule
os.environ['TZ'] = 'Asia/China'

def job():
    randomSleep = random.randint(10,300)
    print("Sleeping for: %ds" % randomSleep)
    time.sleep(randomSleep)
    exec(open('./run.py').read())

schedule.every().day.at("06:00").do(job)

print("Script Started")

while True:
    schedule.run_pending()
    time.sleep(10)
