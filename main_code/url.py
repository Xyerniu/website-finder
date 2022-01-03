# backend
from selenium import webdriver
import random
import string
import math

user_input = []
words: list[str] = []

with open('lots of uk words.txt', 'r') as f:
    re = f.read()
    re = re.splitlines()
    words = [x for x in re if x.strip()]


def stop():
    global x1
    x1 = False


def main_loop(v5, url, num2, num, end1, bool1, bool2, bool3, bool4):
    global x1
    x1 = True
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    b = num2 + 1
    temp = False
    ve = ""
    while x1 is True:
        i_random = random_string(num, bool1, bool2, bool3, bool4)
        r_word = words[random.randrange(10000)]
        if url == "https://www.youtube.com/results?search_query=":
            if v5 is True:
                ve = url + r_word + i_random + "&sp=EgIQAg%253D%253D"
                if ve in user_input:
                    if bool1 and bool2 and bool3 and bool4 is False and len(user_input) == 10000:
                        x1 = False
                    if bool1 or bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10000, b) * math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if v5 is False:
                ve = url + i_random + "&sp=EgIQAg%253D%253D"
                if ve in user_input:
                    if bool1 or bool2 is True and len(user_input) == (math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if ve in user_input:
                pass
            elif ve:
                user_input.append(ve)
                print(ve)
                try:
                    driver.get(ve)
                except Exception:
                    print(ve + " doesn't work")
        if url == "https://sites.google.com/view/":
            if v5 is True:
                ve = url + r_word + i_random
                if ve in user_input:
                    if bool1 and bool2 and bool3 and bool4 is False and len(user_input) == 10000:
                        x1 = False
                    if bool1 or bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10000, b) * math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if v5 is False:
                ve = url + i_random
                if ve in user_input:
                    if bool1 or bool2 is True and len(user_input) == (math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if ve in user_input:
                pass
            elif ve:
                user_input.append(ve)
                print(ve)
                try:
                    driver.get(ve)
                except Exception:
                    print(ve + " doesn't work")
        if url == "https://www.reddit.com/r/":
            if v5 is True:
                ve = url + r_word + i_random
                if ve in user_input:
                    if bool1 and bool2 and bool3 and bool4 is False and len(user_input) == 10000:
                        x1 = False
                    if bool1 or bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10000, b) * math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if v5 is False:
                ve = url + i_random
                if ve in user_input:
                    if bool1 or bool2 is True and len(user_input) == (math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if ve in user_input:
                pass
            elif ve:
                user_input.append(ve)
                print(ve)
                try:
                    driver.get(ve)
                except Exception:
                    print(ve + " doesn't work")
        else:
            if temp is False:
                print(ve)

            temp = False
            if v5 is True:
                ve = url + r_word + i_random
                for j in range(num2 - 1):
                    r_word = words[random.randrange(10000)]
                    i_random = random_string(num, bool1, bool2, bool3, bool4)
                    ve = ve + r_word + i_random
                ve = ve + end1
                if ve in user_input:
                    if bool1 and bool2 and bool3 and bool4 is False and len(user_input) == 10000:
                        x1 = False
                    if bool1 or bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10000, b) * math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(10000, b) * math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(10000, b) * math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(10000, b) * math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (
                            math.pow(10000, b) * math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if v5 is False:
                ve = url + i_random + end1
                if ve in user_input:
                    if bool1 or bool2 is True and len(user_input) == (math.pow(26, num)):
                        x1 = False
                    if bool3 is True and len(user_input) == (math.pow(10, num)):
                        x1 = False
                    if bool4 is True and len(user_input) == (math.pow(40, num)):
                        x1 = False
                    if bool1 and bool2 is True and len(user_input) == (math.pow(52, num)):
                        x1 = False
                    if bool3 and bool2 or bool1 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool3 and bool4 is True and len(user_input) == (math.pow(50, num)):
                        x1 = False
                    if bool4 and bool2 or bool1 is True and len(user_input) == (math.pow(66, num)):
                        x1 = False
                    if bool1 and bool2 and bool4 is True and len(user_input) == (math.pow(36, num)):
                        x1 = False
                    if bool4 and bool3 and bool1 or bool2 is True and len(user_input) == (math.pow(76, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 is True and len(user_input) == (math.pow(62, num)):
                        x1 = False
                    if bool1 and bool2 and bool3 and bool4 is True and len(user_input) == (math.pow(102, num)):
                        x1 = False
                    else:
                        pass
            if ve in user_input:
                pass
            elif ve:
                user_input.append(ve)
                try:
                    driver.get(ve)
                except Exception:
                    temp = True
    driver.close()


def random_string(length=32, uppercase=True, lowercase=True, numbers=True, symbols=False):
    character_set = ''

    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits
    if symbols:
        character_set += string.punctuation

    return ''.join(random.choice(character_set) for i in range(length))
