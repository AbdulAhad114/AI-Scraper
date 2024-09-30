from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_35f00b16-zone-ai_scraper:b5zkxb1p947f'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

def scrape_website(url):
    print('Connecting to Scraping Browser...')

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(url)
        print('waiting for captcha to solve')
        # solve_res = driver.execute('executeCdpCommand', {
        #     'cmd': 'Captcha.waitForSolve',
        #     'params': {'detectTimeout': '10000'},
        # })
        # print('Captcha solved!', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
    
def extract_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup.find_all(['script', 'style']):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_tokens=6000):
    return [dom_content[i:i+max_tokens] for i in range(0, len(dom_content), max_tokens)]

if __name__ == '_main_':
   scrape_website()