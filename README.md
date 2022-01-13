# E-Primer Playwright Tests

This project has some sample Playwright tests for E-Primer app from here:
https://www.exploratorytestingacademy.com/app/ 

## Installing dependencies

Run the following commands to create and activate a Python virtual env:

```
# create venv
python3 -m venv .venv

# run this on Mac/Linux
source .venv/bin/activate 

# run this on Windows
.\venv\Scripts\activate

# install dependencies
pip3 install -r requirements.txt

# install playwright browser binaries
playwright install
```

## Running the tests

The tests are using pytest and Playwright. Use this command to run all tests:

```
pytest tests
```

To run tests in "headed" mode (and with slowmode on to see what is happening), use this:

```
pytest --headed --slowmo=100 tests
```

To run tests on specific browsers, use:

```
pytest --browser chromium --browser firefox tests
```