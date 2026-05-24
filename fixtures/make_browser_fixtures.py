import re
import pytest
from playwright.sync_api import sync_playwright
from config import settings


@pytest.fixture(scope="session")
def browser(request: pytest.FixtureRequest):
    with sync_playwright() as p:
        headless = request.config.getoption("--headless")
        b = p.chromium.launch(headless=headless, slow_mo=settings.slow_mo)
        yield b
        b.close()


@pytest.fixture
def context(browser, request: pytest.FixtureRequest):
    ctx = browser.new_context()
    if not request.node.get_closest_marker("with_cookie_banner"):
        ctx.route(
            re.compile(r"(googlesyndication|doubleclick|google-analytics|adservice)"),
            lambda route: route.abort()
        )
    yield ctx
    ctx.close()


@pytest.fixture
def page(context):
    p = context.new_page()
    p.set_default_timeout(settings.default_timeout)
    p.set_default_navigation_timeout(settings.navigation_timeout)
    yield p

