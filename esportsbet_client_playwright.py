from playwright.async_api import async_playwright
import asyncio
from urllib.parse import urlencode
#curl "https://proxy.scrapeops.io/v1/account?api_key=YOUR_API_KEY"

API_KEY = 'd40d2a84-f923-4ca3-916b-70d804f8a68d'

def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/account?' + urlencode(payload)
    return proxy_url

async def main():
    async with async_playwright() as pw: 
        browser = await pw.chromium.launch(
            headless=False  # Show the browser
        )
        page = await browser.new_page()
        await page.goto(get_proxy_url('https://gg.bet/en/?sportIds[]=esports_league_of_legends'))
        # Data Extraction Code Here
        await page.wait_for_timeout(20000)  # Wait for 1 second
        await browser.close()
        
if __name__ == '__main__':
    asyncio.run(main())