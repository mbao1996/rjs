# -- coding: utf-8 --
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os
import time

def upto_time():
    not_get = True
    while( not_get ):
        time.sleep(5)
        time_now = time.strftime('%H:%M:%S', time.localtime(time.time()))
        print(time_now)
        if( time_now >= time_want ):
            not_get = False
    return(time_now)

driver = Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

#driver.get("http://www.baidu.com/")
driver.get("https://www.rjs.com/member/user.html#login")
assert u"融金所" in driver.title
element = driver.find_element_by_id("login_username")
element.clear()
element.send_keys("Groningen")
element = driver.find_element_by_id("login_pwd")
element.clear()
element.send_keys("zpl177l36h")
element.send_keys(Keys.RETURN)
time.sleep(3)
#  进入【我要投标】
element = driver.find_element_by_link_text(u"我要投标")
element.send_keys(Keys.RETURN)
time.sleep(2)
# 点击加入

refresh = True
while( refresh ):
    try:
        driver.refresh() # refresh
        css = "#investWrap > div:nth-child(10) > div > ul > li:nth-child(1) > table > tbody > td.td5 > button"
        element = driver.find_element_by_css_selector(css)
        print('优选[',element.text,']')
        if( element.text == '立即加入' ):
            refresh = False
            element.click()
        else:
#            upto_time()     # adjust
            time.sleep(5)
    except Exception as e:
        print ("Exception found", format(e))

# 移到金额框，填金额
# 安选
#xpath = '//*[@id="app-wrap"]/div[4]/div[2]/div[2]/div[1]/input'
#css = '#investWrap > div:nth-child(10) > div > ul > li:nth-child(1) > table > tbody > td.td5 > button'
#element = driver.find_element_by_xpath(xpath)
# 优选
#xpath = '//*[@id="investWrap"]/div[9]/div/ul/li[1]/table/tbody/td[5]/button'
#css = '#app-wrap > div.invest-wrap > div.m-content-top > div:nth-child(3) > button'
css = '#app-wrap > div.invest-wrap > div.m-content-top > div:nth-child(2) > div.money > input[type=text]'
element = driver.find_element_by_css_selector(css)
element.click()
element.clear()
element.send_keys("750")    #adjust
# 确认金额
css = '#app-wrap > div.invest-wrap > div.m-content-top > div:nth-child(2) > button'
element = driver.find_element_by_css_selector(css)
element.click()
time.sleep(1)

# 确认警示
refresh = True
while( refresh ):
    try:
        css = '#app-wrap > div.m-risktip-pop > div > div.risktip-content > div > span'
        element = driver.find_element_by_css_selector(css)
        if( element.text == '我知道了' ):
            refresh = False
            element.click()
        else:
            time.sleep(0.5)
    except Exception as e:
        print ("Exception found", format(e))
# 选择红包
css = '#app-wrap > div.m-invest-pop > div.m-invest-pop-wrap > div > div > div.invt-main > dl > dd:nth-child(3) > div.r-box > div.u-dropdown.u-select2 > div.dropdown_hd'
element = driver.find_element_by_css_selector(css)
element.click()

css = '#app-wrap > div.m-invest-pop > div.m-invest-pop-wrap > div > div > div.invt-main > dl > dd:nth-child(3) > div.r-box > div.u-dropdown.u-select2 > div.dropdown_bd > ul > li:nth-child(2)'
element = driver.find_element_by_css_selector(css)
element.click()

# 确认加入
css = '#app-wrap > div.m-invest-pop > div.m-invest-pop-wrap > div > div > div.invt-main > dl > dd:nth-child(7) > div.r-box > div'
element = driver.find_element_by_css_selector(css)
element.click()

#driver.close()

print('---finished---')
