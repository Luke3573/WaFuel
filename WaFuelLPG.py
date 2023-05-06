from bs4 import BeautifulSoup
import urllib.request
import re
import xlsxwriter
import random

workbook = xlsxwriter.Workbook('c:\\WaFuelLPG.xlsx')
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
#soup.replace(",", " ")

pattern=re.compile(r'sitename[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
no_of_words=2
print('started')

for elem in soup(text=pattern):
#    text = re.sub(",", " ",)
#    print("test3")
    str=elem.parent.text
    str=str.replace(':', "")
    str=str.replace(' ', "_")
    str=str.replace('"', " ")
    str=str.replace(',', " ")
    str=str.replace('"''"', " ")
#    print(str)
    list=str.split(' ')
#    list.sub(':', "TCE")
#    print('test')
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
#    text = re.sub(",", " ",)
#    print("test3")
    str=elem.parent.text
    str=str.replace(':', "")
    str=str.replace(' ', "_")
    str=str.replace('"', " ")
    str=str.replace(',', " ")
    str=str.replace('"''"', " ")
#    print(str)
    list=str.split(' ')
#    list.sub(':', "TCE")
#    print(list)
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
#        print(' '.join(list[start:end]).strip()) #end will not affect o/p if > len(list)
#        print("List of Word Before: ",list[start:index])# words before
#        print("List of Words After: ",list[index+2:end])#word after
        
pattern2=re.compile(r'location[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
no_of_words2=2

for elem in soup(text=pattern2):
#    text = re.sub(",", " ",)
#    print("test3")
    str=elem.parent.text
    str=str.replace(':', "")
    str=str.replace(' ', "_")
    str=str.replace('"', " ")
    str=str.replace(',', " ")
    str=str.replace('"''"', " ")
#    print(str)
    list=str.split(' ')
#    list.sub(':', "TCE")
#    print(list)
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
#        print(' '.join(list[start:end]).strip()) #end will not affect o/p if > len(list)
#        print("List of Word Before: ",list[start:index])# words before
#        print("List of Words After: ",list[index+2:end])#word after
        
pattern3=re.compile(r'postCode[\.,|" ]',re.IGNORECASE)#'Risk', 'risk.', 'risk'  but NOT 'risky'
no_of_words3=1

for elem in soup(text=pattern3):
#    text = re.sub(",", " ",)
#    print("test3")
    str=elem.parent.text
    str=str.replace(':', "")
    str=str.replace(' ', "_")
    str=str.replace('"', " ")
    str=str.replace(',', " ")
    str=str.replace('"''"', " ")
#    print(str)
    list=str.split(' ')
#    list.sub(':', "TCE")
#    print(list)
    row = 1
    list_indices=[i for i,x in enumerate(list) if re.match(pattern3,x.strip()+' ')]# +' ' to conform with our pattern
    for index in list_indices:
        start=index-no_of_words3
        end=index+no_of_words3+1
        if start<0:
            start=0
        data = (list[index+1:end])
#        print(data)
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
for elem in soup(text=pattern2):
#    text = re.sub(",", " ",)
#    print("test3")
    str=elem.parent.text
    str=str.replace(':', "")
    str=str.replace(' ', "_")
    str=str.replace('"', " ")
    str=str.replace(',', " ")
    str=str.replace('"''"', " ")
#    print(str)
    list=str.split(' ')
#    list.sub(':', "TCE")
#    print(list)
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
#        print(' '.join(list[start:end]).strip()) #end will not affect o/p if > len(list)
#        print("List of Word Before: ",list[start:index])# words before
#        print("List of Words After: ",list[index+2:end])#word after

#tester------------------------------------------------------------------------------------------------

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
#        print(data)
        if word1 in data:
#            print('true')
            data = data[7]
#            print(data)
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
#        print(data)
        if word1 in data:
            
            if word1 in data:
#                print('true')
                data = data[10]
#                print(data)
                data=data.replace('_', " ")
                worksheet.write_string(row, col5, data)
                row += 1
            else:
                worksheet.write_string(row, col5, 'N/A')
                row += 1
                
        elif word2 in data:
#            print('true')
            data = data[7]
#            print(data)
            data=data.replace('_', " ")
            worksheet.write_string(row, col5, data)
            row += 1   
            
        else:
            worksheet.write_string(row, col5, 'N/A')
            row += 1
print('finish')        

#tester---------------------------------------------------------------------------------------------------------       
        
        
        
         
workbook.close()
