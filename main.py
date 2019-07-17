import datetime

from moduls import ssl_checker as sc
from prettytable import PrettyTable


date_check_start = datetime.datetime.now()
table_checks = PrettyTable(["Domain", "Status message", "Grade"])
list_domains = sc.open_domain_list()
table_check_domain = sc.check_domains(list_domains, table_checks)
sc.print_result(table_check_domain, date_check_start)

