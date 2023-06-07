import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

nums = []

PATH = r"C:\Users\mng48\source\repos\tools\chrome driver"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://weather.com/weather/monthly/l/674df01bc334d053adbe68272ba816d5124ede34225906b04639c9694392df03")

for date in range (1,30):
    id = f"[data-id='calendar-6/{date}']"
    element = driver.find_element(By.CSS_SELECTOR, id)
    nums.append(element.text)
print(nums)