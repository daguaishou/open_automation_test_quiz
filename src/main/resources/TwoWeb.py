import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

path = r'C:\Users\庞非非\AppData\Local\Google\Chrome\Application\chromedriver.exe'
#url = r'https://jinshuju.net/f/xngzEK?embedded=true&from_template_market=true&banner=show&form_margin=show'
wurl = r'//*[@id="root"]/div/form/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/label/span[2]/span[1]'
url = r'https://jinshuju.net/templates/detail/Dv9JPD'
# 浏览器驱动路径，注意驱动与selenium版本相匹配
service = Service(executable_path=path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

my_dict = {
    'Shendate':datetime.now().strftime('%Y-%m-%d'),
    'ShenPeople':'自动化',
    'Shenphone':'13888888888',
    'company':'测试公司',
    'inworkNum':99,
    'Baodate':datetime.now().strftime('%Y-%m-%d'),
    'MiNum':0,
    'pic':'庞非非',
    'phone':'13888888888',
    'FangAn':'测试内容'
}
def scrollDown():
    # 滚动到页面底部
    action = ActionChains(driver)
    action.send_keys(Keys.PAGE_DOWN).perform()

#打开浏览器
driver.get(url)
time.sleep(5)

#窗口最大化
driver.maximize_window()
time.sleep(5)
#获取iframe
iframe = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div/div[1]/iframe')
driver.switch_to.frame(iframe)
#划到最底部
scrollDown()

#选择单位情况
driver.find_element(By.XPATH,wurl).click()
time.sleep(2)

driver.save_screenshot('..//data/1.png')

#提交第一页表单
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[4]/div[1]/button').click()
#划到最底部
scrollDown()
time.sleep(5)
#定位到第二页，输入时间
date_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[4]/div/div/div[2]/div[1]/div/div/div/div/span/input')
date_input.send_keys(my_dict.get('Shendate'))
time.sleep(2)
#定位到申请人
driver.find_element(By.ID,'TextInputfield_19').send_keys(my_dict.get('ShenPeople'))
time.sleep(2)
#定位到联系方式
driver.find_element(By.NAME,'field_20').send_keys(my_dict.get('Shenphone'))

driver.save_screenshot('..//data/2.png')
time.sleep(2)
#点击下一页
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[3]/div[1]/button[2]').click()
time.sleep(5)
#划到最底部
scrollDown()
#填写公司名称
driver.find_element(By.ID,'TextInputfield_23').send_keys(my_dict.get('company'))
# 等待一段时间（例如2秒）
time.sleep(2)
#设置在岗人数
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[6]/div/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/input').send_keys(my_dict.get('inworkNum'))
# 等待一段时间（例如2秒）
time.sleep(2)
#设置报备日期
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[8]/div/div/div[2]/div[1]/div/div/div/div/span/input').send_keys(my_dict.get('Baodate'))
# 等待一段时间（例如2秒）
time.sleep(2)
#设置密接人数
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[10]/div/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/input').send_keys(my_dict.get('MiNum'))
# 等待一段时间（例如2秒）
time.sleep(2)
#设置负责人
driver.find_element(By.ID,'TextInputfield_27').send_keys(my_dict.get('pic'))
# 等待一段时间（例如2秒）
time.sleep(2)
#划到最底部
scrollDown()
#设置联系方式
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[14]/div/div/div[2]/div[1]/div/div/div/div/span/input').send_keys(my_dict.get('phone'))
# 等待一段时间（例如2秒）
time.sleep(2)
#设置疫情方案
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[16]/div/div/div[2]/div[1]/div/div[2]/div/span/textarea').send_keys(my_dict.get('FangAn'))
# 等待一段时间（例如2秒）
time.sleep(2)
driver.save_screenshot('..//data/3.png')
#提交表单
driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[3]/div[1]/button[2]').submit()
time.sleep(5)
# 退出iframe，回到主文档
driver.switch_to.default_content()
# 关闭浏览器
driver.quit()