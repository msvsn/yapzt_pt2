from pages.nested_frames_page import NestedFramesPage

def test_get_text_from_frame_method(driver):
    from selenium.webdriver.common.by import By
    page = NestedFramesPage(driver)
    page.open()
    
    # Використовуємо наш новий метод з Middle Level
    text = page.get_text_from_frame("frame-bottom", (By.TAG_NAME, "body"))
    assert "BOTTOM" in text