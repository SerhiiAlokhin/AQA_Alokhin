import time
import logging
from datetime import datetime, timedelta


Key1 = 'TSTFEED0300|7E3E|0400'

logging.basicConfig(
    filename='HB_test.log',
    level= logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

def time_track(time_str):
    format_string = '%H:%M:%S'
    previous_time = datetime.strptime(time_str[0],format_string)
    for heartbeat in time_str:
        time_obj = datetime.strptime(heartbeat, format_string)


        if timedelta(seconds=31) < (previous_time - time_obj) < timedelta(seconds=33):
            logging.warning(f'WARNING: heartbeat = {(previous_time - time_obj)} сек.')
        elif (previous_time - time_obj) >= timedelta(seconds=33):
            logging.error(f'ERROR: heartbeat = {(previous_time - time_obj)} сек.')
        previous_time = time_obj


with open('hblog.txt', 'r') as file1:
    data = file1
    time_time = []
    for i in data:
        if Key1 in i:
            time_time.append(i[53:61])
time_track(time_time)

print(time_time)

