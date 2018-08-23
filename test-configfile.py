import configparser
import requests
import json
import datetime

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

file = open("metrics.txt", "w")
file.write(r.text)
file.close()



