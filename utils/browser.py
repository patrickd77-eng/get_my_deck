from config.settings import DEBUG_MODE_ON
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#These are options that are intended to make the browser appear less bot-like. These work fine, but you can change them if you want.
def get_browser():
    browser_options = Options()
    if not DEBUG_MODE_ON:
        browser_options.add_argument("--headless=new") #hide browser if we're not in debug, there's no need to display it.
    browser_options.add_argument("--disable-blink-features=AutomationControlled")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--disable-dev-shm-usage")
    browser_options.add_argument("--disable-gpu")
    browser_options.add_argument("--disable-infobars")
    browser_options.add_argument("--disable-extensions")
    browser_options.add_argument("--disable-popup-blocking")
    browser_options.add_argument("--disable-notifications")
    browser_options.add_argument("--disable-logging")
    browser_options.add_argument("--disable-default-apps")
    browser_options.add_argument("--disable-crash-reporter")
    browser_options.add_argument("--disable-in-process-stack-traces")
    browser_options.add_argument("--disable-background-networking")
    browser_options.add_argument("--disable-background-timer-throttling")
    browser_options.add_argument("--disable-client-side-phishing-detection")
    browser_options.add_argument("--disable-hang-monitor")
    browser_options.add_argument("--disable-prompt-on-repost")
    browser_options.add_argument("--disable-renderer-backgrounding")
    browser_options.add_argument("--disable-sync")
    browser_options.add_argument("--disable-translate")
    browser_options.add_argument("--metrics-recording-only")
    browser_options.add_argument("--mute-audio")
    browser_options.add_argument("--no-first-run")
    browser_options.add_argument("--no-default-browser-check")
    browser_options.add_argument("--password-store=basic")
    browser_options.add_argument("--use-mock-keychain")
    browser_options.add_argument("--lang=en-GB") #You can change this to en-US if you want.
    browser_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    browser_options.add_argument("--window-size=1920,1080")
    browser_options.add_argument("--incognito")
    browser_options.add_argument("--disable-web-security")
    browser_options.add_argument("--allow-running-insecure-content")
    browser_options.add_argument("--ignore-certificate-errors")
    browser_options.add_argument("--disable-software-rasterizer")
    browser_options.add_argument("--disable-features=VizDisplayCompositor")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=browser_options)