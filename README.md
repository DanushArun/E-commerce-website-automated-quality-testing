# Nike Website Automation Experiment

A Selenium script exploring a live e-commerce journey on Nike India: navigation, product
selection, cart interactions and login-related flows.

## Current state

[Automation_code.py](Automation_code.py) contains the browser automation.
It is not executable as committed: the login call contains literal `<Enter username>` and
`<Enter Password>` placeholders, which are invalid Python syntax.

[test_execution.log](test_execution.log) is a saved execution log. It does not prove that the
current committed script passes, and several handlers log failures without propagating them.
The final success message can therefore appear after an earlier operation failed.

## Dependencies

The script imports Selenium, Requests and webdriver-manager and expects Chrome.
There is no requirements file or dependency lockfile.

```bash
git clone https://github.com/DanushArun/E-commerce-website-automated-quality-testing.git
cd E-commerce-website-automated-quality-testing
python3 -m venv .venv
source .venv/bin/activate
python -m pip install selenium requests webdriver-manager
python -m py_compile Automation_code.py
```

The final command currently reports a syntax error at the placeholder login call.
Resolve that source error before attempting a browser run. The script does not load the
`credentials.json` file described by earlier documentation.

## Execution boundary

This script targets an external production website and performs cart and login interactions.
Run only with an authorized test account and an appropriate testing environment.
Selectors, redirects and anti-automation behavior can change independently of this repository.

## Verification

The source and saved log were reviewed. Syntax validation identified the committed blocker.
No live browser journey was executed for this documentation update.
There is no isolated test fixture, automated assertion suite or verified pass rate.
