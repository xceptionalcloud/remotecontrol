from lxml import etree
import requests
import time
import configparser

site = '6305'

config = configparser.RawConfigParser()
config.read('settings.ini')
iosUser = config['ROUTER']['user']
iosPass = config['ROUTER']['pass']
iosHost = config['ROUTER'][site]
phoneUser = config['IPPHONE']['user']
phonePass = config['IPPHONE']['pass']

device = {
    'device_type': 'cisco_ios',
    'host': iosHost,
    'username': iosUser,
    'password': iosPass
}

print("Starting PhoneRemote test")

#_88xx_keynavlist = ['Dial:923215000']
#_88xx_keynavlist = ['Key:KeyPad1', 'Key:KeyPad2', 'Key:KeyPad0', 'Key:KeyPad3', 'Key:KeyPadPound']
#_88xx_keynavlist = ['Key:KeyPad9', 'Key:KeyPad3', 'Key:KeyPad4', 'Key:KeyPad1', 'Key:KeyPadPound']
#_88xx_keynavlist = ['Key:Soft2']
_88xx_keynavlist = ['Play:sunshine.raw']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPad6']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPad6','Key:KeyPad4','Key:KeyPad1','Key:Soft3']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPadStar','Key:KeyPadStar','Key:KeyPadPound','Key:KeyPadStar','Key:KeyPadStar']
#_88xx_keynavlist = ['Key:Applications','Key:KeyPad5','Key:KeyPad4','Key:KeyPad4','Key:Soft3']
#_88xx_keynavlist = ['Key:Applications'] #,'Key:KeyPad6','Key:KeyPad4','Key:KeyPad1','Key:Soft3']
#_88xx_keynavlist = ['Key:KeyPad2']

alphaCCap = ['Key:KeyPad2', 'Key:KeyPad2', 'Key:KeyPad2', 'Key:KeyPad2', 'Key:KeyPad2', 'Key:KeyPad2', 'Key:KeyPad2']
alphaI = ['Key:KeyPad4', 'Key:KeyPad4', 'Key:KeyPad4']
alphaS = ['Key:KeyPad7', 'Key:KeyPad7', 'Key:KeyPad7', 'Key:KeyPad7']
alphaC = ['Key:KeyPad2', 'Key:KeyPad2', 'Key:KeyPad2']
alphaO = ['Key:KeyPad6', 'Key:KeyPad6', 'Key:KeyPad6']

key = 'XML'
keynav = {key : []}
url = 'http://10.255.20.93/CGI/Execute'
#url = 'http://10.255.12.51/CGI/Execute'
headers={'content-type':'application/xml'}

for keypress in _88xx_keynavlist:
    ph_nav = etree.Element('CiscoIPPhoneExecute')
    exeit_e = etree.SubElement(ph_nav, 'ExecuteItem')
    exeit_e.set('Priority','0')
    exeit_e.set('URL',keypress)
    phnavstr = etree.tostring(ph_nav,pretty_print=True)
    keynav[key] = keynav[key]+[phnavstr]
'''
for keypress in alphaO:
    ph_nav = etree.Element('CiscoIPPhoneExecute')
    exeit_e = etree.SubElement(ph_nav, 'ExecuteItem')
    exeit_e.set('Priority','0')
    exeit_e.set('URL',keypress)
    phnavstr = etree.tostring(ph_nav,pretty_print=True)
    keynav[key] = keynav[key]+[phnavstr]
'''
#print(keynav)
#print('this')
#print(keynav[key])

for xml in keynav[key]:
    key_press = {}
    key_press[key] = xml
    print("This key press - " + str(key_press))
    r = requests.post(url,headers=headers,data=key_press,auth=(phoneUser,phonePass))
    time.sleep(0.5)
    print("Response code from phone - " + str(r))
    print("Response content from phone - " + str(r.content))

print("All Done!!")
