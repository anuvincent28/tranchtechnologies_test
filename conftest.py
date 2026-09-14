import pytest
import pytest_html
from pathlib import Path
from playwright.sync_api import sync_playwright
from config import BASE_URL

@pytest.fixture(scope="session")

def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")
    
    
    yield page

    video_path = page.video.path()
    context.close()
    browser.close()
    p.stop()
    request.node.video_path = video_path
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extra.append(pytest_html.extras.image(str(file_name)))

        report.extra = extra

    if report.when == "teardown":
        video_path = getattr(item, "video_path", None)
        if video_path:
            report.extra.append(pytest_html.extras.video(str(video_path)))