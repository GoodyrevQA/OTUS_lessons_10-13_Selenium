def test_hello_mail_ru(browser):
    browser.get("https://github.com/")

    assert "GitHub" in browser.title, "Неверный тайтл у сайта"


def test_hello_gosuslugi(browser):
    browser.get("https://www.gosuslugi.ru/")

    assert "Портал государственных услуг" in browser.title, "Неверный тайтл у сайта"
