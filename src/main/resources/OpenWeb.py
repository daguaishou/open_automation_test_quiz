import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from collections import Counter
from publicsuffix2 import PublicSuffixList
from urllib.parse import urlparse


path = r'C:\Users\庞非非\AppData\Local\Google\Chrome\Application\chromedriver.exe'
url = r'https://cn.bing.com/'
my_dict = {'您的名字':'//*[@id="b_results"]/li[14]/nav/ul/li[5]','Selenium':'//*[@id="b_results"]/li[16]/nav/ul/li[5]'}
#strs = ['您的名字','selenium']
#urls = ['https://www.baidu/1','https://cn.bing.com/2','https://www.google.cn/2','https://www.google.cn/2','https://bochaai.com/2']


# 浏览器驱动路径，注意驱动与selenium版本相匹配
service = Service(executable_path=path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#获取顶级域名
def get_tld(url):
    psl = PublicSuffixList()
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return psl.get_public_suffix(domain)

#打开浏览器
driver.get(url)
time.sleep(5)

#窗口最大化
driver.maximize_window()

for key,values in my_dict.items():
    # 找到元素并输入值
    element = driver.find_element(By.ID, 'sb_form_q')
    element.clear()
    element.send_keys(key)
    time.sleep(4)
    # 键盘敲击enter
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(4)
    # 滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    # 点击下一页
    driver.find_element(By.XPATH,values).click()

    """
    element = driver.find_element(By.TAG_NAME,'body')
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(10)
    """
    time.sleep(5)
    # 获取所有的a标签
    elements = driver.find_elements(By.CLASS_NAME, "b_dftt")
    for element in elements:
        print(get_tld(element.get_attribute("herf")))
        print(element)

    # 使用Counter统计每个元素的出现次数
    count = Counter(elements)
    # 打印结果
    print(count)

    # 点击下一页
    # driver.find_element(By.CLASS_NAME, 'sb_pagN').click()
"""
    try:
        # 等待元素出现，最长等待时间10秒
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="b_results"]/li[13]/nav/ul/li[2]/a'))
        )
        # 在这里对element进行操作，例如点击等
        element.click()
    except TimeoutException:
        print("元素没有在指定时间内出现")
"""

#time.sleep(100)
# 关闭浏览器
driver.quit()
