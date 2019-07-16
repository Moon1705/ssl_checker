import datetime
import time
import os
from moduls import ssllabs_scanner as ss

def absolute_path(absol_path) -> str:
	'''Return absolutely path in any OS'''
	return os.path.abspath(absol_path)

def open_domain_list() -> list:
	'''Open file ../domain/list_of_domain.txt'''
	with open(absolute_path('domain/list_of_domain.txt')) as f_read:
		list_domains = f_read.read().splitlines()
	return list_domains

def print_result(table_checks, date_check_start) -> None:
	'''Write result check, start and end time in ../result/result.txt'''
	data_format = "%d-%m-%Y %H:%M"
	with open(absolute_path('result/result.txt'), 'w') as f_write:
		f_write.write("Start check: {}\n".format(str(date_check_start.strftime(data_format))))
		f_write.write(table_checks.get_string())
		date_check_end = datetime.datetime.now()
		f_write.write("\nEnd check: {}".format(str(date_check_end.strftime(data_format))))
	return None

def check_domains(list_domains, table_checks):
	'''Check domain and return table domain with grade'''
	for domain in list_domains:
		print(domain + "\n")
		timeout = True
		while timeout:
			try:
				check = ss.newScan(domain)
				if 'endpoints' in check:
					status_message = check['endpoints'][0]['statusMessage']
					if status_message == 'Ready':
						grade = check['endpoints'][0]['grade']
						table_checks.add_row([domain, status_message, grade])
					else:
						grade = 'None'
						table_checks.add_row([domain, status_message, grade])
				else:
					table_checks.add_row([domain, check['statusMessage'], 'None'])
				timeout = False
			except Exception as e:
				print('ERROR IN TABLE!\n' + repr(e) + '\n')
				time.sleep(100)
	return table_checks