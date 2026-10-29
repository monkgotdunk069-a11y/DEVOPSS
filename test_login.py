
from pathlib import Path
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


LOGIN_PAGE = Path(__file__).with_name(
    "login.html"
).resolve().as_uri()


def run_login_test(test_name, password, expected, keep_open=False):
    options = Options()
    options.page_load_strategy = "normal"
    driver = None

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(LOGIN_PAGE)

        # Enter username and password
        driver.find_element(
            By.ID, "username"
        ).send_keys("student")

        driver.find_element(
            By.ID, "password"
        ).send_keys(password)

        # Click login
        driver.find_element(
            By.ID, "login"
        ).click()

        # Read actual result
        actual = driver.find_element(
            By.ID, "message"
        ).text

        # Assertion
        assert actual == expected, (
            f"Expected: {expected}, Actual: {actual}"
        )

        print(f"{test_name}: PASS")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        print("-" * 40)

    except Exception as error:
        print(f"{test_name}: FAIL")
        print(error)
        raise

    finally:
        if driver is not None:
            if keep_open:
                input("Press Enter to close the browser...")
            driver.quit()


# Test Case 1: Valid credentials
def test_valid_login():
    run_login_test(
        "Test Case 1",
        "Password123",
        "Login successful"
    )


# Test Case 2: Incorrect password
def test_invalid_password():
    run_login_test(
        "Test Case 2",
        "WrongPassword",
        "Invalid username or password"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Selenium login tests.")
    parser.add_argument(
        "--keep-open",
        action="store_true",
        help="Keep the browser open after each test until Enter is pressed.",
    )
    args = parser.parse_args()

    run_login_test(
        "Test Case 1",
        "Password123",
        "Login successful",
        keep_open=args.keep_open,
    )
    run_login_test(
        "Test Case 2",
        "WrongPassword",
        "Invalid username or password",
        keep_open=args.keep_open,
    )
