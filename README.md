# Selenium Automation Portfolio

## About
Automation test suite built using **Selenium WebDriver + Python + pytest**  
for testing live web applications across News and Media domain.

**Tester:** Anchal Srivastava  
**Experience:** 2.6+ Years QA Manual + Automation  
**Domain:** News, OTT, E-Commerce  

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Selenium WebDriver | Browser automation |
| pytest | Test framework |
| ChromeDriver | Chrome browser driver |

---

## Test Cases Covered

### 1. Hamburger Menu Test — IndiaTV
**File:** `tests/test_hamburger.py`  
**Site:** indiatv.in  
- Verifies hamburger menu icon is visible and clickable
- Validates menu opens after click by checking "on" class

### 2. Sign In Test — IndiaTV
**File:** `tests/test_signinINDTV.py`  
**Site:** indiatv.in  
- Verifies Sign In button is present in header
- Validates login flow navigation

### 3. Sign In Test — Ample Images
**File:** `tests/test_signinAmple.py`  
**Site:** ampleimages.com  
- Fills email and password using send_keys
- Verifies successful login via URL change

### 4. Registration Test — Ample Images
**File:** `tests/test_registration.py`  
**Site:** ampleimages.com  
- Switches between Sign In and Register tabs
- Fills all form fields including dropdowns
- Uses dynamic timestamp-based unique email
- Handles password field via JavaScript execution

### 5. Live TV Test — IndiaTV
**File:** `tests/test_livetv_play.py`  
**Site:** indiatv.in  
- Verifies Live TV button is clickable
- Validates video player loads and plays

### 6. Share Icons Test — IndiaTV
**File:** `tests/test_share_icons.py`  
**Site:** indiatv.in  
- Verifies WhatsApp share icon visibility
- Opens share popup and validates all icons
- Tests Facebook, Twitter, LinkedIn, Pinterest
- Verifies each platform opens in new window
- Handles multiple browser windows

---

## Concepts Demonstrated
- Explicit and implicit waits
- CSS Selectors and XPath locators
- Dropdown handling using Select class
- Multiple window handling
- JavaScript execution for complex interactions
- Dynamic element handling
- Form filling with send_keys
- pytest fixtures via conftest.py

---

## How To Run

**Install dependencies:**# selenium-automation-portfolio
Selenium WebDriver automation scripts for web testing using Python and pytest
