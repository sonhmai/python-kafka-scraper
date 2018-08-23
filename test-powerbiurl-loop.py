import configparser
import requests
import json
import datetime
import time

# function to send real_time data to PowerBI
def send_powerbi(powerbi_url, metric, value):
    payload = {}
    payload['datetime'] = datetime.datetime.now().isoformat(timespec='seconds')
    payload['metrics'] = metric
    payload['value'] = value
    payload = [payload] #power BI API accepts list
    response = requests.post(powerbi_url, json=payload)
    return response


config = configparser.ConfigParser(interpolation=None)
# set interpolation to none to avoid interpreting % in URL as reference variable
# if not set, error will be raised due to %2 and %3D in POWERBI_URL

config.read('config.ini')
print('sections:', config.sections())

main_config = config['main']
for key in main_config:
    print(key, main_config.get(key))

kafka_jmx = main_config.get('kafka_jmx')
print(kafka_jmx)

r = requests.get(kafka_jmx)
print(r.status_code)

powerbi_url = main_config.get('powerbi_url')

# test send_powerbi() function: send 1 data points 5seconds apart to PowerBI
for i in range(1,11):
    r = send_powerbi(powerbi_url, metric='mem used', value=i)
    print(f'reponse of time {i}: {r.status_code}')
    time.sleep(1)

for i in range(11,1,-1):
    r = send_powerbi(powerbi_url, metric='mem used', value=i)
    print(f'reponse of time {i}: {r.status_code}')
    time.sleep(1)


