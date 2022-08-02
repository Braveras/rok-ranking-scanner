import cv2
import pytesseract
import os
import sys
from PIL import Image, ImageOps
import csv
import numpy
import re

number = ""
row = [
    'ID','Name','Alliance','Power','Total Killpts','T1 Killpts','T2 Killpts','T3 Killpts','T4 Killpts','T5 Killpts',
    'Highest Power','Victory','Defeat','Dead','Scout Times','Gathered rss','Sent rss','Help times']

if len( sys.argv ) <= 3:
    print("I need 3 args")
    sys.exit()

number = sys.argv[1]
name = sys.argv[2]
filename = sys.argv[3]

def PilThresh(img):
    img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR + cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return img

with Image.open(os.getcwd() +'\screens\\' + number + 'gov.png') as im:
    powa = im.crop((1078, 437, 1295, 481))
    powa = PilThresh(powa)
    totalkills = im.crop((1353, 437, 1600, 481))
    totalkills = PilThresh(totalkills)
    govid = im.crop((933, 277, 1140, 318))
    govid = PilThresh(govid)
    alliance = im.crop((768, 433, 1082, 474))
    #alliance = PilThresh(alliance)
    alliance = cv2.cvtColor(numpy.array(alliance), cv2.COLOR_RGB2BGR + cv2.COLOR_BGR2GRAY)
    alliance = cv2.bitwise_not(alliance)
    #cv2.imwrite('whatisthis.png', alliance)
power = pytesseract.image_to_string(powa)
power = power.replace('\n', ' ').strip()
power = power.replace(',', '')
power = power.replace('Power ', '')
idstr = pytesseract.image_to_string(govid, config='--psm 6 -c tessedit_char_whitelist=0123456789')
idstr = idstr.replace('\n', ' ').strip()
idstr = idstr.replace(')', '')
allkills = pytesseract.image_to_string(totalkills)
allkills = allkills.replace('\n', ' ').strip()
allkills = allkills.replace(',', '')
allkills = allkills.replace('Kill Points ', '')
alliancestr = pytesseract.image_to_string(alliance, config='--psm 7 --oem 1')
alliancestr = alliancestr.replace('\n', ' ').strip()
if len(alliancestr) < 10:
    alliancestr = "-"

with Image.open( os.getcwd() +'\screens\\' + number + 'govkills.png') as im:
    T1kills = im.crop((1502, 715, 1707, 755))
    T1kills = PilThresh(T1kills)
    T1kills = cv2.bitwise_not(T1kills)
    T2kills = im.crop((1502, 767, 1707, 810))
    T2kills = PilThresh(T2kills)
    T2kills = cv2.bitwise_not(T2kills)
    T3kills = im.crop((1502, 823, 1707, 863))
    T3kills = PilThresh(T3kills)
    T3kills = cv2.bitwise_not(T3kills)
    T4kills = im.crop((1502, 876, 1707, 918))
    T4kills = PilThresh(T4kills)
    T4kills = cv2.bitwise_not(T4kills)
    T5kills = im.crop((1502, 927, 1707, 968))
    T5kills = PilThresh(T5kills)
    T5kills = cv2.bitwise_not(T5kills)
    t1str = pytesseract.image_to_string(T1kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if t1str is None:
        #print('t1str was none')
        T1kills = im.crop((1626, 715, 1707, 755))
        T1kills = PilThresh(T1kills)
        t1str = pytesseract.image_to_string(T1kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    t2str = pytesseract.image_to_string(T2kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if t2str is None:
        #print('t2str was none')
        T2kills = im.crop((1626, 767, 1707, 810))
        T2kills = PilThresh(T2kills)
        t2str = pytesseract.image_to_string(T2kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    t3str = pytesseract.image_to_string(T3kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if t3str is None:
        #print('t3str was none')
        T3kills = im.crop((1626, 823, 1707, 863))
        T3kills = PilThresh(T3kills)
        t3str = pytesseract.image_to_string(T3kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    t4str = pytesseract.image_to_string(T4kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if t4str is None:
        #print('t4str was none')
        T4kills = im.crop((1626, 876, 1707, 918))
        T4kills = PilThresh(T4kills)
        t4str = pytesseract.image_to_string(T4kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    t5str = pytesseract.image_to_string(T5kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if t5str is None:
        #print('t5str was none')
        T5kills = im.crop((1626, 927, 1707, 968))
        T5kills = PilThresh(T5kills)
        t5str = pytesseract.image_to_string(T5kills, config='--psm 6 -c tessedit_char_whitelist=0123456789')
t1str = t1str.replace('\n', ' ').strip()
t1str = re.sub(' +', ' ', t1str)
t1str = t1str.replace(',', '')
t2str = t2str.replace('\n', ' ').strip()
t2str = re.sub(' +', ' ', t2str)
t2str = t2str.replace(',', '')
t3str = t3str.replace('\n', ' ').strip()
t3str = re.sub(' +', ' ', t3str)
t3str = t3str.replace(',', '')
t4str = t4str.replace('\n', ' ').strip()
t4str = re.sub(' +', ' ', t4str)
t4str = t4str.replace(',', '')
t5str = t5str.replace('\n', ' ').strip()
t5str = re.sub(' +', ' ', t5str)
t5str = t5str.replace(',', '')

with Image.open(os.getcwd() + '\screens\\' + number + 'govinfo.png') as im:
    highestPowa = im.crop((1300, 303, 1580, 360))
    highestPowa = PilThresh(highestPowa)
    victory = im.crop((1300, 381, 1580, 434))
    victory = PilThresh(victory)
    defeat = im.crop((1300, 454, 1580, 507))
    defeat = PilThresh(defeat)
    dead = im.crop((1300, 526, 1580, 579))
    dead = PilThresh(dead)
    scouts = im.crop((1300, 600, 1580, 655))
    scouts = PilThresh(scouts)
    gathered = im.crop((1300, 729, 1580, 785))
    gathered = PilThresh(gathered)
    sent = im.crop((1300, 803, 1580, 857))
    sent = PilThresh(sent)
    helps = im.crop((1300, 877, 1580, 930))
    helps = PilThresh(helps)
    highPowaStr = pytesseract.image_to_string(highestPowa, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    victStr = pytesseract.image_to_string(victory, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if victStr is None:
        #print('victory was none')
        victory = im.crop((1443, 381, 1580, 434))
        victory = PilThresh(victory)
        victStr = pytesseract.image_to_string(victory, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    defStr = pytesseract.image_to_string(defeat, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if defStr is None:
        #print('defeat was none')
        defeat = im.crop((1443, 454, 1580, 507))
        defeat = PilThresh(defeat)
        defStr = pytesseract.image_to_string(defeat, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    deadStr = pytesseract.image_to_string(dead, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if deadStr is None:
        #print('dead was none')
        dead = im.crop((1443, 526, 1580, 579))
        dead = PilThresh(dead)
        deadStr = pytesseract.image_to_string(dead, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    scoutStr = pytesseract.image_to_string(scouts, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if scoutStr is None:
        #print('scouts was none')
        scouts = im.crop((1300, 600, 1580, 655))
        scouts = PilThresh(scouts)
        scoutStr = pytesseract.image_to_string(scouts, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    gatherStr = pytesseract.image_to_string(gathered, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if gatherStr is None:
        #print('gathered was none')
        gathered = im.crop((1300, 729, 1580, 785))
        gathered = PilThresh(gathered)
        gatherStr = pytesseract.image_to_string(gathered, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    sentStr = pytesseract.image_to_string(sent, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if sentStr is None:
        #print('sent was none')
        sent = im.crop((1300, 803, 1580, 857))
        sent = PilThresh(sent)
        sentStr = pytesseract.image_to_string(sent, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    helpsStr = pytesseract.image_to_string(helps, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    if helpsStr is None:
        #print('helps was none')
        helps = im.crop((1300, 877, 1580, 930))
        helps = PilThresh(helps)
        helpsStr = pytesseract.image_to_string(helps, config='--psm 6 -c tessedit_char_whitelist=0123456789')
highPowaStr = highPowaStr.replace('\n', ' ').strip()
highPowaStr = highPowaStr.replace(',', '')
highPowaStr = re.sub(' +', ' ', highPowaStr)
victStr = victStr.replace('\n', ' ').strip()
victStr = victStr.replace(',', '')
victStr = re.sub(' +', ' ', victStr)
defStr = defStr.replace('\n', ' ').strip()
defStr = defStr.replace(',', '')
defStr = re.sub(' +', ' ', defStr)
deadStr = deadStr.replace('\n', ' ').strip()
deadStr = deadStr.replace(',', '')
deadStr = re.sub(' +', ' ', deadStr)
scoutStr = scoutStr.replace('\n', ' ').strip()
scoutStr = scoutStr.replace(',', '')
scoutStr = re.sub(' +', ' ', scoutStr)
gatherStr = gatherStr.replace('\n', ' ').strip()
gatherStr = gatherStr.replace(',', '')
gatherStr = re.sub(' +', ' ', gatherStr)
sentStr = sentStr.replace('\n', ' ').strip()
sentStr = sentStr.replace(',', '')
sentStr = re.sub(' +', ' ', sentStr)
helpsStr = helpsStr.replace('\n', ' ').strip()
helpsStr = helpsStr.replace(',', '')
helpsStr = re.sub(' +', ' ', helpsStr)

with open(os.getcwd()+'\excel\\'+filename+'.csv', 'a', encoding="utf-8") as csvf:
    wr = csv.DictWriter(csvf, fieldnames=row, lineterminator='\n')
    wr.writerow(
        {'ID': idstr, 'Name': name, 'Alliance': alliancestr, 'Power': power, 'Total Killpts': allkills, 'T1 Killpts': t1str, 'T2 Killpts': t2str,
         'T3 Killpts': t3str, 'T4 Killpts': t4str, 'T5 Killpts': t5str, 'Highest Power': highPowaStr,
         'Victory': victStr, 'Defeat': defStr, 'Dead': deadStr, 'Scout Times': scoutStr, 'Gathered rss': gatherStr,
         'Sent rss': sentStr, 'Help times': helpsStr})

os.remove(os.getcwd() + '\screens\\' + number + 'gov.png')
os.remove(os.getcwd() + '\screens\\' + number + 'govkills.png')
os.remove(os.getcwd() + '\screens\\' + number + 'govinfo.png')



