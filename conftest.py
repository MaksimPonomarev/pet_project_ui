from playwright.sync_api import expect
from config import settings

pytest_plugins = [
    "fixtures.page_fixtures",
    "fixtures.make_browser_fixtures",
    "fixtures.user_fixtures"
]

expect.set_options(timeout=settings.default_timeout)

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)