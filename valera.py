from playwright.sync_api import Page, expect

def test_search_on_python_org(page: Page):
    # 1. Відкриваємо реальний сайт
    page.goto("https://www.python.org")

    # 2. Перевіряємо заголовок сторінки (assert)
    expect(page).to_have_title("Welcome to Python.org")

    # 3. Знаходимо поле пошуку, вводимо слово "downloads" і тиснемо Enter
    search_input = page.locator("#id-search-field")
    search_input.fill("downloads")
    search_input.press("Enter")

    # 4. Перевіряємо, що у списку результатів є потрібний текст
    results = page.locator(".list-recent-events")
    expect(results).to_contain_text("Download")