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

def find_by_ID_and_click(htmlObjID, browser):

    htmlObj = exists_by_id(browser, htmlObjID, ignoreNone = True, waitToFind = False)
    actionChains = ActionChains(browser)
    while not htmlObj.is_displayed():
        actionChains.send_keys(Keys.TAB).perform()
        htmlObj = exists_by_id(browser, htmlObjID, ignoreNone = True, waitToFind = False)

    click_and_wait(htmlObj, browser)

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

    find_by_ID_and_click('SubmitBtn', browser)

    WillingnessAmount = exists_by_id(browser, 'WillingnessAmount', ignoreNone = False, waitToFind = True)
    willingnessRand = str(random.uniform(0.0, 4.0))
    while WillingnessAmount.get_attribute('value') != willingnessRand:
        WillingnessAmount.send_keys(willingnessRand)
    WillingnessAmount.send_keys(Keys.ENTER)

    find_by_ID_and_click('Continue', browser)

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

    find_by_ID_and_click('SliderSubmitBtn', browser)

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
            find_by_ID_and_click('SliderSubmitBtn', browser)
            isNotSubmitted = False
        except:
            print "I'm not able to continue yet."
            errorNum += 1

def FindGame(browser):

    Decision1OptionABtn = None
    Gamble1 = None
    Trust1 = None
    while Decision1OptionABtn == None and Gamble1 == None and Trust1 == None:

        Decision1OptionABtn = exists_by_id(browser, 'Decision1OptionA', ignoreNone = True, waitToFind = False)
        Gamble1 = exists_by_id(browser, 'Gamble1', ignoreNone = True, waitToFind = False)
        Trust1 = exists_by_id(browser, 'SliderSubmitBtn', ignoreNone = True, waitToFind = False)

    return Decision1OptionABtn, Gamble1, Trust1

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
    # browser.get('https://bftrain.miserver.it.umich.edu')
    browser.get('https://bftrain.miserver.it.umich.edu/')
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

    # GotoTrainingBtn = exists_by_id(browser, 'GotoTraining', ignoreNone = False, waitToFind = True)
    # hover_and_click(GotoTrainingBtn, browser)

    find_by_ID_and_click('GotoTraining', browser)

    startTrainingBtn = exists_by_id(browser, 'StartBtn', ignoreNone = False, waitToFind = True)
    click_and_wait(startTrainingBtn, browser)

    startTrainingBtn = exists_by_xpath(browser, '//*[@id="mCSB_1_container"]/div[2]/div[2]/a', ignoreNone = False, waitToFind = True)
    click_and_wait(startTrainingBtn, browser)

    for index in range(4):
        linkAnchor = exists_by_css_selector(browser, '.LinkAnchor', ignoreNone = False, waitToFind = True)

        actionChains = ActionChains(browser)
        if randint(0, 1) == 1:
            actionChains.move_to_element(linkAnchor).perform()

        YesOrNo = randint(0, 1)

        if YesOrNo == 0:
            find_by_ID_and_click("NoButton", browser)
        else:
            find_by_ID_and_click("YesButton", browser)

        find_by_ID_and_click("Continue", browser)

        if index == 0:
            find_by_ID_and_click("Continue", browser)


    find_by_ID_and_click("StartBtn", browser)

    participationDecision = randint(0, 2)

    if participationDecision == 0:
        find_by_ID_and_click("ParticipateBtn", browser)

        find_by_ID_and_click("ConsentSignature", browser)

        find_by_ID_and_click("Continue", browser)

        for gameIndex in range(3):
            Decision1OptionABtn, Gamble1, Trust1 = FindGame(browser)

            if Decision1OptionABtn != None:
                playLottery(browser)
            elif Gamble1 != None:
                playGamble(browser)
            elif Trust1 != None:
                playWholeTrust(browser)

        randomString = base64.urlsafe_b64encode(os.urandom(13))

        PretestComment = exists_by_id(browser, "FullnameInput", ignoreNone = False, waitToFind = True)
        PretestComment.send_keys(randomString)

        PretestComment = exists_by_id(browser, "StreetInput", ignoreNone = False, waitToFind = True)
        PretestComment.send_keys(randomString)

        PretestComment = exists_by_id(browser, "CityInput", ignoreNone = False, waitToFind = True)
        PretestComment.send_keys(randomString)

        PretestComment = exists_by_id(browser, "StateInput", ignoreNone = False, waitToFind = True)
        PretestComment.send_keys(randomString)

        PretestComment = exists_by_id(browser, "ZipCodeInput", ignoreNone = False, waitToFind = True)
        PretestComment.send_keys("12345")

        find_by_ID_and_click("SubmitBtn", browser)

        SurveyComment = exists_by_name(browser, "Emailsperday", ignoreNone = False, waitToFind = True)
        SurveyComment.send_keys(Keys.ENTER)

        SurveyComment = exists_by_name(browser, "YearsOfInternet", ignoreNone = False, waitToFind = True)
        SurveyComment.send_keys(Keys.ENTER)

        find_by_ID_and_click("SubmitBtn", browser)

    elif participationDecision == 1:
        find_by_ID_and_click("PostponeBtn", browser)

        find_by_ID_and_click("StartBtn", browser)

    elif participationDecision == 2:
        find_by_ID_and_click("QuitBtn", browser)

        find_by_ID_and_click("StartBtn", browser)



    # PretestComment = exists_by_id(browser, "PretestComment", ignoreNone = False, waitToFind = True)
    # PretestComment.send_keys(randomString)

    # TrainingComment = exists_by_id(browser, "TrainingComment", ignoreNone = False, waitToFind = True)
    # TrainingComment.send_keys(randomString)

    # GamesComment = exists_by_id(browser, "GamesComment", ignoreNone = False, waitToFind = True)
    # GamesComment.send_keys(randomString)

    # submitBtn = exists_by_tag_name(browser, "button", ignoreNone = False, waitToFind = True)
    # hover_and_click(submitBtn, browser)

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



