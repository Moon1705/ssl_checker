@echo off
SET SSL_CHECKER_PATH_FOLDER=%~dp0
SET SSL_CHECKER_FILE_NAME=ssl_checker_script.py
SET SSL_CHECKER_LOG_FILE=log\ssl_checker.log
cd /d %SSL_CHECKER_PATH_FOLDER%
python %SSL_CHECKER_FILE_NAME% > %SSL_CHECKER_LOG_FILE% 2>&1
