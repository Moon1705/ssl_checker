# ssl_checker
SSL Checker is designed to evaluate the work SSL-certificates.

It is necessary:
1. Install **Python** (version 2.7 or 3.7)
2. Install the **requests** and **PrettyTable** packages:
- Python 3.7:
```
pip3 install requests
pip3 install PrettyTable
```
- Python 2.7:
```
pip install requests
pip install PrettyTable
```
3. Write the analyzed domains in the file **domain/list_of_domain.txt**
4. Run **ssl_checker**:
- Windows: ``` start_ssl_checker.bat ```
- Linux: ``` start_ssl_checker.sh ```
> Note: ssl_checker can be run via taskschd.msc and cron
5. Analyze the result in the file **result/result.txt**
> PS: the script log is located in the **log/ssl_checker.log**. Average script running time 3 min / 1 domain

