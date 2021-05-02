import random
import time

randomSleep = random.randint(5,15)

print("Sleeping for: %ds" % randomSleep)

time.sleep(randomSleep)

exec(open('./genshin-os.py').read())
