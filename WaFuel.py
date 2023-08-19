# whilts inthe folder that the files have been stored in command shell (gti add && gti commit -a -m "*file name*" && git push)
# to update a cloned repository that has already been downloaded , make sure terminal in folder (git pull)
# clone repo onto computer (git clone gti.github.com:Luke3573/WaFuel.git)
#ensure the SSH code is correct for that PC and added to the Git hub repo settings

from bs4 import BeautifulSoup
import urllib.request
import re
import xlsxwriter
import random
import pandas as pb
from github import Github
import datetime
import time

#INPUT TAGS
ACCESS_TOKEN = "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"
GITHUB_REPO = "WaFuel"
GIT_BRANCH = "main"
INTERNAL_FILE_ULP = "WaFuel/WaFuelULP.html"
FOLDER_EMPL_IN_GIT_ULP = "WaFuel/WaFuelULP.html"
INTERNAL_FILE_98 = "WaFuel/WaFuel98.html"
FOLDER_EMPL_IN_GIT_98 = "WaFuel/WaFuel98.html"
INTERNAL_FILE_DSL = "WaFuel/WaFuelDSL.html"
FOLDER_EMPL_IN_GIT_DSL = "WaFuel/WaFuelDSL.html"
INTERNAL_FILE_LPG = "WaFuel/WaFuelLPG.html"
FOLDER_EMPL_IN_GIT_LPG = "WaFuel/WaFuelLPG.html"
INTERNAL_FILE_95 = "WaFuel/WaFuel95.html"
FOLDER_EMPL_IN_GIT_95 = "WaFuel/WaFuel95.html"


#INPUT TAGS
def ULP():
    workbook = xlsxwriter.Workbook('WaFuelULP.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 36)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 8)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 12)
    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Location', bold)
    worksheet.write('C1', 'Suberb', bold)
    worksheet.write('D1', 'PostCode', bold)
    worksheet.write('E1', 'Price Today', bold)
    worksheet.write('F1', 'Price Tomorrow', bold)
    worksheet.write('G1', 'Brand', bold)
    row = 1
    col = 0
    col1 = 1
    col2 = 2
    col3 = 3
    col4 = 4
    col5 = 5
    col6 = 6

    url='https://www.fuelwatch.wa.gov.au/api/sites?fuelType=ULP'
    req = urllib.request.Request(url,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    sauce = urllib.request.urlopen(req).read()

    soup=BeautifulSoup(sauce,'html.parser')

    pattern=re.compile(r'sitename[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words=2

    for elem in soup(text=pattern):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col, data)
            row += 1

    pattern1=re.compile(r'line1[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words1=2

    for elem in soup(text=pattern1):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern1,x.strip()+' ')]# +' ' to conform with our pattern
        row = 1
        for index in list_indices:
            start=index-no_of_words1
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col1, data)
            row += 1

    pattern2=re.compile(r'location[\.,|" ]',re.IGNORECASE)
    no_of_words2=2

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col2, data)
            row += 1
    pattern3=re.compile(r'postCode[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words3=1

    for elem in soup(text=pattern3):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern3,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words3
            end=index+no_of_words3+1
            if start<0:
                start=0
            data = (list[index+1:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col3, data)
            row += 1

    pattern2=re.compile(r'brandname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word711 = '711'
    wordamp = 'AMP'
    wordalt = 'ATL'
    wordbet = 'BET'
    wordbp = 'BP'
    wordcal = 'CAL'
    wordcco = 'CCO'
    wordcgl = 'CGL'
    wordcol = 'COL'
    wordea = 'EA'
    wordega = 'EGA'
    wordff = 'FF'
    wordgul = 'GUL'
    wordind = 'IND'
    wordlib = 'LIB'
    wordmet = 'MET'
    wordmob = 'MOB'
    wordpum = 'PUM'
    wordshl = 'SHL'
    wordutd = 'UTD'
    wordvib = 'VIB'
    wordwaf = 'WAF'
    wordxcv = 'XCV'
    wordbur = 'BUR'
    wordphx = 'PHX'
    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            if word711 in data:
                data = '7 Eleven'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbur in data:
                data = 'BURK'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordphx in data:
                data = 'Pheonix'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordamp in data:
                data = 'Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordalt in data:
                data = 'Atlas'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbet in data:
                data = 'Better Choice'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbp in data:
                data = 'BP'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcal in data:
                data = 'Caltex'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcco in data:
                data = 'Costco'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcgl in data:
                data = 'CGL Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcol in data:
                data = 'Coles Express'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordea in data:
                data = 'Eagle'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordega in data:
                data = 'EG Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordff in data:
                data = 'FastFuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordgul in data:
                data = 'Gull'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordind in data:
                data = 'Independent'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordlib in data:
                data = 'Liberty'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmet in data:
                data = 'Metro'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmob in data:
                data = 'Mobil'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordpum in data:
                data = 'Puma'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordshl in data:
                data = 'Shell'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordutd in data:
                data = 'United'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordvib in data:
                data = 'Vibe'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordwaf in data:
                data = 'WA Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordxcv in data:
                data = 'X Convenience'
                worksheet.write_string(row, col6, data)
                row += 1
            else:
                row += 1
    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    pattern9=re.compile(r'pricetoday[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:
                data = data[7]
                data=data.replace('_', " ")
                data=data.replace('}', "")
                worksheet.write_string(row, col4, data)
                row += 1

            else:
                worksheet.write_string(row, col4, 'N/A')
                row += 1

    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:

                if word1 in data:
                    data = data[10]
                    data=data.replace('_', " ")
                    worksheet.write_string(row, col5, data)
                    row += 1
                else:
                    worksheet.write_string(row, col5, 'N/A')
                    row += 1

            elif word2 in data:
                data = data[7]
                data=data.replace('_', " ")
                worksheet.write_string(row, col5, data)
                row += 1

            else:
                worksheet.write_string(row, col5, 'N/A')
                row += 1

    workbook.close()

def PUP():
    workbook = xlsxwriter.Workbook('WaFuel95.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 36)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 8)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 12)
    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Location', bold)
    worksheet.write('C1', 'Suberb', bold)
    worksheet.write('D1', 'PostCode', bold)
    worksheet.write('E1', 'Price Today', bold)
    worksheet.write('F1', 'Price Tomorrow', bold)
    worksheet.write('G1', 'Brand', bold)
    row = 1
    col = 0
    col1 = 1
    col2 = 2
    col3 = 3
    col4 = 4
    col5 = 5
    col6 = 6

    url='https://www.fuelwatch.wa.gov.au/api/sites?fuelType=PUP'
    req = urllib.request.Request(url,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    sauce = urllib.request.urlopen(req).read()

    soup=BeautifulSoup(sauce,'html.parser')

    pattern=re.compile(r'sitename[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words=2

    for elem in soup(text=pattern):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col, data)
            row += 1

    pattern1=re.compile(r'line1[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words1=2

    for elem in soup(text=pattern1):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern1,x.strip()+' ')]# +' ' to conform with our pattern
        row = 1
        for index in list_indices:
            start=index-no_of_words1
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col1, data)
            row += 1

    pattern2=re.compile(r'location[\.,|" ]',re.IGNORECASE)
    no_of_words2=2

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col2, data)
            row += 1
    pattern3=re.compile(r'postCode[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words3=1

    for elem in soup(text=pattern3):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern3,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words3
            end=index+no_of_words3+1
            if start<0:
                start=0
            data = (list[index+1:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col3, data)
            row += 1

    pattern2=re.compile(r'brandname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word711 = '711'
    wordamp = 'AMP'
    wordalt = 'ATL'
    wordbet = 'BET'
    wordbp = 'BP'
    wordcal = 'CAL'
    wordcco = 'CCO'
    wordcgl = 'CGL'
    wordcol = 'COL'
    wordea = 'EA'
    wordega = 'EGA'
    wordff = 'FF'
    wordgul = 'GUL'
    wordind = 'IND'
    wordlib = 'LIB'
    wordmet = 'MET'
    wordmob = 'MOB'
    wordpum = 'PUM'
    wordshl = 'SHL'
    wordutd = 'UTD'
    wordvib = 'VIB'
    wordwaf = 'WAF'
    wordxcv = 'XCV'
    wordbur = 'BUR'
    wordphx = 'PHX'
    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            if word711 in data:
                data = '7 Eleven'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbur in data:
                data = 'BURK'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordphx in data:
                data = 'Pheonix'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordamp in data:
                data = 'Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordalt in data:
                data = 'Atlas'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbet in data:
                data = 'Better Choice'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbp in data:
                data = 'BP'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcal in data:
                data = 'Caltex'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcco in data:
                data = 'Costco'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcgl in data:
                data = 'CGL Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcol in data:
                data = 'Coles Express'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordea in data:
                data = 'Eagle'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordega in data:
                data = 'EG Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordff in data:
                data = 'FastFuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordgul in data:
                data = 'Gull'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordind in data:
                data = 'Independent'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordlib in data:
                data = 'Liberty'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmet in data:
                data = 'Metro'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmob in data:
                data = 'Mobil'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordpum in data:
                data = 'Puma'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordshl in data:
                data = 'Shell'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordutd in data:
                data = 'United'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordvib in data:
                data = 'Vibe'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordwaf in data:
                data = 'WA Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordxcv in data:
                data = 'X Convenience'
                worksheet.write_string(row, col6, data)
                row += 1
            else:
                row += 1
    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    pattern9=re.compile(r'pricetoday[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:
                data = data[7]
                data=data.replace('_', " ")
                data=data.replace('}', "")
                worksheet.write_string(row, col4, data)
                row += 1

            else:
                worksheet.write_string(row, col4, 'N/A')
                row += 1

    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:

                if word1 in data:
                    data = data[10]
                    data=data.replace('_', " ")
                    worksheet.write_string(row, col5, data)
                    row += 1
                else:
                    worksheet.write_string(row, col5, 'N/A')
                    row += 1

            elif word2 in data:
                data = data[7]
                data=data.replace('_', " ")
                worksheet.write_string(row, col5, data)
                row += 1

            else:
                worksheet.write_string(row, col5, 'N/A')
                row += 1

    workbook.close()

def PRE():
    workbook = xlsxwriter.Workbook('WaFuel98.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 36)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 8)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 12)
    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Location', bold)
    worksheet.write('C1', 'Suberb', bold)
    worksheet.write('D1', 'PostCode', bold)
    worksheet.write('E1', 'Price Today', bold)
    worksheet.write('F1', 'Price Tomorrow', bold)
    worksheet.write('G1', 'Brand', bold)
    row = 1
    col = 0
    col1 = 1
    col2 = 2
    col3 = 3
    col4 = 4
    col5 = 5
    col6 = 6

    url='https://www.fuelwatch.wa.gov.au/api/sites?fuelType=98R'
    req = urllib.request.Request(url,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    sauce = urllib.request.urlopen(req).read()

    soup=BeautifulSoup(sauce,'html.parser')

    pattern=re.compile(r'sitename[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words=2

    for elem in soup(text=pattern):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col, data)
            row += 1

    pattern1=re.compile(r'line1[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words1=2

    for elem in soup(text=pattern1):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern1,x.strip()+' ')]# +' ' to conform with our pattern
        row = 1
        for index in list_indices:
            start=index-no_of_words1
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col1, data)
            row += 1

    pattern2=re.compile(r'location[\.,|" ]',re.IGNORECASE)
    no_of_words2=2

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col2, data)
            row += 1
    pattern3=re.compile(r'postCode[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words3=1

    for elem in soup(text=pattern3):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern3,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words3
            end=index+no_of_words3+1
            if start<0:
                start=0
            data = (list[index+1:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col3, data)
            row += 1

    pattern2=re.compile(r'brandname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word711 = '711'
    wordamp = 'AMP'
    wordalt = 'ATL'
    wordbet = 'BET'
    wordbp = 'BP'
    wordcal = 'CAL'
    wordcco = 'CCO'
    wordcgl = 'CGL'
    wordcol = 'COL'
    wordea = 'EA'
    wordega = 'EGA'
    wordff = 'FF'
    wordgul = 'GUL'
    wordind = 'IND'
    wordlib = 'LIB'
    wordmet = 'MET'
    wordmob = 'MOB'
    wordpum = 'PUM'
    wordshl = 'SHL'
    wordutd = 'UTD'
    wordvib = 'VIB'
    wordwaf = 'WAF'
    wordxcv = 'XCV'
    wordbur = 'BUR'
    wordphx = 'PHX'
    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            if word711 in data:
                data = '7 Eleven'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbur in data:
                data = 'BURK'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordphx in data:
                data = 'Pheonix'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordamp in data:
                data = 'Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordalt in data:
                data = 'Atlas'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbet in data:
                data = 'Better Choice'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbp in data:
                data = 'BP'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcal in data:
                data = 'Caltex'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcco in data:
                data = 'Costco'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcgl in data:
                data = 'CGL Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcol in data:
                data = 'Coles Express'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordea in data:
                data = 'Eagle'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordega in data:
                data = 'EG Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordff in data:
                data = 'FastFuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordgul in data:
                data = 'Gull'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordind in data:
                data = 'Independent'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordlib in data:
                data = 'Liberty'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmet in data:
                data = 'Metro'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmob in data:
                data = 'Mobil'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordpum in data:
                data = 'Puma'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordshl in data:
                data = 'Shell'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordutd in data:
                data = 'United'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordvib in data:
                data = 'Vibe'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordwaf in data:
                data = 'WA Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordxcv in data:
                data = 'X Convenience'
                worksheet.write_string(row, col6, data)
                row += 1
            else:
                row += 1
    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    pattern9=re.compile(r'pricetoday[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:
                data = data[7]
                data=data.replace('_', " ")
                data=data.replace('}', "")
                worksheet.write_string(row, col4, data)
                row += 1

            else:
                worksheet.write_string(row, col4, 'N/A')
                row += 1

    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:

                if word1 in data:
                    data = data[10]
                    data=data.replace('_', " ")
                    worksheet.write_string(row, col5, data)
                    row += 1
                else:
                    worksheet.write_string(row, col5, 'N/A')
                    row += 1

            elif word2 in data:
                data = data[7]
                data=data.replace('_', " ")
                worksheet.write_string(row, col5, data)
                row += 1

            else:
                worksheet.write_string(row, col5, 'N/A')
                row += 1

    workbook.close()

def DSL():
    workbook = xlsxwriter.Workbook('WaFuelDSL.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 36)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 8)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 12)
    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Location', bold)
    worksheet.write('C1', 'Suberb', bold)
    worksheet.write('D1', 'PostCode', bold)
    worksheet.write('E1', 'Price Today', bold)
    worksheet.write('F1', 'Price Tomorrow', bold)
    worksheet.write('G1', 'Brand', bold)
    row = 1
    col = 0
    col1 = 1
    col2 = 2
    col3 = 3
    col4 = 4
    col5 = 5
    col6 = 6

    url='https://www.fuelwatch.wa.gov.au/api/sites?fuelType=DSL'
    req = urllib.request.Request(url,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    sauce = urllib.request.urlopen(req).read()

    soup=BeautifulSoup(sauce,'html.parser')

    pattern=re.compile(r'sitename[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words=2

    for elem in soup(text=pattern):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col, data)
            row += 1

    pattern1=re.compile(r'line1[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words1=2

    for elem in soup(text=pattern1):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern1,x.strip()+' ')]# +' ' to conform with our pattern
        row = 1
        for index in list_indices:
            start=index-no_of_words1
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col1, data)
            row += 1

    pattern2=re.compile(r'location[\.,|" ]',re.IGNORECASE)
    no_of_words2=2

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col2, data)
            row += 1
    pattern3=re.compile(r'postCode[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words3=1

    for elem in soup(text=pattern3):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern3,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words3
            end=index+no_of_words3+1
            if start<0:
                start=0
            data = (list[index+1:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col3, data)
            row += 1

    pattern2=re.compile(r'brandname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word711 = '711'
    wordamp = 'AMP'
    wordalt = 'ATL'
    wordbet = 'BET'
    wordbp = 'BP'
    wordcal = 'CAL'
    wordcco = 'CCO'
    wordcgl = 'CGL'
    wordcol = 'COL'
    wordea = 'EA'
    wordega = 'EGA'
    wordff = 'FF'
    wordgul = 'GUL'
    wordind = 'IND'
    wordlib = 'LIB'
    wordmet = 'MET'
    wordmob = 'MOB'
    wordpum = 'PUM'
    wordshl = 'SHL'
    wordutd = 'UTD'
    wordvib = 'VIB'
    wordwaf = 'WAF'
    wordxcv = 'XCV'
    wordbur = 'BUR'
    wordphx = 'PHX'
    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            if word711 in data:
                data = '7 Eleven'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbur in data:
                data = 'BURK'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordphx in data:
                data = 'Pheonix'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordamp in data:
                data = 'Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordalt in data:
                data = 'Atlas'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbet in data:
                data = 'Better Choice'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbp in data:
                data = 'BP'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcal in data:
                data = 'Caltex'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcco in data:
                data = 'Costco'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcgl in data:
                data = 'CGL Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcol in data:
                data = 'Coles Express'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordea in data:
                data = 'Eagle'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordega in data:
                data = 'EG Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordff in data:
                data = 'FastFuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordgul in data:
                data = 'Gull'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordind in data:
                data = 'Independent'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordlib in data:
                data = 'Liberty'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmet in data:
                data = 'Metro'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmob in data:
                data = 'Mobil'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordpum in data:
                data = 'Puma'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordshl in data:
                data = 'Shell'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordutd in data:
                data = 'United'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordvib in data:
                data = 'Vibe'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordwaf in data:
                data = 'WA Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordxcv in data:
                data = 'X Convenience'
                worksheet.write_string(row, col6, data)
                row += 1
            else:
                row += 1
    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    pattern9=re.compile(r'pricetoday[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:
                data = data[7]
                data=data.replace('_', " ")
                data=data.replace('}', "")
                worksheet.write_string(row, col4, data)
                row += 1

            else:
                worksheet.write_string(row, col4, 'N/A')
                row += 1

    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:

                if word1 in data:
                    data = data[10]
                    data=data.replace('_', " ")
                    worksheet.write_string(row, col5, data)
                    row += 1
                else:
                    worksheet.write_string(row, col5, 'N/A')
                    row += 1

            elif word2 in data:
                data = data[7]
                data=data.replace('_', " ")
                worksheet.write_string(row, col5, data)
                row += 1

            else:
                worksheet.write_string(row, col5, 'N/A')
                row += 1

    workbook.close()

def LPG():
    workbook = xlsxwriter.Workbook('WaFuelLPG.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 36)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 8)
    worksheet.set_column('E:E', 15)
    worksheet.set_column('F:F', 15)
    worksheet.set_column('G:G', 12)
    worksheet.write('A1', 'Name', bold)
    worksheet.write('B1', 'Location', bold)
    worksheet.write('C1', 'Suberb', bold)
    worksheet.write('D1', 'PostCode', bold)
    worksheet.write('E1', 'Price Today', bold)
    worksheet.write('F1', 'Price Tomorrow', bold)
    worksheet.write('G1', 'Brand', bold)
    row = 1
    col = 0
    col1 = 1
    col2 = 2
    col3 = 3
    col4 = 4
    col5 = 5
    col6 = 6

    url='https://www.fuelwatch.wa.gov.au/api/sites?fuelType=LPG'
    req = urllib.request.Request(url,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    sauce = urllib.request.urlopen(req).read()

    soup=BeautifulSoup(sauce,'html.parser')

    pattern=re.compile(r'sitename[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words=2

    for elem in soup(text=pattern):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col, data)
            row += 1

    pattern1=re.compile(r'line1[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words1=2

    for elem in soup(text=pattern1):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        list_indices=[i for i,x in enumerate(list) if re.match(pattern1,x.strip()+' ')]# +' ' to conform with our pattern
        row = 1
        for index in list_indices:
            start=index-no_of_words1
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col1, data)
            row += 1

    pattern2=re.compile(r'location[\.,|" ]',re.IGNORECASE)
    no_of_words2=2

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col2, data)
            row += 1
    pattern3=re.compile(r'postCode[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words3=1

    for elem in soup(text=pattern3):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern3,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words3
            end=index+no_of_words3+1
            if start<0:
                start=0
            data = (list[index+1:end])
            data = data[0]
            data=data.replace('_', " ")
            worksheet.write_string(row, col3, data)
            row += 1

    pattern2=re.compile(r'brandname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word711 = '711'
    wordamp = 'AMP'
    wordalt = 'ATL'
    wordbet = 'BET'
    wordbp = 'BP'
    wordcal = 'CAL'
    wordcco = 'CCO'
    wordcgl = 'CGL'
    wordcol = 'COL'
    wordea = 'EA'
    wordega = 'EGA'
    wordff = 'FF'
    wordgul = 'GUL'
    wordind = 'IND'
    wordlib = 'LIB'
    wordmet = 'MET'
    wordmob = 'MOB'
    wordpum = 'PUM'
    wordshl = 'SHL'
    wordutd = 'UTD'
    wordvib = 'VIB'
    wordwaf = 'WAF'
    wordxcv = 'XCV'
    wordbur = 'BUR'
    wordphx = 'PHX'
    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+1
            if start<0:
                start=0
            data = (list[index+2:end])
            data = data[0]
            data=data.replace('_', " ")
            if word711 in data:
                data = '7 Eleven'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbur in data:
                data = 'BURK'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordphx in data:
                data = 'Pheonix'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordamp in data:
                data = 'Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordalt in data:
                data = 'Atlas'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbet in data:
                data = 'Better Choice'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordbp in data:
                data = 'BP'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcal in data:
                data = 'Caltex'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcco in data:
                data = 'Costco'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcgl in data:
                data = 'CGL Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordcol in data:
                data = 'Coles Express'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordea in data:
                data = 'Eagle'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordega in data:
                data = 'EG Ampol'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordff in data:
                data = 'FastFuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordgul in data:
                data = 'Gull'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordind in data:
                data = 'Independent'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordlib in data:
                data = 'Liberty'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmet in data:
                data = 'Metro'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordmob in data:
                data = 'Mobil'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordpum in data:
                data = 'Puma'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordshl in data:
                data = 'Shell'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordutd in data:
                data = 'United'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordvib in data:
                data = 'Vibe'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordwaf in data:
                data = 'WA Fuel'
                worksheet.write_string(row, col6, data)
                row += 1
            elif wordxcv in data:
                data = 'X Convenience'
                worksheet.write_string(row, col6, data)
                row += 1
            else:
                row += 1
    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    pattern9=re.compile(r'pricetoday[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:
                data = data[7]
                data=data.replace('_', " ")
                data=data.replace('}', "")
                worksheet.write_string(row, col4, data)
                row += 1

            else:
                worksheet.write_string(row, col4, 'N/A')
                row += 1

    pattern2=re.compile(r'shortname[\.,|" ]',re.IGNORECASE)
    no_of_words2=2
    word1 = 'priceToday'
    word2 = 'priceTomorrow'

    for elem in soup(text=pattern2):
        str=elem.parent.text
        str=str.replace(':', "")
        str=str.replace(' ', "_")
        str=str.replace('"', " ")
        str=str.replace(',', " ")
        str=str.replace('"''"', " ")
        list=str.split(' ')
        row = 1
        list_indices=[i for i,x in enumerate(list) if re.match(pattern2,x.strip()+' ')]# +' ' to conform with our pattern
        for index in list_indices:
            start=index-no_of_words2
            end=index+no_of_words+12
            data = (list[index+2:end])
            if word1 in data:

                if word1 in data:
                    data = data[10]
                    data=data.replace('_', " ")
                    worksheet.write_string(row, col5, data)
                    row += 1
                else:
                    worksheet.write_string(row, col5, 'N/A')
                    row += 1

            elif word2 in data:
                data = data[7]
                data=data.replace('_', " ")
                worksheet.write_string(row, col5, data)
                row += 1

            else:
                worksheet.write_string(row, col5, 'N/A')
                row += 1

    workbook.close()
    
# convert exel to CSV then to HTML
def Convert():
    read_file = pb.read_excel (r'WaFuelULP.xlsx')
    read_file.to_csv (r'WaFuelULP.csv', index = None, header=True)
    df = pb.read_csv('WaFuelULP.csv')
    df.to_html('WaFuelULP.html')

    read_file = pb.read_excel(r'WaFuel95.xlsx')
    read_file.to_csv(r'WaFuel/WaFuel95.csv', index=None, header=True)
    df = pb.read_csv('WaFuel/WaFuel95.csv')
    df.to_html('WaFuel95.html')

    read_file = pb.read_excel(r'WaFuel98.xlsx')
    read_file.to_csv(r'WaFuel/WaFuel98.csv', index=None, header=True)
    df = pb.read_csv('WaFuel/WaFuel98.csv')
    df.to_html('WaFuel98.html')

    read_file = pb.read_excel(r'WaFuelDSL.xlsx')
    read_file.to_csv(r'WaFuel/WaFuelDSL.csv', index=None, header=True)
    df = pb.read_csv('WaFuel/WaFuelDSL.csv')
    df.to_html('WaFuelDSL.html')

    read_file = pb.read_excel(r'WaFuelLPG.xlsx')
    read_file.to_csv(r'WaFuel/WaFuelLPG.csv', index=None, header=True)
    df = pb.read_csv('WaFuel/WaFuelLPG.csv')
    df.to_html('WaFuelLPG.html')

def UpLoad_ULP(access_tocken, github_repo, git_branch, initial_file, folder_empl_in_git):
    g = Github(access_tocken)

    repo = g.get_user().get_repo(github_repo)

    all_files = []
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    with open(initial_file, 'r') as file:
        content = file.read()

    # Upload to github
    if folder_empl_in_git in all_files:
        contents = repo.get_contents(folder_empl_in_git)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch=git_branch)
        return folder_empl_in_git + ' UPDATED'
    else:
        repo.create_file(folder_empl_in_git, "committing files", content, branch=git_branch)
        return folder_empl_in_git + ' CREATED'

def UpLoad_98(access_tocken, github_repo, git_branch, initial_file, folder_empl_in_git):
    g = Github(access_tocken)

    repo = g.get_user().get_repo(github_repo)

    all_files = []
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    with open(initial_file, 'r') as file:
        content = file.read()

    # Upload to github
    if folder_empl_in_git in all_files:
        contents = repo.get_contents(folder_empl_in_git)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch=git_branch)
        return folder_empl_in_git + ' UPDATED'
    else:
        repo.create_file(folder_empl_in_git, "committing files", content, branch=git_branch)
        return folder_empl_in_git + ' CREATED'

def UpLoad_95(access_tocken, github_repo, git_branch, initial_file, folder_empl_in_git):
    g = Github(access_tocken)

    repo = g.get_user().get_repo(github_repo)

    all_files = []
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    with open(initial_file, 'r') as file:
        content = file.read()

    # Upload to github
    if folder_empl_in_git in all_files:
        contents = repo.get_contents(folder_empl_in_git)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch=git_branch)
        return folder_empl_in_git + ' UPDATED'
    else:
        repo.create_file(folder_empl_in_git, "committing files", content, branch=git_branch)
        return folder_empl_in_git + ' CREATED'

def UpLoad_DSL(access_tocken, github_repo, git_branch, initial_file, folder_empl_in_git):
    g = Github(access_tocken)

    repo = g.get_user().get_repo(github_repo)

    all_files = []
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    with open(initial_file, 'r') as file:
        content = file.read()

    # Upload to github
    if folder_empl_in_git in all_files:
        contents = repo.get_contents(folder_empl_in_git)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch=git_branch)
        return folder_empl_in_git + ' UPDATED'
    else:
        repo.create_file(folder_empl_in_git, "committing files", content, branch=git_branch)
        return folder_empl_in_git + ' CREATED'

def UpLoad_LPG(access_tocken, github_repo, git_branch, initial_file, folder_empl_in_git):
    g = Github(access_tocken)

    repo = g.get_user().get_repo(github_repo)

    all_files = []
    contents = repo.get_contents("")

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    with open(initial_file, 'r') as file:
        content = file.read()

    # Upload to github
    if folder_empl_in_git in all_files:
        contents = repo.get_contents(folder_empl_in_git)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch=git_branch)
        return folder_empl_in_git + ' UPDATED'
    else:
        repo.create_file(folder_empl_in_git, "committing files", content, branch=git_branch)
        return folder_empl_in_git + ' CREATED'

# schedualer time pattern for runnung RUN script
def scheduler():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute

    if hour == 6 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 7 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 8 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 9 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 10 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 11 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 12 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 13 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 14 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 15 and minute == 0:
        time.sleep(20)
        RUN()

    elif hour == 16 and minute == 0:
        time.sleep(20)
        RUN()
        
    elif hour == 17 and minute == 0:
        time.sleep(20)
        RUN()
        
    elif hour == 18 and minute == 0:
        time.sleep(20)
        RUN()

    else:
        time.sleep(20)
        scheduler()

def RUN():
    ULP()
    PUP()
    PRE()
    DSL()
    LPG()
    Convert()
    call(git add, shell=True)
    call(git commit -a -m "updated files", shell=True)
    call(git push, shell=True)
    #UpLoad_ULP(ACCESS_TOKEN, GITHUB_REPO, GIT_BRANCH, INTERNAL_FILE_ULP, FOLDER_EMPL_IN_GIT_ULP)
    #UpLoad_95(ACCESS_TOKEN, GITHUB_REPO, GIT_BRANCH, INTERNAL_FILE_95, FOLDER_EMPL_IN_GIT_95)
    #UpLoad_DSL(ACCESS_TOKEN, GITHUB_REPO, GIT_BRANCH, INTERNAL_FILE_DSL, FOLDER_EMPL_IN_GIT_DSL)
    #UpLoad_LPG(ACCESS_TOKEN, GITHUB_REPO, GIT_BRANCH, INTERNAL_FILE_LPG, FOLDER_EMPL_IN_GIT_LPG)
    #UpLoad_98(ACCESS_TOKEN, GITHUB_REPO, GIT_BRANCH, INTERNAL_FILE_98, FOLDER_EMPL_IN_GIT_98)
    print('completed')
    scheduler()
print ('started')

RUN()



print ('finished')
