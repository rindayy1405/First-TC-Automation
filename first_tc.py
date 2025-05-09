from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()  # Nếu dùng Firefox thì đổi thành webdriver.Firefox()

try:
    driver.get("https://www.google.com")
    print("Opened Google")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Test Automation")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    title = driver.title
    print(f"Page title is: {title}")

    assert "Test" in title, "Title does not contain 'Test'"
    print("✅ Test Passed: Title contains 'Test'")

except Exception as e:
    print(f"❌ Test Failed: {e}")

finally:
    driver.quit()
