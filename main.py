import pyautogui
from selenium import webdriver
from tkinter import *
from tkinter import messagebox
import time
import pygetwindow as gw
from PIL import Image, ImageTk
import FuncSetupImage as funcS
import ImageExample as imgE
import requests
from datetime import datetime

scr_w, scr_h = pyautogui.size()


root = Tk()
root.title("Instagram Auto")
root.iconbitmap('./Images/app_logo.ico')
root.geometry('840x185+'+str(int(scr_w/6))+'+'+str(int(scr_h/2.8)))
root.minsize(840, 185)
root.maxsize(840, 185)

username = StringVar()

password = StringVar()

number_of_stories = StringVar()
number_of_stories.set('1')

timer = StringVar()
timer.set('0')

download_user = StringVar()

global user_url


def start_count():
    a = timer.get()
    for i in range(int(a), 0, -1):
        time.sleep(1)
        timer.set(str(i))
        root.update()


def get_profile_url():
    time.sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]').click()
    global user_url
    user_url = driver.current_url
    time.sleep(0.5)
    driver.get('https://www.instagram.com/')


def delete_story():

    driver.get(user_url)

    time.sleep(2)

    for i in range(int(number_of_stories.get())):
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/div/div').click()

        time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div[1]/div/section/div/header/div[2]/div[2]/button[2]').click()

        time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div/button[1]').click()

        time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div[2]/button[1]').click()

        time.sleep(1)
        driver.get(user_url)
        time.sleep(2)


def delete_one_story_with_check():

    driver.get(user_url)

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/div/div').click()
    time.sleep(1)
    try:
        if pyautogui.locateOnScreen('./images/seenby.png', confidence=0.8) is not None:

            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div[1]/div/section/div/div[3]/div[2]/button'
            ).click()

            time.sleep(1)

            if pyautogui.locateOnScreen('./images/scrollcheck.png', confidence=0.8) is not None:

                root.update()

                x, y = pyautogui.locateCenterOnScreen('./images/scrollcheck.png', confidence=0.8)
                pyautogui.moveTo(x, y)

                while True:
                    if pyautogui.locateOnScreen('./images/scrollstop.png', confidence=0.8) is not None:
                        pyautogui.scroll(-20)
                        try:
                            if pyautogui.locateOnScreen('./images/check_personal.png', confidence=0.6) is not None:
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div/div/div[1]/div/div[2]/button').click()

                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[1]/section/div[1]/div/section/div/header/div[2]/div[2]/button[2]'
                                ).click()

                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div/div/div/button[1]').click()
                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div/div/div[2]/button[1]').click()

                                break
                            else:
                                messagebox.showinfo(title="Not seen", message="The user haven't seen yet")
                                driver.get(user_url)
                                break
                        except Exception as err:
                            print(err)
                            messagebox.showerror(title="Error",
                                                 message="Somethings went wrong!, should re-setup check_personal.png")
                    else:

                        pyautogui.scroll(-40)

                        try:
                            if pyautogui.locateOnScreen('./images/check_personal.png', confidence=0.6) is not None:

                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div/div/div[1]/div/div[2]/button'
                                ).click()
                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[1]/section/div[1]/div/section/div/header/div[2]/div[2]/button[2]'
                                ).click()
                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div/div/div/button[1]'
                                ).click()
                                time.sleep(1)

                                driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div/div/div[2]/button[1]'
                                ).click()

                                break
                            else:
                                messagebox.showinfo(title="Not seen", message="The user haven't seen yet")
                                driver.get(user_url)
                                break
                        except Exception as err:
                            print(err)
                            messagebox.showerror(title="Error",
                                                 message="Somethings went wrong!, should re-setup check_personal.png")
            else:

                root.update()

                try:
                    if pyautogui.locateOnScreen('./images/check_personal.png', confidence=0.6) is not None:

                        time.sleep(1)

                        driver.find_element_by_xpath(
                            '/html/body/div[5]/div/div/div/div[1]/div/div[2]/button'
                        ).click()

                        time.sleep(1)

                        driver.find_element_by_xpath(
                            '/html/body/div[1]/section/div[1]/div/section/div/header/div[2]/div[2]/button[2]'
                        ).click()

                        time.sleep(1)

                        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[1]').click()

                        time.sleep(1)

                        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[1]').click()

                    else:
                        messagebox.showinfo(title="Not seen", message="The user haven't seen yet")
                        driver.get(user_url)
                except Exception as err:
                    print(err)
                    messagebox.showerror(title="Error",
                                         message="Somethings went wrong!, should re-setup check_personal.png")
        else:
            messagebox.showinfo(title="No body seen", message="There are nobody seen yet")
            driver.get(user_url)
    except Exception as err:
        print(err)
        messagebox.showerror(title="Error",
                             message="Somethings went wrong!, should re-setup seenby.png")


def delete_story_with_check():
    driver.get(user_url)

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/div/div').click()

    time.sleep(1)

    for i in range(int(number_of_stories.get()) - 1):
        print(i)
        print(number_of_stories.get())
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/div/section/div/button/div').click()
    try:
        if pyautogui.locateOnScreen('./images/seenby.png', confidence=0.8) is not None:

            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div[1]/div/section/div/div[3]/div[2]/button'
            ).click()

            time.sleep(1)
            if pyautogui.locateOnScreen('./images/scrollcheck.png', confidence=0.8) is not None:
                root.update()
                x, y = pyautogui.locateCenterOnScreen('./images/scrollcheck.png', confidence=0.8)
                pyautogui.moveTo(x, y)
                while True:
                    if pyautogui.locateOnScreen('./images/scrollstop.png', confidence=0.8) is not None:
                        pyautogui.scroll(-20)
                        if pyautogui.locateOnScreen('./images/check_personal.png', confidence=0.6) is not None:
                            delete_story()
                            break
                        else:
                            messagebox.showinfo(title="Not seen", message="The user haven't seen yet")
                            driver.get(user_url)
                            break
                    else:
                        pyautogui.scroll(-40)
                        if pyautogui.locateOnScreen('./images/check_personal.png', confidence=0.6) is not None:
                            delete_story()
                            break
                        else:
                            messagebox.showinfo(title="Not seen", message="The user haven't seen yet")
                            driver.get(user_url)
                            break
            else:
                root.update()
                if pyautogui.locateOnScreen('./images/check_personal.png', confidence=0.6) is not None:
                    delete_story()
                else:
                    messagebox.showinfo(title="Not seen", message="The user haven't seen yet")
                    driver.get(user_url)
        else:
            messagebox.showinfo(title="No body seen", message="There are nobody seen yet")
            driver.get(user_url)
    except Exception as err:
        print(err)
        messagebox.showerror(title="Error",
                             message="Somethings went wrong!, should re-setup seenby.png")


# region Create login and login with check function

global waitinput


def loginmanual():
    root.update()

    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
    ).click()

    time.sleep(0.01)

    while pyautogui.locateOnScreen('./images/logedin.png', confidence=0.6) is None:

        global waitinput
        waitinput = 0

    time.sleep(1)

    try:
        while pyautogui.locateCenterOnScreen('./images/notstoreinfo.png', confidence=0.45) is None:
            time.sleep(0.01)
        else:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        if pyautogui.locateCenterOnScreen('./images/nofi.png', confidence=0.45) is not None:
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    except Exception as err:
        print(err)
        messagebox.showerror(title="Error",
                             message="Somethings went wrong!, should re-setup notstoreinfo.png and nofi.png")


def login():
    root.update()

    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
    ).send_keys(username.get())

    time.sleep(0.01)

    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
    ).send_keys(password.get())

    time.sleep(0.01)

    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button'
    ).click()

    try:
        while pyautogui.locateCenterOnScreen('./images/notstoreinfo.png', confidence=0.45) is None:
            time.sleep(0.01)
            try:
                if driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p') is not None:
                    messagebox.showerror(title="Error",
                                         message="Somethings went wrong!, should check your username and password")
                    driver.get('https://www.instagram.com/')
                    time.sleep(0.5)
                    root.update()
                    break
            except:
                continue
        else:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        if pyautogui.locateCenterOnScreen('./images/nofi.png', confidence=0.45) is not None:
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    except Exception as err:
        print(err)
        messagebox.showerror(title="Error",
                             message="Somethings went wrong!, should re-setup notstoreinfo.png and nofi.png")


global manual


def login_with_check():
    global manual

    try:
        if pyautogui.locateOnScreen('./images/logedin.png', confidence=0.6) is not None:

            time.sleep(1)
        else:
            if pyautogui.locateOnScreen('./images/changeaccount.png', confidence=0.6) is not None:

                corr_x, corr_y = pyautogui.locateCenterOnScreen('./images/changeaccount.png', confidence=0.6)
                pyautogui.click(x=corr_x, y=corr_y, clicks=1, interval=1, button='left')

                time.sleep(0.5)

                if manual == 0:
                    login()
                else:
                    loginmanual()

            else:

                if manual == 0:
                    login()
                else:
                    loginmanual()

        time.sleep(0.2)
    except Exception as err:
        print(err)
        messagebox.showerror(title="Error",
                             message="Somethings went wrong!, should re-setup logedin.png and changeaccount.png")

# endregion


global driver


def initatedriver():
    global driver
    driver = webdriver.Chrome('./chromedriver')


def login_function():
    initatedriver()
    gw.getActiveWindow().maximize()
    driver.get('https://www.instagram.com/')
    root.update()
    login_with_check()
    try:
        get_profile_url()
    except Exception as err:
        print(err)
        driver.close()


def first_function_call():
    global manual
    if str(username.get()) == "" and str(password.get()) == "":
        if messagebox.askyesno(title="Manual login confirm",
                               message="Your username and password haven't been set. Do you want manual login?"):
            manual = 1
            login_function()
    elif str(username.get()) == "" or str(password.get()) == "":
        if str(username.get()) == "":
            if messagebox.askyesno(title="Manual login confirm",
                                   message="Your username haven't been set. Do you want manual login?"):
                manual = 1
                login_function()
        elif str(password.get()) == "":
            if messagebox.askyesno(title="Manual login confirm",
                                   message="Your password haven't been set. Do you want manual login?"):
                manual = 1
                login_function()
    else:
        manual = 0
        login_function()


def close_web():
    driver.get('https://www.instagram.com/')
    time.sleep(1.5)
    driver.close()
    messagebox.showinfo(title="Done", message="Done")


def now_delete_story():
    if int(number_of_stories.get()) >= 1:
        first_function_call()
        delete_story()
        close_web()
    else:
        messagebox.showerror(title="Error", message="Must at least 1 story.")


def now_delete_story_check():
    if int(number_of_stories.get()) >= 1:
        first_function_call()
        delete_story_with_check()
        close_web()
    else:
        messagebox.showerror(title="Error", message="Must at least 1 story.")


def now_delete_one_story_check():
    if int(number_of_stories.get()) >= 1:
        first_function_call()
        delete_one_story_with_check()
        close_web()
    else:
        messagebox.showerror(title="Error", message="Must at least 1 story.")


def timed_delete_story():
    if int(number_of_stories.get()) >= 1 and int(timer.get()) >= 10:
        start_count()
        first_function_call()
        delete_story()
        close_web()
    else:
        messagebox.showerror(title="Error", message="Must at least 1 story and timer at least 10 second.")


def timed_delete_story_check():
    if int(number_of_stories.get()) >= 1 and int(timer.get()) >= 10:
        start_count()
        first_function_call()
        delete_story_with_check()
        close_web()
    else:
        messagebox.showerror(title="Error", message="Must at least 1 story and timer at least 10 second.")


def timed_delete_one_story_check():
    if int(number_of_stories.get()) >= 1 and int(timer.get()) >= 10:
        start_count()
        first_function_call()
        delete_one_story_with_check()
        close_web()
    else:
        messagebox.showerror(title="Error", message="Must at least 1 story and timer at least 10 second.")


# region Create function that call function setup image from FuncSetupImage and add some code

def func_setim_scp():
    funcS.set_image_story_check_person()
    gw.getWindowsWithTitle("Re-setup image")[0].moveTo(int(scr_w - (scr_w / 1.7)), int(scr_h / 3))
    gw.getWindowsWithTitle("Re-setup image")[0].activate()


def func_setim_li():
    funcS.set_image_logedin()
    gw.getWindowsWithTitle("Re-setup image")[0].moveTo(int(scr_w - (scr_w / 1.7)), int(scr_h / 3))
    gw.getWindowsWithTitle("Re-setup image")[0].activate()


def func_setim_nsi():
    funcS.set_image_notstoreinfo()
    gw.getWindowsWithTitle("Re-setup image")[0].moveTo(int(scr_w - (scr_w / 1.7)), int(scr_h / 3))
    gw.getWindowsWithTitle("Re-setup image")[0].activate()


def func_setim_nf():
    funcS.set_image_nofi()
    gw.getWindowsWithTitle("Re-setup image")[0].moveTo(int(scr_w - (scr_w / 1.7)), int(scr_h / 3))
    gw.getWindowsWithTitle("Re-setup image")[0].activate()


def func_setim_sb():
    funcS.set_image_seenby()
    gw.getWindowsWithTitle("Re-setup image")[0].moveTo(int(scr_w - (scr_w / 1.7)), int(scr_h / 3))
    gw.getWindowsWithTitle("Re-setup image")[0].activate()

# endregion


def rootclose():
    if messagebox.askyesno(title="Quit", message="Are you sure want to quit?"):
        root.destroy()


global render

def openAuto():
    auto = Toplevel()
    auto.title('Auto Check')
    auto.update()
    auto.geometry('500x139+'+str(int(scr_w-(scr_w/1.7)))+'+'+str(int(scr_h/2.5)))
    auto.maxsize(500, 139)
    auto.minsize(500, 139)
    auto.iconbitmap('./Images/app_logo.ico')
    auto.update()

    global buttonauto

    gw.getWindowsWithTitle('Auto Check')[0].activate()

    timer = StringVar()
    timer.set('4')

    count_timer = StringVar()
    count_timer.set(timer.get())

    loopVar = StringVar()
    loopVar.set('0')

    stopLoop = StringVar()
    stopLoop.set('0')

    funcAstat = StringVar()
    funcAstat.set('Function A is Disable')
    funcBstat = StringVar()
    funcBstat.set('Function B is Disable')

    global trigAfunc
    global trigBfunc

    trigAfunc = 0

    trigBfunc = 0

    MyTimer = Entry(auto, textvariable=timer).grid(row=0, column=0, columnspan=1, ipadx=10)
    MyTimerLable = Label(auto, text='Count-down secs:').grid(row=0, column=1)
    MyTimerLableCount = Label(auto, textvariable=count_timer).grid(row=0, column=2)

    Entry(auto, textvariable=download_user).grid(row=1, column=1, columnspan=2, ipadx=55)
    Label(auto, text='Full link of user:').grid(row=1, column=0)

    Label(auto, textvariable=funcAstat).grid(row=2, column=3, ipadx=3)
    Label(auto, textvariable=funcBstat).grid(row=3, column=3, ipadx=3)

    def funcA():

        driver.get(download_user.get())

        now = datetime.now()
        current_time = now.strftime("%H%M%S%f")

        time.sleep(1)

        while True:

            driver.get(download_user.get())

            time.sleep(1)

            pyautogui.moveTo(26, 51, duration=0.1)

            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/div/div/span/img').click()

            time.sleep(0.5)

            if pyautogui.locateOnScreen('./autocheck/profile.png', confidence=0.7) != None:
                driver.get('https://www.instagram.com/')
                pyautogui.moveTo(1, 1, duration=0.1)
            else:
                try:
                    time.sleep(0.5)

                    video_url = driver.find_element_by_xpath(
                        '/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source').get_attribute(
                        "src")

                    with open('./videos/saved_video{}.mp4'.format(current_time), 'wb') as handle:
                        response = requests.get(video_url, stream=True)

                        if not response.ok:
                            print(response)

                        for block in response.iter_content(1024):
                            if not block:
                                break

                            handle.write(block)
                    time.sleep(0.5)
                    pyautogui.press('right')
                    if pyautogui.locateOnScreen('./autocheck/profile.png', confidence=0.7) != None:
                        driver.get('https://www.instagram.com/')
                        pyautogui.moveTo(1, 1, duration=0.1)
                        break
                    else:
                        while pyautogui.locateOnScreen('./autocheck/profile.png', confidence=0.7) == None:

                            now = datetime.now()
                            current_time = now.strftime("%H%M%S%f")
                            try:
                                video_url = driver.find_element_by_xpath(
                                    '/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source').get_attribute(
                                    "src")

                                with open('./videos/saved_video{}.mp4'.format(current_time), 'wb') as handle:
                                    response = requests.get(video_url, stream=True)

                                    if not response.ok:
                                        print(response)

                                    for block in response.iter_content(1024):
                                        if not block:
                                            break

                                        handle.write(block)

                                pyautogui.press('right')
                                time.sleep(1)
                            except Exception as err:
                                print(err)

                                pic_url = driver.find_element_by_xpath(
                                    '/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute(
                                    "src")

                                with open('./pics/saved_image{}.png'.format(current_time), 'wb') as handle:
                                    response = requests.get(pic_url, stream=True)

                                    if not response.ok:
                                        print(response)

                                    for block in response.iter_content(1024):
                                        if not block:
                                            break

                                        handle.write(block)
                                time.sleep(0.5)
                                pyautogui.press('right')
                                time.sleep(0.5)
                        else:
                            break
                except Exception as err:
                    print(err)
                    time.sleep(1)

                    pic_url = driver.find_element_by_xpath(
                        '/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute("src")

                    with open('./pics/saved_image{}.png'.format(current_time), 'wb') as handle:
                        response = requests.get(pic_url, stream=True)

                        if not response.ok:
                            print(response)

                        for block in response.iter_content(1024):
                            if not block:
                                break

                            handle.write(block)

                    time.sleep(1)
                    pyautogui.press('right')
                    if pyautogui.locateOnScreen('./autocheck/profile.png', confidence=0.7) != None:
                        driver.get('https://www.instagram.com/')
                        pyautogui.moveTo(1, 1, duration=0.1)
                        break
                    else:
                        while pyautogui.locateOnScreen('./autocheck/profile.png', confidence=0.7) == None:

                            now = datetime.now()
                            current_time = now.strftime("%H%M%S%f")
                            try:
                                video_url = driver.find_element_by_xpath(
                                    '/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/video/source').get_attribute(
                                    "src")

                                with open('./videos/saved_video{}.mp4'.format(current_time), 'wb') as handle:
                                    response = requests.get(video_url, stream=True)

                                    if not response.ok:
                                        print(response)

                                    for block in response.iter_content(1024):
                                        if not block:
                                            break

                                        handle.write(block)

                                pyautogui.press('right')
                                time.sleep(0.5)
                            except Exception as err:
                                print(err)

                                pic_url = driver.find_element_by_xpath(
                                    '/html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/img').get_attribute(
                                    "src")

                                with open('./pics/saved_image{}.png'.format(current_time), 'wb') as handle:
                                    response = requests.get(pic_url, stream=True)

                                    if not response.ok:
                                        print(response)

                                    for block in response.iter_content(1024):
                                        if not block:
                                            break

                                        handle.write(block)
                                time.sleep(0.5)
                                pyautogui.press('right')
                                time.sleep(0.5)
                        else:
                            driver.get('https://www.instagram.com/')
                            pyautogui.moveTo(1, 1, duration=0.1)
                            break

    def funcB():
        print('funcB')

    def buff_start():
        print('Start!')
        loopVar.set('1')
        stopLoop.set('0')
        first_function_call()
        if trigAfunc == 1:
            funcA()
            if trigBfunc == 1:
                for i in range(5):
                    time.sleep(1)
        if trigBfunc == 1:
            funcB()
        start()

    def stop_loop():
        print('Stop!')
        loopVar.set('0')
        stopLoop.set('1')
        driver.close()

    def active_func_a():
        global trigAfunc
        trigAfunc = 1
        funcAstat.set('Function A is Active')

    def active_func_b():
        global trigBfunc
        trigBfunc = 1
        funcBstat.set('Function B is Active')

    def disable_func_a():
        global trigAfunc
        trigAfunc = 0
        funcAstat.set('Function A is Disable')

    def disable_func_b():
        global trigBfunc
        trigBfunc = 0
        funcBstat.set('Function B is Disable')

    def start():
        global trigAfunc
        global trigBfunc
        while int(loopVar.get()) == 1 and int(stopLoop.get()) == 0:
            a = int(timer.get())
            if a > 3:
                for i in range(a, 0, -1):
                    if int(stopLoop.get()) == 0:
                        time.sleep(1)
                        count_timer.set(str(i))
                        auto.update()
                    else:
                        count_timer.set(str(a))
                        break
                if int(stopLoop.get()) == 0:
                    if trigAfunc == 1:
                        funcA()
                        if trigBfunc == 1:
                            for i in range(5):
                                time.sleep(1)
                    if trigBfunc == 1:
                        funcB()
                else:
                    count_timer.set(str(a))
                    break
            else:
                print('Timer must greater than 3')
                break

    def closeauto():
        buttonauto.configure(state=NORMAL)
        auto.destroy()

    myButton1 = Button(auto, text="Start!", command=lambda: buff_start()).grid(row=2, column=0, ipadx=50)
    myButton2 = Button(auto, text="Stop!", command=lambda: stop_loop()).grid(row=3, column=0, ipadx=50)

    activeA = Button(auto, text="Active function A!", command=lambda: active_func_a()).grid(row=2, column=1, ipadx=4)
    activeB = Button(auto, text="Active function B!", command=lambda: active_func_b()).grid(row=3, column=1, ipadx=5)

    disableA = Button(auto, text="Disable function A!", command=lambda: disable_func_a()).grid(row=2, column=2, ipadx=4)
    disableB = Button(auto, text="Disable function B!", command=lambda: disable_func_b()).grid(row=3, column=2, ipadx=5)

    Label(auto, text='Function A is ').grid(row=4, column=0, columnspan=4, sticky='W')
    Label(auto, text='Function B is ').grid(row=5, column=0, columnspan=4, sticky='W')

    try:
        if len(gw.getWindowsWithTitle("Auto check")) == 1:
            root.update()
            buttonauto.configure(state=DISABLED)
        else:
            root.update()
            buttonauto.configure(state=NORMAL)
    except Exception as err:
        print(err)
        buttonauto.configure(state=NORMAL)
    auto.protocol("WM_DELETE_WINDOW", closeauto)


def opensetup():
    def close():
        buttonopen.configure(state=NORMAL)
        top.destroy()
    global buttonopen
    top = Toplevel()
    top.title("Re-setup image")
    top.geometry("228x240")
    top.maxsize(228, 240)
    top.minsize(228, 240)
    top.iconbitmap('./Images/app_logo.ico')

    Label(top, text="Save")

    global render

    load = Image.open('./Images/question.png')
    a = load.resize((15, 15))
    render = ImageTk.PhotoImage(a)

    Label(top, text="Change account to check:").grid(row=0, column=0, columnspan=3)
    Button(top, image=render, command=lambda: imgE.image_checkp()).grid(row=0, column=2)
    Label(top, text="").grid(row=1, column=0, columnspan=2)
    Button(top, text='Re-setup', command=lambda: func_setim_scp()).grid(row=2, column=0, columnspan=3)
    Label(top, text="").grid(row=3, column=0, columnspan=2)

    Label(top, text="Change if get error:").grid(row=4, column=0, columnspan=3)
    Label(top, text="").grid(row=5, column=0, columnspan=2)

    Button(top, image=render, command=lambda: imgE.image_logined()).grid(row=6, column=2)
    Label(top, text="Re-setup logined.png").grid(row=6, column=0, sticky='W')
    Button(top, text='Re-setup', command=lambda: func_setim_li()).grid(row=6, column=1)

    Button(top, image=render, command=lambda: imgE.image_nofi()).grid(row=7, column=2)
    Label(top, text="Re-setup nofi.png").grid(row=7, column=0, sticky='W')
    Button(top, text='Re-setup', command=lambda: func_setim_nf()).grid(row=7, column=1)

    Button(top, image=render, command=lambda: imgE.image_notstoreinfo()).grid(row=8, column=2)
    Label(top, text="Re-setup notstoreinfo.png").grid(row=8, column=0, sticky='W')
    Button(top, text='Re-setup', command=lambda: func_setim_nsi()).grid(row=8, column=1)

    Button(top, image=render, command=lambda: imgE.image_seenby()).grid(row=9, column=2)
    Label(top, text="Re-setup seenby.png").grid(row=9, column=0, sticky='W')
    Button(top, text='Re-setup', command=lambda: func_setim_sb()).grid(row=9, column=1)
    root.update()
    top.update()
    gw.getWindowsWithTitle("Re-setup image")[0].moveTo(int(scr_w-(scr_w/1.7)), int(scr_h/3))
    gw.getWindowsWithTitle("Re-setup image")[0].activate()
    try:
        if len(gw.getWindowsWithTitle("Re-setup image")) == 1:
            root.update()
            buttonopen.configure(state=DISABLED)
        else:
            root.update()
            buttonopen.configure(state=NORMAL)
    except Exception as err:
        print(err)
        buttonopen.configure(state=NORMAL)
    top.protocol("WM_DELETE_WINDOW", close)


lableTime = Label(root, text='Input time to delete (seconds)').grid(row=2, column=2, ipadx=5)
countDownTime = Entry(root, textvariable=timer).grid(row=2, column=3, ipadx=50)


lableNumberStory = Label(root, text='Input number of story (default 1) ').grid(row=4, column=2, ipadx=5)
lableNofi = Label(root, text='The deletion will start\nfrom oldest story to newest ',
                  font=("Arial", 12, 'bold'), fg="red4", bg="gray80").grid(row=1, column=1, rowspan=6)

lableNumberNofi = Label(root, text='Must at least 1 or more').grid(row=3, column=3, ipadx=50)
numbersOfStoriesEntry = Entry(root, textvariable=number_of_stories).grid(row=4, column=3, ipadx=50)


lableUser = Label(root, text='Username', font='bold').grid(row=0, column=0, ipadx=25)
usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1, ipadx=50)

lablePass = Label(root, text='Password', font='bold').grid(row=0, column=2, ipadx=25)
passwordEntry = Entry(root, textvariable=password, show="*").grid(row=0, column=3, ipadx=50)


myButton1 = Button(root,
                   text="Delete now",
                   command=lambda: now_delete_story()).grid(row=1, column=0, ipadx=60)

myButton2 = Button(root,
                   text="Delete now with check",
                   command=lambda: now_delete_story_check()).grid(row=2, column=0, ipadx=30)
myButton3 = Button(root,
                   text="Delete one now with check",
                   command=lambda: now_delete_one_story_check()).grid(row=3, column=0, ipadx=18.5)

myButton4 = Button(root,
                   text="Timed Delete",
                   command=lambda: timed_delete_story()).grid(row=4, column=0, ipadx=55)

myButton5 = Button(root,
                   text="Timed Delete with check",
                   command=lambda: timed_delete_story_check()).grid(row=5, column=0, ipadx=25)

myButton6 = Button(root,
                   text="Timed Delete one with check",
                   command=lambda: timed_delete_one_story_check()).grid(row=6, column=0, ipadx=13)

Label(root, text='Open auto window.').grid(row=5, column=2, sticky="E")
buttonauto = Button(root, text='Auto', command=lambda: openAuto())
buttonauto.grid(row=5, column=3, ipadx=91)


Label(root, text='Re-setup image if get an error.').grid(row=6, column=2, sticky="E")
buttonopen = Button(root, text='Re-setup images', command=lambda: opensetup())
buttonopen.grid(row=6, column=3, ipadx=60)

myButton7 = Button(root,
                   text="Timed Delete one with check",
                   command=lambda: first_function_call()).grid(row=7, column=0, ipadx=13)

root.protocol("WM_DELETE_WINDOW", rootclose)
root.mainloop()
