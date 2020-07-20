from selenium import webdriver
import time

driver = webdriver.Chrome()
# 登录GitHub
def login(user,password):
# 打开GitHub登录页
    driver.get("https://github.com/login")
    driver.implicitly_wait(5)       # 隐形等待，最长30秒，如果到之前完成则执行，否则时间到自己执行
    driver.find_element_by_id('login_field').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(3)
    driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
    time.sleep(1)


def check():
    a = driver.find_element_by_css_selector('.flash.flash-full.flash-error').text
    if a == 'Incorrect username or password.':
        print("登录失败")
    else:
        print("登陆成功")


# 退出GitHub
def logout():
    time.sleep(3)

    driver.find_element_by_css_selector('.Header-item.position-relative.mr-0.d-none.d-lg-flex').click()
    driver.find_element_by_css_selector('.dropdown-item.dropdown-signout').click()

login('user','password')   # 在这儿输入你的用户名和密码
logout()
print("成功登录并退出登录")



##driver.quit()