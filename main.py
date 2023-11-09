import subprocess
from time import sleep


timeout = 1  # update time (seconds)

while True:
    command = 'scrapy crawl bybit -O output.csv'
    subprocess.run(command, shell=True)
    sleep(timeout)
