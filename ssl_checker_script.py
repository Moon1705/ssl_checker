import ssllabs_scanner
import datetime
import time
from prettytable import PrettyTable

# Open file ../domain/list_of_domain.txt
def ssl_checker_open_domain_list():
	with open('domain\\list_of_domain.txt') as f_read:
		list_domains = f_read.read().splitlines()
	return list_domains

#Write result check, start and end time in ../result/result_dd.mm.YYYY.txt
def ssl_checker_print_result(table_checks):
	with open('result\\result_check_' + str(date_check_start.strftime("%d.%m.%Y")) + '.txt','tw') as f_write:
		f_write.write("Start check: " + str(date_check_start.strftime("%d-%m-%Y %H:%M")) + "\n")
		f_write.write(table_checks.get_string())
		date_check_end = datetime.datetime.now()
		f_write.write("\nEnd check: " + str(date_check_end.strftime("%d-%m-%Y %H:%M")))

table_checks = PrettyTable(["Domain", "Status message", "Grade"])
list_domains = ssl_checker_open_domain_list()
date_check_start = datetime.datetime.now()
	
for domain in list_domains:
	print(domain + "\n")
	timeout = True
	while timeout:
		try:
			check = ssllabs_scanner.newScan(domain)
			if 'endpoints' in check:
				if check['endpoints'][0]['statusMessage'] == 'Ready':
					table_checks.add_row([domain, check['endpoints'][0]['statusMessage'], check['endpoints'][0]['grade']])
				else:
					table_checks.add_row([domain, check['endpoints'][0]['statusMessage'], 'None'])
			else:
				table_checks.add_row([domain, check['statusMessage'], 'None'])
			timeout = False
		except Exception as e:
			print('ERROR IN TABLE!\n' + repr(e) + '\n')
			time.sleep(300)
		finally:
			ssl_checker_print_result(table_checks)