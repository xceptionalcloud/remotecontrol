from lxml import etree
import requests
import time
from netmiko import ConnectHandler
import configparser

site = '8701'

config = configparser.RawConfigParser()
config.read('settings.ini')
iosUser = config['ROUTER']['user']
iosPass = config['ROUTER']['pass']
iosHost = config['ROUTER'][site]

device = {
    'device_type': 'cisco_ios',
    'host': iosHost,
    'username': iosUser,
    'password': iosPass
}

phoneDb = []
dnDb = []
telephonyDb = []

print("Starting Router connection test")

net_connect = ConnectHandler(**device)
#output = net_connect.send_command('config terminal', expect_string='#')
output = net_connect.send_command('show run')
#print(output)
for thisLine in output:

'''
print("Starting PhoneRemote test")

_88xx_keynavlist = ['Dial:90016194194600']
#_88xx_keynavlist = ['Key:KeyPad1', 'Key:KeyPad2', 'Key:KeyPad0', 'Key:KeyPad3', 'Key:KeyPadPound']
#_88xx_keynavlist = ['Key:KeyPad9', 'Key:KeyPad3', 'Key:KeyPad4', 'Key:KeyPad1', 'Key:KeyPadPound']
_88xx_keynavlist = ['Key:Soft2']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPad6','Key:KeyPad4','Key:KeyPad1','Key:Soft3']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPadStar','Key:KeyPadStar','Key:KeyPadPound','Key:KeyPadStar','Key:KeyPadStar']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPad5','Key:KeyPad4','Key:KeyPad4','Key:Soft3']
key = 'XML'
keynav = {key : []}
url = 'http://10.87.102.41/CGI/Execute'
user='variphy'
pwd='variphy'
headers={'content-type':'application/xml'}

for keypress in _88xx_keynavlist:
    ph_nav = etree.Element('CiscoIPPhoneExecute')
    exeit_e = etree.SubElement(ph_nav, 'ExecuteItem')
    exeit_e.set('Priority','0')
    exeit_e.set('URL',keypress)
    phnavstr = etree.tostring(ph_nav,pretty_print=True)
    keynav[key] = keynav[key]+[phnavstr]

for xml in keynav[key]:
    key_press = {}
    key_press[key] = xml
    print("This key press - " + str(key_press))
    r = requests.post(url,headers=headers,data=key_press,auth=(user,pwd))
    time.sleep(1.0)
    print("Response code from phone - " + str(r))
    print("Response content from phone - " + str(r.content))

print("All Done!!")
'''