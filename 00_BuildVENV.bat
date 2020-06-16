@echo off
REM turning ECHO off, to avoid If statement being printed to stdout


REM Checking that you don't over write the current env, Python will puke.
Echo Verifying not in virtual env already:
IF NOT x"%PROMPT:(env)=%"==x"%PROMPT%" (

    ECHO FAIL: YOU ARE ALREADY IN A VIRTUAL ENV
    ECHO       DEACTIVATE THE CURRENT VENV BEFORE RUNNING THIS SCRIPT
    GOTO END
)
ECHO PASS
ECHO.



REM Checking for Python version 3.7
ECHO Verifying Python Version is 3.7.x:
REM getting python version
FOR /F "tokens=* USEBACKQ" %%F IN (
    `python --version`
) DO (
    SET PYTHON_VERSION=%%F
)
REM IF statement Explained, if (%pythonversion% - "3.7") == %pythonversion%
REM IF ("Python 3.7.4" - "3.7") == "Python 3.7.4"; Evaluates to,  IF "Python .4" == "Python 3.7.4"
REM IF ("Python 3.8.0" - "3.7") == "Python 3.8.0"; Evaluates to,  IF "Python 3.8.0" == "Python 3.8.0"
IF x"%PYTHON_VERSION:3.7=%" == x"%PYTHON_VERSION%" (
    ECHO FAIL: You Need to have python 3.7 installed you have - %PYTHON_VERSION%
    ECHO       This is a requiremnt of the TAF appliation.
    GOTO END
)
ECHO PASS
ECHO.

ECHO BEGINING TO BUILD AND INSTALL TESTING ENVIRONMENT...

REM turning ECHO back on, to see progress of script
@echo on

REM Create the python virtual env
python -m venv --clear env

REM Enter the Virtual env with the activate script
call env\Scripts\activate.bat

REM Upgrade pip within the ENV, This isnt needed but nice to know we are always up to date.
python -m pip install --upgrade pip

REM PIP install all the packages needed.
REM --no-index, tells pip not to look on the interwebs for packages.
REM --find-links, Tells pip where to look instead for package file.
pip install -r requirements.txt


:END