# Import the required libraries.
import sys
import os

from datetime import datetime, date, time
import re
import time
import random
from random import randint
import glob

import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Define the log file:
try:
    log_file = open('log_file.txt', mode = 'w')
except:
    print ("Unable to open the log file.")

# Print out the error message to the both standard output and log_file.
def print_log(message):
    try:
        log_file.write(str(datetime.now()) + ': ' + message + '\n')
        print (str(datetime.now()) + ': ' + message)
    except:
        print ("Unable to write into the log file.")

# Expand definition of find_element_by_id to return False in case there is no element.
def exists_by_id(parentObj, idText, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_id(idText)
    except:
        print_log("Element by id = '" + idText + "' not found.")
        if ignoreNone:
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_id(parentObj, idText, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_id(parentObj, idText, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_name to return False in case there is no element.
def exists_by_name(parentObj, name, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_name(name)
    except:
        print_log("Element by name = '" + name + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_tag_name to return False in case there is no element.
def exists_by_tag_name(parentObj, tagName, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_tag_name(tagName)
    except:
        print_log("Element by tag name = '" + tagName + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_css_selector to return False in case there is no element.
def exists_by_css_selector(parentObj, css_selector, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_css_selector(css_selector)
    except:
        print_log("Element by CSS selector = '" + css_selector + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_xpath to return False in case there is no element.
def exists_by_xpath(parentObj, xpath, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_xpath(xpath)
    except:
        print_log("Element by xpath = '" + xpath + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_tag_name to return False in case there is no element.
def exist_all_by_name(parentObj, name, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_name(name)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by name = '" + name + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by name = '" + name + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_tag_name to return False in case there is no element.
def exist_all_by_tag_name(parentObj, tagName, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_tag_name(tagName)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by tag name = '" + tagName + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by tag name = '" + tagName + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_css_selector to return False in case there is no element.
def exist_all_by_css_selector(parentObj, css_selector, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_css_selector(css_selector)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by CSS selector = '" + css_selector + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by CSS selector = '" + css_selector + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_xpath to return False in case there is no element.
def exist_all_by_xpath(parentObj, xpath, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_xpath(xpath)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by xpath = '" + xpath + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by xpath = '" + xpath + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()


# Find the element and extract its text.
def find_and_extract(parentObj, objName, xpath):
    # Find the element.
    ObjTag = exists_by_xpath(parentObj, xpath, True)

    # Find the text of the element.
    if ObjTag != None:
        objText = ObjTag.text
    else:
        objText = ""

    print_log(objName + ": " + objText)

    return objText

def hover_and_click(htmlObj, browser):

    actionChains = ActionChains(browser)
    actionChains.move_to_element(htmlObj).perform()

    browser.execute_script("arguments[0].setAttribute('style', 'visibility:visible;');", htmlObj)

    htmlObj.click()

    # bodyObj = exists_by_tag_name(browser, 'body', ignoreNone = False, waitToFind = True)
    # location = htmlObj.location

    # browser.execute_script("var e = new jQuery.Event('click'); e.pageX = " + str(location['x']) + "; e.pageY = " + str(location['y']) + "; $('body').trigger(e);")

    # actionChains.move_to_element_with_offset(bodyObj, location['x'], location['y'])
    # actionChains.click()
    # actionChains.perform()

# Click the element and wait for a random number between 1 and 10 seconds.
def click_and_wait(htmlObj, browser):

    hover_and_click(htmlObj, browser)

    # Random float x, 1.0 <= x < 10.0
    randomTimePeriod = random.uniform(1, 4)

    print_log("Wait time: " + str(randomTimePeriod) + " seconds")

    time.sleep(randomTimePeriod)

# Go back to the previous page and wait for a random number between 1 and 10 seconds.
def back_and_wait(browser):

    browser.back()

    # Random float x, 1.0 <= x < 10.0
    randomTimePeriod = random.uniform(1, 4)

    print_log("Wait time: " + str(randomTimePeriod) + " seconds")

    time.sleep(randomTimePeriod)

def playLottery(browser):

    for index in range(1, 11):
        option = randint(0, 1)

        if option == 0:
            Decision1OptionABtn = exists_by_id(browser, 'Decision' + str(index) + 'OptionA', ignoreNone = False, waitToFind = True)
            hover_and_click(Decision1OptionABtn, browser)
        else:
            Decision1OptionBBtn = exists_by_id(browser, 'Decision' + str(index) + 'OptionB', ignoreNone = False, waitToFind = True)
            hover_and_click(Decision1OptionBBtn, browser)

    SubmitBtnBtn = exists_by_id(browser, 'SubmitBtn', ignoreNone = False, waitToFind = True)
    hover_and_click(SubmitBtnBtn, browser)

    WillingnessAmount = exists_by_id(browser, 'WillingnessAmount', ignoreNone = False, waitToFind = True)
    willingnessRand = str(random.uniform(0.0, 4.0))
    while WillingnessAmount.get_attribute('value') != willingnessRand:
        WillingnessAmount.send_keys(willingnessRand)
    WillingnessAmount.send_keys(Keys.ENTER)

    ContinueBtn = exists_by_id(browser, 'Continue', ignoreNone = False, waitToFind = True)
    hover_and_click(ContinueBtn, browser)

def playTrust(browser, part):

    slider = exists_by_id(browser, 'slider', ignoreNone = False, waitToFind = True)
    sliderPin = exists_by_tag_name(slider, 'span', ignoreNone = False, waitToFind = True)
    if part == 0:
        moveRnd = randint(0, 5)
        for intNum in range(moveRnd):
            sliderPin.send_keys(Keys.ARROW_RIGHT)

    else:
        moveRnd = randint(0, 5 + ((part-1) * 3))
        for intNum in range(moveRnd):
            sliderPin.send_keys(Keys.ARROW_LEFT)

    SubmitBtnBtn = exists_by_id(browser, 'SliderSubmitBtn', ignoreNone = False, waitToFind = True)
    hover_and_click(SubmitBtnBtn, browser)

def playWholeTrust(browser):

    playTrust(browser, 0)
    playTrust(browser, 1)
    playTrust(browser, 2)
    playTrust(browser, 3)
    playTrust(browser, 4)
    playTrust(browser, 5)
    playTrust(browser, 6)
    SubmitBtnBtn = exists_by_id(browser, 'SliderSubmitBtn', ignoreNone = True, waitToFind = False)
    while SubmitBtnBtn.get_attribute('value') != "Continue...":
        SubmitBtnBtn = exists_by_id(browser, 'SliderSubmitBtn', ignoreNone = True, waitToFind = False)
        print "Waiting to find the Continue... button."
        time.sleep(4)
    errorNum = 0
    isNotSubmitted = True
    while isNotSubmitted and errorNum < 25:
        try:
            SubmitBtnBtn = exists_by_id(browser, 'SliderSubmitBtn', ignoreNone = True, waitToFind = False)
            hover_and_click(SubmitBtnBtn, browser)
            isNotSubmitted = False
        except:
            print "I'm not able to continue yet."
            errorNum += 1

def playGamble(browser):

    optionRnd = randint(1, 9)

    gambleRnd = exists_by_id(browser, 'Gamble' + str(optionRnd), ignoreNone = False, waitToFind = True)
    hover_and_click(gambleRnd, browser)

    SubmitBtnBtn = exists_by_id(browser, 'SubmitBtn', ignoreNone = False, waitToFind = True)
    hover_and_click(SubmitBtnBtn, browser)

    time.sleep(7)
    ContinueBtn = exists_by_id(browser, 'Continue', ignoreNone = False, waitToFind = True)
    hover_and_click(ContinueBtn, browser)



# Main program:

# Define the browser to be used as Mozilla Firefox, because it if the most flexible one among well-known browsers.
firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference('permissions.default.stylesheet', 2)
# firefox_profile.set_preference('permissions.default.image', 2)

while True:
    firefox_profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(firefox_profile)

    # Retrieve the content of the start page.
    browser.get('https://bftrain.miserver.it.umich.edu')
    browser.maximize_window()

    html = exists_by_tag_name(browser, 'html', ignoreNone = False, waitToFind = True)
    html.send_keys(Keys.CONTROL + Keys.SUBTRACT)
    html.send_keys(Keys.CONTROL + Keys.SUBTRACT)
    html.send_keys(Keys.CONTROL + Keys.SUBTRACT)

    inputEmailObj = exists_by_id(browser, "inputEmail", ignoreNone = False, waitToFind = True)

    accountRandomString = base64.urlsafe_b64encode(os.urandom(7)).replace('=', '').replace('_', '').replace('-', '')
    domainRandomString = base64.urlsafe_b64encode(os.urandom(7)).replace('=', '').replace('_', '').replace('-', '')

    inputEmailObj.send_keys(accountRandomString + "@" + domainRandomString + ".com")

    submitMethod = randint(0, 1)

    if submitMethod == 0:
        submitBtn = exists_by_xpath(browser, "/html/body/div/div[1]/div[2]/form/button", ignoreNone = False, waitToFind = True)
        hover_and_click(submitBtn, browser)
    else:
        inputEmailObj.send_keys(Keys.ENTER)
    
    startPretestBtn = exists_by_id(browser, 'StartBtn', ignoreNone = False, waitToFind = True)
    hover_and_click(startPretestBtn, browser)

    for index in range(7):
        linkAnchor = exists_by_css_selector(browser, '.LinkAnchor', ignoreNone = False, waitToFind = True)

        actionChains = ActionChains(browser)
        if randint(0, 1) == 1:
            actionChains.move_to_element(linkAnchor).perform()

        # if randint(0, 1) == 1:
        #     hover_and_click(linkAnchor, browser)

        # if randint(0, 1) == 1:
        #     actionChains.context_click(linkAnchor).perform()

        browser.execute_script("window.scrollTo(0, 1000);")

        YesOrNo = randint(0, 1)

        if YesOrNo == 0:
            NoBtn = exists_by_id(browser, "NoButton", ignoreNone = False, waitToFind = True)
            hover_and_click(NoBtn, browser)
        else:
            YesBtn = exists_by_id(browser, "YesButton", ignoreNone = False, waitToFind = True)
            hover_and_click(YesBtn, browser)

    GotoTrainingBtn = exists_by_id(browser, 'GotoTraining', ignoreNone = False, waitToFind = True)
    hover_and_click(GotoTrainingBtn, browser)

    fileNamesList = ['100015_1194_165.png', '119666_517_126.png', '119670_415_152.png', '119674_391_160.png', '119690_1416_152.png', '126234_1240_126.png', '185316_800_246.png', '185324_796_311.png', '185344_819_389.png', '19910_416_322.png', '199666_101_29.png', '199670_101_29.png', '201658_101_29.png', '201660_101_29.png', '201662_101_29.png', '201889_101_29.png', '201891_101_29.png', '201893_101_29.png', '202092_173_29.png', '202094_173_29.png', '202096_173_29.png', '202693_134_29.png', '202695_134_29.png', '202697_134_29.png', '202733_101_29.png', '202735_101_29.png', '202737_101_29.png', '202743_101_29.png', '202745_101_29.png', '202747_101_29.png', '220086.png', '220089_894_590.png', '220093.png', '220339.png', '220346.png', '220349.png', '220352_894_590.png', '220356.png', '220359.png', '220362.png', '220371.png', '220377.png', '220380_894_590.png', '220390.png', '220396.png', '262279.png', '262351.png', '262419.png', '262423_558_121.png', '262431_657_134.png', '262439_563_93.png', '264566_400_161.png', '264570.png', '264574.png', '264657_1240_126.png', '264665_894_590.png', '271141_720_470.png', '271145_327_218.png', '27253_465_189.png', '274445.png', '286051_101_29.png', '286053_101_29.png', '286055_101_29.png', '292881_534_55.png', '292887_772_454.png', '292891_580_441.png', '292895_600_238.png', '296019_519_76.png', '325682_556_81.png', '339488.png', '344120.png', '344123.png', '344126.png', '344129.png', '344534.png', '347674.png', '350077.png', '350301.png', '350310.png', '350318.png', '350327.png', '351290_558_408.png', '351296_738_371.png', '351308_578_190.png', '351814_812_328.png', '353884.png', '353893.png', '353902.png', '353905_753_422.png', '355876_786_307.png', '37551_894_60.png', '40168_457_186.png', '47330.png', '75591_306_213.png', 'Directions_Practice_Email.png', 'Directions_Practice_Email_488.png', 'Directions_Practice_Email_491.png', 'Directions_Practice_Email_494.png', 'Directions_Practice_Email_497.png', 'Directions_Practice_Email_500.png', 'loading.gif', 'Practice_Email.png', 'Practice_Email_490.png', 'Practice_Email_493.png', 'Practice_Email_496.png', 'Practice_Email_499.png', 'Practice_Email_502.png', 'Practice_Email_Question.png', 'Practice_Email_Question_489.png', 'Practice_Email_Question_492.png', 'Practice_Email_Question_495.png', 'Practice_Email_Question_498.png', 'Practice_Email_Question_501.png', 'Press_shift_to_simulate_tab_in_email_button_100.png', 'Press_shift_to_simulate_tab_in_email_button_101.png', 'Press_shift_to_simulate_tab_in_email_button_104.png', 'Press_shift_to_simulate_tab_in_email_button_105.png', 'Press_shift_to_simulate_tab_in_email_button_108.png', 'Press_shift_to_simulate_tab_in_email_button_111.png', 'Press_shift_to_simulate_tab_in_email_button_114.png', 'Press_shift_to_simulate_tab_in_email_button_115.png', 'Press_shift_to_simulate_tab_in_email_button_118.png', 'Press_shift_to_simulate_tab_in_email_button_119.png', 'Press_shift_to_simulate_tab_in_email_button_121.png', 'Press_shift_to_simulate_tab_in_email_button_123.png', 'Press_shift_to_simulate_tab_in_email_button_125.png', 'Press_shift_to_simulate_tab_in_email_button_127.png', 'Press_shift_to_simulate_tab_in_email_button_129.png', 'Press_shift_to_simulate_tab_in_email_button_131.png', 'Press_shift_to_simulate_tab_in_email_button_132.png', 'Press_shift_to_simulate_tab_in_email_button_134.png', 'Press_shift_to_simulate_tab_in_email_button_136.png', 'Press_shift_to_simulate_tab_in_email_button_138.png', 'Press_shift_to_simulate_tab_in_email_button_140.png', 'Press_shift_to_simulate_tab_in_email_button_142.png', 'Press_shift_to_simulate_tab_in_email_button_144.png', 'Press_shift_to_simulate_tab_in_email_button_147.png', 'Press_shift_to_simulate_tab_in_email_button_149.png', 'Press_shift_to_simulate_tab_in_email_button_151.png', 'Press_shift_to_simulate_tab_in_email_button_153.png', 'Press_shift_to_simulate_tab_in_email_button_87.png', 'Press_shift_to_simulate_tab_in_email_button_90.png', 'Press_shift_to_simulate_tab_in_email_button_93.png', 'Press_shift_to_simulate_tab_in_email_button_96.png', 'Press_Shift_T_to_simulate_tab_in_email_button.png', 'Press_shift_T_to_simulate_tab_in_email_button_84.png', 'Requirements_Text.png', 'Rollover.png', 'Rollover_103.png', 'Rollover_107.png', 'Rollover_91.png', 'Rollover_95.png', 'Rollover_99.png', 'Rollover_Caption_100.png', 'Rollover_Caption_101.png', 'Rollover_Caption_102.png', 'Rollover_Caption_104.png', 'Rollover_Caption_105.png', 'Rollover_Caption_106.png', 'Rollover_Caption_108.png', 'Rollover_Caption_109.png', 'Rollover_Caption_110.png', 'Rollover_Caption_111.png', 'Rollover_Caption_112.png', 'Rollover_Caption_113.png', 'Rollover_Caption_114.png', 'Rollover_Caption_115.png', 'Rollover_Caption_116.png', 'Rollover_Caption_117.png', 'Rollover_Caption_118.png', 'Rollover_Caption_119.png', 'Rollover_Caption_120.png', 'Rollover_Caption_121.png', 'Rollover_Caption_122.png', 'Rollover_Caption_123.png', 'Rollover_Caption_124.png', 'Rollover_Caption_125.png', 'Rollover_Caption_126.png', 'Rollover_Caption_127.png', 'Rollover_Caption_128.png', 'Rollover_Caption_129.png', 'Rollover_Caption_130.png', 'Rollover_Caption_131.png', 'Rollover_Caption_132.png', 'Rollover_Caption_133.png', 'Rollover_Caption_134.png', 'Rollover_Caption_135.png', 'Rollover_Caption_136.png', 'Rollover_Caption_137.png', 'Rollover_Caption_138.png', 'Rollover_Caption_139.png', 'Rollover_Caption_140.png', 'Rollover_Caption_141.png', 'Rollover_Caption_142.png', 'Rollover_Caption_143.png', 'Rollover_Caption_144.png', 'Rollover_Caption_145.png', 'Rollover_Caption_146.png', 'Rollover_Caption_147.png', 'Rollover_Caption_148.png', 'Rollover_Caption_149.png', 'Rollover_Caption_150.png', 'Rollover_Caption_151.png', 'Rollover_Caption_152.png', 'Rollover_Caption_153.png', 'Rollover_Caption_154.png', 'Rollover_Caption_155.png', 'Rollover_Caption_29.png', 'Rollover_Caption_31.png', 'Rollover_Caption_37.png', 'Rollover_Caption_38.png', 'Rollover_Caption_39.png', 'Rollover_Caption_46.png', 'Rollover_Caption_48.png', 'Rollover_Caption_50.png', 'Rollover_Caption_51.png', 'Rollover_Caption_52.png', 'Rollover_Caption_53.png', 'Rollover_Caption_54.png', 'Rollover_Caption_88.png', 'Rollover_Caption_89.png', 'Rollover_Caption_90.png', 'Rollover_Caption_92.png', 'Rollover_Caption_93.png', 'Rollover_Caption_94.png', 'Rollover_Caption_96.png', 'Rollover_Caption_97.png', 'Rollover_Caption_98.png', 'si321008.png', 'si321022.png', 'si335414.png', 'si335427.png', 'si335790.png', 'si335803.png', 'si336166.png', 'si336179.png', 'si336542.png', 'si336555.png', 'si336918.png', 'si336931.png', 'si339548.png', 'si339575.png', 'si339633.png', 'si339660.png', 'si341002.png', 'si341029.png', 'si341109.png', 'si341136.png', 'si343367.png', 'si343380.png', 'si343710.png', 'si343723.png', 'si344053.png', 'si344066.png', 'si344221.png', 'si344248.png', 'si344503.png', 'si344516.png', 'si345576.png', 'si345603.png', 'si345917.png', 'si345930.png', 'si346240.png', 'si346253.png', 'si346563.png', 'si346576.png', 'si346886.png', 'si346899.png', 'si347209.png', 'si347222.png', 'si347532.png', 'si347545.png', 'si347885.png', 'si347912.png', 'si348216.png', 'si348229.png', 'si348545.png', 'si348558.png', 'si348874.png', 'si348887.png', 'si349203.png', 'si349216.png', 'si349532.png', 'si349545.png', 'si349861.png', 'si349874.png', 'si352987.png', 'si353014.png', 'si353269.png', 'si353282.png', 'si353533.png', 'si353546.png', 'si353797.png', 'si353810.png', 'SmartShape_11.png', 'SmartShape_12.png', 'SmartShape_15.png', 'SmartShape_16.png', 'SmartShape_17.png', 'SmartShape_194.png', 'SmartShape_20.png', 'SmartShape_249.png', 'SmartShape_262.png', 'SmartShape_266.png', 'SmartShape_279.png', 'SmartShape_283.png', 'SmartShape_29.png', 'SmartShape_298.png', 'SmartShape_30.png', 'SmartShape_31.png', 'SmartShape_311.png', 'SmartShape_312.png', 'SmartShape_313.png', 'SmartShape_315.png', 'SmartShape_319.png', 'SmartShape_344.png', 'SmartShape_360.png', 'SmartShape_406.png', 'SmartShape_408.png', 'SmartShape_409.png', 'SmartShape_416.png', 'SmartShape_417.png', 'SmartShape_418.png', 'SmartShape_421.png', 'SmartShape_422.png', 'SmartShape_436.png', 'SmartShape_438.png', 'SmartShape_439.png', 'SmartShape_440.png', 'SmartShape_442.png', 'SmartShape_451.png', 'SmartShape_452.png', 'SmartShape_453.png', 'SmartShape_454.png', 'SmartShape_508.png', 'SmartShape_509.png', 'SmartShape_510.png', 'SmartShape_512.png', 'SmartShape_513.png', 'SmartShape_514.png', 'SmartShape_516.png', 'SmartShape_517.png', 'SmartShape_518.png', 'SmartShape_520.png', 'SmartShape_521.png', 'SmartShape_522.png', 'SmartShape_524.png', 'SmartShape_525.png', 'SmartShape_526.png', 'SmartShape_528.png', 'SmartShape_529.png', 'SmartShape_530.png', 'SmartShape_532.png', 'SmartShape_533.png', 'SmartShape_534.png', 'SmartShape_535.png', 'SmartShape_536.png', 'SmartShape_537.png', 'SmartShape_538.png', 'SmartShape_539.png', 'SmartShape_540.png', 'SmartShape_541.png', 'SmartShape_542.png', 'SmartShape_543.png', 'SmartShape_550.png', 'SmartShape_551.png', 'SmartShape_552.png', 'SmartShape_553.png', 'SmartShape_554.png', 'SmartShape_555.png', 'SmartShape_556.png', 'SmartShape_557.png', 'SmartShape_558.png', 'SmartShape_559.png', 'SmartShape_560.png', 'SmartShape_561.png', 'SmartShape_569.png', 'SmartShape_570.png', 'SmartShape_571.png', 'SmartShape_572.png', 'SmartShape_573.png', 'SmartShape_574.png', 'Text_Caption_10.png', 'Text_Caption_11.png', 'Text_Caption_12.png', 'Text_Caption_13.png', 'Text_Caption_14.png', 'Text_Caption_16.png', 'Text_Caption_17.png', 'Text_Caption_18.png', 'Text_Caption_19.png', 'Text_Caption_20.png', 'Text_Caption_21.png', 'Text_Caption_22.png', 'Text_Caption_23.png']
    for fileName in fileNamesList:
        browser.get("https://bftrain.miserver.it.umich.edu/static/games/Phishing_Game_Keyboard_Accessible/dr/" + fileName)
        time.sleep(0.25)

    browser.get("https://bftrain.miserver.it.umich.edu/gameselection")

    Decision1OptionABtn = None
    Gamble1 = None
    while Decision1OptionABtn == None and Gamble1 == None:

        Decision1OptionABtn = exists_by_id(browser, 'Decision1OptionA', ignoreNone = True, waitToFind = False)
        Gamble1 = exists_by_id(browser, 'Gamble1', ignoreNone = True, waitToFind = False)

    if Decision1OptionABtn != None:
        playLottery(browser)
        playWholeTrust(browser)
        playGamble(browser)
    if Gamble1 != None:
        playGamble(browser)
        playWholeTrust(browser)
        playLottery(browser)

    randomString = base64.urlsafe_b64encode(os.urandom(13))

    PretestComment = exists_by_id(browser, "PretestComment", ignoreNone = False, waitToFind = True)
    PretestComment.send_keys(randomString)

    TrainingComment = exists_by_id(browser, "TrainingComment", ignoreNone = False, waitToFind = True)
    TrainingComment.send_keys(randomString)

    GamesComment = exists_by_id(browser, "GamesComment", ignoreNone = False, waitToFind = True)
    GamesComment.send_keys(randomString)

    submitBtn = exists_by_tag_name(browser, "button", ignoreNone = False, waitToFind = True)
    hover_and_click(submitBtn, browser)

    browser.quit();
    time.sleep(1)


# time.sleep(10);

# browser.switch_to.frame(exists_by_tag_name(browser, 'iframe', ignoreNone = False, waitToFind = True))

# StartTrainingBtn = exists_by_id(browser, 'Button_54', ignoreNone = False, waitToFind = True)
# # hover_and_click(StartTrainingBtn, browser)
# while not StartTrainingBtn.is_displayed():
#     time.sleep(1)
# actionChains = ActionChains(browser)
# actionChains.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

# ContinueTrainingBtn = exists_by_id(browser, 'Button_57', ignoreNone = True, waitToFind = True)

# while ContinueTrainingBtn == None or not ContinueTrainingBtn.is_displayed():
#     actionChains = ActionChains(browser)
#     actionChains.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

#     ContinueTrainingBtn = exists_by_id(browser, 'Button_57', ignoreNone = True, waitToFind = True)

# # hover_and_click(ContinueTrainingBtn, browser)
# actionChains.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

# Continue_to_Practice_EmailBtn = exists_by_id(browser, 'Continue_to_Practice_Email', ignoreNone = False, waitToFind = True)

# while ContinueTrainingBtn == None or not ContinueTrainingBtn.is_displayed():
#     actionChains = ActionChains(browser)
#     actionChains.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

#     ContinueTrainingBtn = exists_by_id(browser, 'Continue_to_Practice_Email', ignoreNone = True, waitToFind = True)

# # hover_and_click(Continue_to_Practice_EmailBtn, browser)
# actionChains.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

# Practice_Email_Answer = randint(0, 1)

# if Practice_Email_Answer == 0:
#     Practice_Email_NoBtn = exists_by_id(browser, 'Practice_Email_No', ignoreNone = False, waitToFind = True)
#     hover_and_click(Practice_Email_NoBtn, browser)

#     Button_28Btn = exists_by_id(browser, 'Button_28', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_28Btn, browser)
# else:
#     Practice_Email_YesBtn = exists_by_id(browser, 'Practice_Email_Yes', ignoreNone = False, waitToFind = True)
#     hover_and_click(Practice_Email_YesBtn, browser)

#     Button_27Btn = exists_by_id(browser, 'Button_27', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_27Btn, browser)

# Button_29Btn = exists_by_id(browser, 'Button_29', ignoreNone = False, waitToFind = True)
# hover_and_click(Button_29Btn, browser)

# Practice_Email2_Answer = randint(0, 1)

# if Practice_Email2_Answer == 0:
#     Button_22Btn = exists_by_id(browser, 'Button_22', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_22Btn, browser)

#     Practice_Email2_No = randint(0, 1)

#     if Practice_Email2_No == 0:
#         Button_34Btn = exists_by_id(browser, 'Button_34', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_34Btn, browser)
#         Button_35Btn = exists_by_id(browser, 'Button_35', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_35Btn, browser)
#     else:
#         Button_33Btn = exists_by_id(browser, 'Button_33', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_33Btn, browser)
# else:
#     Button_21Btn = exists_by_id(browser, 'Button_21', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_21Btn, browser)

#     Practice_Email2_Yes = randint(0, 1)

#     if Practice_Email2_Yes == 0:
#         Button_32Btn = exists_by_id(browser, 'Button_32', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_32Btn, browser)
#     else:
#         Button_31Btn = exists_by_id(browser, 'Button_31', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_31Btn, browser)

# Practice_Email3_Answer = randint(0, 1)

# if Practice_Email3_Answer == 0:
#     Button_23Btn = exists_by_id(browser, 'Button_23', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_23Btn, browser)

#     Practice_Email3_Yes = randint(0, 1)

#     if Practice_Email3_Yes == 0:
#         Button_37Btn = exists_by_id(browser, 'Button_37', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_37Btn, browser)
#     else:
#         Button_38Btn = exists_by_id(browser, 'Button_38', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_38Btn, browser)
#         Button_41Btn = exists_by_id(browser, 'Button_41', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_41Btn, browser)
# else:
#     Button_24Btn = exists_by_id(browser, 'Button_24', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_24Btn, browser)

#     Practice_Email3_No = randint(0, 1)

#     if Practice_Email3_No == 0:
#         Button_39Btn = exists_by_id(browser, 'Button_39', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_39Btn, browser)
#     else:
#         Button_40Btn = exists_by_id(browser, 'Button_40', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_40Btn, browser)
#         Button_41Btn = exists_by_id(browser, 'Button_41', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_41Btn, browser)

# Practice_Email4_Answer = randint(0, 1)

# if Practice_Email4_Answer == 0:
#     Button_25Btn = exists_by_id(browser, 'Button_25', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_25Btn, browser)

#     Practice_Email4_Yes = randint(0, 1)

#     if Practice_Email4_Yes == 0:
#         Button_43Btn = exists_by_id(browser, 'Button_43', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_43Btn, browser)
#     else:
#         Button_44Btn = exists_by_id(browser, 'Button_44', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_44Btn, browser)
#         Continue_to_EndBtn = exists_by_id(browser, 'Continue_to_End', ignoreNone = False, waitToFind = True)
#         hover_and_click(Continue_to_EndBtn, browser)
# else:
#     Button_26Btn = exists_by_id(browser, 'Button_26', ignoreNone = False, waitToFind = True)
#     hover_and_click(Button_26Btn, browser)

#     Practice_Email4_No = randint(0, 1)

#     if Practice_Email4_No == 0:
#         Button_45Btn = exists_by_id(browser, 'Button_45', ignoreNone = False, waitToFind = True)
#         hover_and_click(Button_45Btn, browser)
#     else:
#         Review_the_CluesBtn = exists_by_id(browser, 'Review_the_Clues', ignoreNone = False, waitToFind = True)
#         hover_and_click(Review_the_CluesBtn, browser)
#         Continue_to_EndBtn = exists_by_id(browser, 'Continue_to_End', ignoreNone = False, waitToFind = True)
#         hover_and_click(Continue_to_EndBtn, browser)

# QuitBtn = exists_by_id(browser, 'Quit', ignoreNone = False, waitToFind = True)
# hover_and_click(QuitBtn, browser)



