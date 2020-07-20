# Selenium_Github_signin-out

 This project is used to simulate the user login and logout operations on the GitHub webpage using a browser.（e.g.Google Chrome）
 
# 1.Background
***Selenium*** is a browser automation testing framework.  
It was originally developed for automated testing. After the crawler became popular, it also became a crawler tool. Its function is simply to control the browser, use code to simulate the operation of the browser, and realize automation.

# 2.Install
***Google Chrome*** and ***chromedriver*** need to be installed for this project.  
Below are the versions installed on my Mac.
suit           |version              |location       
---------------|:-------------------:|:-------------:
[Google Chrome](https://www.google.com/intl/zh-CN/chrome/)  |84.0.4147.89(mac64)  |Default path   
[chromedriver](http://chromedriver.chromium.org/downloads)|84.0.4147.30(mac64)  |/usr/local/bin 

# 3.Usage
* Install selenium   
  ```pip install selenium```   
  or install selenium manually in Pycharm.
* Place chromedriver.exe to `/usr/local/bin(on Mac)`
* Change the `'user'` and `'password'` field in the python file
* Run the python file.  
*(If the login is successful, it will automatically log out within a few seconds after the success. If it fails, the login failure page will be displayed.)*

# 4.Development Environment
*Python 3.7 + PyCharm 2019.2.1*
