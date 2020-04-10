from netmiko import ConnectHandler
import configparser
import time

site = '6305'

config = configparser.RawConfigParser()
config.read('settings.ini')
iosUser = config['ROUTER']['user']
iosPass = config['ROUTER']['pass']
iosHost = config['ROUTER'][site]

device = {
    'device_type': 'cisco_ios',
    'host': iosHost,
    'username': iosUser,
    'password': iosPass,
    'global_delay_factor': 10
}
print("Starting Router connection test")

net_connect = ConnectHandler(**device)
net_connect.write_channel('show run\n')
time.sleep(5)
showRun = net_connect.read_channel()
#print(showRun)
for entry in showRun.split('\n'):
    print(entry)
net_connect.disconnect()
print("ALL DONE")
