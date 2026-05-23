from playwright.sync_api import expect
from config import settings


pytest_plugins = [
    "ui.fixtures.page_fixtures",
    "ui.fixtures.make_browser_fixtures",
    "ui.fixtures.user_fixtures"
]

expect.set_options(timeout=settings.default_timeout)

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)