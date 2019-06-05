# all test parameters are declared here

delay = 5 #no of seconds to wait before deciding to exit
chrome_driver_path = '/home/apalya/browsers/chromedriver2.46'
website = 'http://www.sunnxt.com'
signin_text = 'Sign In'
profile_icon_xpath = '//span[@class="icomoon icon-icn_profile"]'
signin_link_xpath = '//ul[@class="signinicon dropdown-menu dropdown-menu-right logg"]/li/a'
signin_modal_close_xpath = '//button[@class="close"]'

##modal sigin popup
signin_modal_title_xpath = '//h4[@id="myModalLabel"]/*/div[@class="signin_label"]'
#signin_modal_title_xpath = '//div[@class="signin_label"]'
username_xpath = '//input[@id="email-up"]'
username_placeholder = 'Email / Mobile'
passwd_xpath = '//input[@id="password"][@type="password"]'
password_placeholder = 'Password'
signin_button_xpath = '//div[@class="log_btn"]//button[@type="submit"][@class="btn btn-red"]'
btn_colors = "btn btn-red"
signin_invalid_user = 'Please Enter Valid Email Or Mobile Number'
signin_invalid_format_xpath = '//span[@class="error"]'
user_doesnot_exist = 'User does not exist. Please sign up.'
verify_username_pwd = 'Kindly Verify Your User Id Or Password And Try Again.'
user_doesnot_exist_xpath = '//span[@class="error"]'
invalid_user = 'abcdefg'
invalid_password = '123456'
invalid_username = '1234567899'
invalid_passwd = '9911223344'