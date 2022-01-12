import pytest
import allure
from playwright.sync_api import Page, Browser

@pytest.fixture(scope="function")
def page(browser: Browser, request):
    p: Page = browser.new_page(record_video_dir="video/")
    request.page = p
    yield p
    screenshot = p.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    video = p.video.path()
    p.close()
    allure.attach(screenshot, name=f"{request.node.name}", attachment_type=allure.attachment_type.PNG)
    allure.attach.file(f'./{video}', attachment_type=allure.attachment_type.WEBM)