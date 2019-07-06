#!/bin/bash
SSL_CHECKER_PATH_FOLDER=$(pwd)
SSL_CHECKER_FILE_NAME=$SSL_CHECKER_PATH_FOLDER/ssl_checker_script.py
SSL_CHECKER_LOG_FILE=$SSL_CHECKER_PATH_FOLDER/log/ssl_checker.log
python3 $SSL_CHECKER_FILE_NAME > $SSL_CHECKER_LOG_FILE 2>&1