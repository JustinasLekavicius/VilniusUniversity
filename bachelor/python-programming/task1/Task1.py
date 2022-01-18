#First argument: http or ip
#Second argument: 1, 2 or 3
#Third argument: file name, for example test2.log
#Fourth argument (optional): The amount of lines to output.
import re
import sys
dict_ip_html = dict()
criterion1 = sys.argv[1]
criterion2 = sys.argv[2]
criterion3 = "None" #Criterion 3 is titled None by default if the fourth argument (line length) is not entered.

def add_item_to_dict_ip_htmlionary(added_item, added_value):
	if added_item not in dict_ip_html:
		dict_ip_html[added_item] = 0
	if added_item in dict_ip_html:
		dict_ip_html[added_item] = dict_ip_html[added_item] + added_value

def output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, count):
	for key, value in sorted (dict_ip_html.items(), key=lambda kv: kv[1], reverse=True):
		if criterion3 == 0:
			break
		if criterion3 == "None":
			""
		else: criterion3 = criterion3 - 1
		if criterion2 == '1':
			print(sys.argv[1].upper(), key, ", request count: ", value)
		if criterion2 == '2':
			print(sys.argv[1].upper(), key, ", request count percentage: ", ((value / count) * 100), "%")
		if criterion2 == '3':
			print(sys.argv[1].upper(), key, ", total amount of bytes transferred: ", value)

if len(sys.argv) == 5:
	criterion3 = int (sys.argv[4])
try:
	with open(sys.argv[3]) as logfile:
		if (criterion1 != 'ip' and criterion1 != 'http') or (criterion2 != '1' and criterion2 != '2' and criterion2 != '3'):
			print("Incorrect parameters! Please try again.")
			sys.exit(0)

		if criterion1 == 'ip' and criterion2 == '1':
			for line in logfile:
				ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', line)[0]
				add_item_to_dict_ip_htmlionary(ip, 1)
			output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, 1)

		if criterion1 == 'ip' and criterion2 == '2':
			count = 0
			for line in logfile:
				count = count + 1
				ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', line)[0]
				add_item_to_dict_ip_htmlionary(ip, 1)
			output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, count)

		if criterion1 == 'ip' and criterion2 == '3':
			for line in logfile:
				ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', line)[0]
				bytes = re.findall('[0-9]\s(\d{1,20}|\-)\s\"', line)[0]
				if '-' in bytes:
					bytes = 0
				add_item_to_dict_ip_htmlionary(ip, int(bytes))
			output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, 1)

		if criterion1 == 'http' and criterion2 == '1':
			for line in logfile:
				http = re.findall('\"\s(\d{3}|\-)\s[0-9|\-]', line )[0]
				add_item_to_dict_ip_htmlionary(http, 1)
			output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, 1)

		if criterion1 == 'http' and criterion2 == '2':
			count = 0
			for line in logfile:
				count = count + 1
				http = re.findall('\"\s(\d{3}|\-)\s[0-9|\-]', line )[0]
				add_item_to_dict_ip_htmlionary(http, 1)
			output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, count)

		if criterion1 == 'http' and criterion2 == '3':
			for line in logfile:
				http = re.findall('\"\s(\d{3}|\-)\s[0-9|\-]', line )[0]
				bytes = re.findall('[0-9]\s(\d{1,20}|\-)\s\"', line)[0]
				if '-' in bytes:
					bytes = 0
				add_item_to_dict_ip_htmlionary(http, int(bytes))
			output_dict_ip_htmlionary(dict_ip_html, criterion2, criterion3, 1)


except FileNotFoundError:
	print("File not found! You may have entered the wrong file name.")


