#!/bin/bash
# If you want to use cron, you need to write the full path to ssl_checker folder in $SSL_CHECKER_PATH_FOLDER
SSL_CHECKER_PATH_FOLDER=$(pwd)
SSL_CHECKER_FILE_NAME=ssl_checker_script.py
SSL_CHECKER_LOG_FILE=log/ssl_checker.log
cd $SSL_CHECKER_PATH_FOLDER
python3 $SSL_CHECKER_FILE_NAME > $SSL_CHECKER_LOG_FILE 2>&1
