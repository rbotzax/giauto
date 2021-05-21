import random
import time

randomSleep = random.randint(10,300)

print("Sleeping for: %ds" % randomSleep)

time.sleep(randomSleep)

exec(open('./genshin-os.py').read())
