from pages.windows_page import WindowsPage

def test_window_scenario_1(driver):
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()
    page.click_here()
    
    page.wait_for_number_of_windows(2)
    page.switch_to_new_window(original_window)
    assert "New Window" in page.get_page_source()

def test_window_scenario_2(driver):
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()
    page.click_here()
    
    page.wait_for_number_of_windows(2)
    page.switch_to_new_window(original_window)
    page.close_window()
    
    page.switch_to_window(original_window)
    assert page.is_click_here_clickable()

def test_window_scenario_3(driver):
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()
    page.click_here()
    
    page.wait_for_number_of_windows(2) 
    page.switch_to_new_window(original_window)
    assert "New Window" in page.get_page_source()

def test_window_scenario_4(driver):
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()
    
    page.click_here()
    page.click_here()
    
    page.wait_for_number_of_windows(3)
    
    for window in page.get_all_windows():
        page.switch_to_window(window)
        if window == original_window:
            assert "Opening a new window" in page.get_page_source()
        else:
            assert "New Window" in page.get_page_source()