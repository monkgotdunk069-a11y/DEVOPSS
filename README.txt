
SELENIUM AUTOMATED WEB TESTING

Requirements:
1. Python installed
2. Google Chrome installed
3. Selenium and pytest packages installed

Installation:
python -m pip install -r requirements.txt

Execution:
python test_login.py

To keep the browser open after each test for manual inspection:
python test_login.py --keep-open

TEST CASE 1:
Username: student
Password: Password123
Expected: Login successful

TEST CASE 2:
Username: student
Password: WrongPassword
Expected: Invalid username or password

Expected status:
Test Case 1: PASS
Test Case 2: PASS
