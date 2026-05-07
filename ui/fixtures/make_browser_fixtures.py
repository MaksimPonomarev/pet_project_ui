import pytest
from playwright.sync_api import sync_playwright

from config import settings


@pytest.fixture
def get_page_with_context(request):
    #фикстура для создания браузера с контекстом
    with sync_playwright() as p:
        headless = request.config.getoption("--headless")
        browser = p.chromium.launch(headless=headless, slow_mo=settings.slow_mo)
        context = browser.new_context(storage_state="./ui/storage_state.json")
        page = context.new_page()
        page.set_default_timeout(settings.default_timeout)
        page.set_default_navigation_timeout(settings.navigation_timeout)
        try:
            yield page
        finally:
            page.close()
            context.close()
            browser.close()


@pytest.fixture
def get_page_without_context(request):
    #фикстура для создания браузера без контекста
    with sync_playwright() as p:
        headless = request.config.getoption("--headless")
        browser = p.chromium.launch(headless=headless, slow_mo=settings.slow_mo)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(settings.default_timeout)
        page.set_default_navigation_timeout(settings.navigation_timeout)
        try:
            yield page
        finally:
            page.close()
            context.close()
            browser.close()
