url = f"https://covidlive.com.au"
urlact = f"https://covidlive.com.au/act"
urlwa = f"https://covidlive.com.au/wa"
urlvic = f"https://covidlive.com.au/vic"
urlqld = f"https://covidlive.com.au/qld"
urlnt = f"https://covidlive.com.au/nt"
urltas = f"https://covidlive.com.au/tas"
urlsa= f"https://covidlive.com.au/sa"
urlnsw = f"https://covidlive.com.au/nsw"

from subprocess import call
#from collections import Mapping
#from collections.abc import Mapping
import pyrebase
import time
from requests_html import HTMLSession
session = HTMLSession()

config1 = {
        # define a dictionary named config with several key-value pairs that configure the connection to the database.
        "apiKey": "AIzaSyDAcpymn2JYEGfYBNEmEOxIkRw4nZiQ24s",
        "authDomain": "minermonitor-9ae44-default-rtdb.firebaseapp.com",
        "databaseURL": "https://minermonitor-9ae44-default-rtdb.firebaseio.com/",
        "storageBucket": "COVID.appspot.com"
        #"measurementID": "$user_id"
    }

firebase1 = pyrebase.initialize_app(config1)

def state():
    r = session.get(url).html
    css = r.find('table.CASES',first=True).text.split()
    
    if css[css.index('NSW')] == 'NSW':
        state1 = "NSW"
        state1cases = css[css.index('NSW') + 1]
        state1cases = state1cases.replace(',','')
        state1new = css[css.index('NSW') + 2]
        state1new = state1new.replace(',','')
    else:
        state1 = "NSW"
        state1cases = "-"
        state1new = "-"

    if css[css.index('Victoria')] == 'Victoria':
        state2 = "Victoria"
        state2cases = css[css.index('Victoria') + 1]
        state2cases = state2cases.replace(',','')
        state2new = css[css.index('Victoria') + 2]
        state2new = state2new.replace(',','')
    else:
        state2 = "Victoria"
        state2cases = "-"
        state2new = "-"
        
    if css[css.index('Queensland')] == 'Queensland':
        state3 = "Queensland"
        state3cases = css[css.index('Queensland') + 1]
        state3cases = state3cases.replace(',','')
        state3new = css[css.index('Queensland') + 2]
        state3new = state3new.replace(',','')
    else:
        state3 = "Queensland"
        state3cases = "-"
        state3new = "-"
        
    if css[css.index('SA')] == 'SA':
        state4 = "SA"
        state4cases = css[css.index('SA') + 1]
        state4cases = state4cases.replace(',','')
        state4new = css[css.index('SA') + 2]
        state4new = state4new.replace(',','')
    else:
        state4 = "SA"
        state4cases = "-"
        state4new = "-"
        
    if css[css.index('ACT')] == 'ACT':
        state5 = "ACT"
        state5cases = css[css.index('ACT') + 1]
        state5cases = state5cases.replace(',','')
        state5new = css[css.index('ACT') + 2]
        state5new = state5new.replace(',','')
    else:
        state5 = "ACT"
        state5cases = "-"
        state5new = "-"
        
    if css[css.index('Tasmania')] == 'Tasmania':
        state6 = "Tasmania"
        state6cases = css[css.index('Tasmania') + 1]
        state6cases = state6cases.replace(',','')
        state6new = css[css.index('Tasmania') + 2]
        state6new = state6new.replace(',','')
    else:
        state6 = "Tasmania"
        state6cases = "-"
        state6new = "-"
        
    if css[css.index('NT')] == 'NT':
        state7 = "NT"
        state7cases = css[css.index('NT') + 1]
        state7cases = state7cases.replace(',','')
        state7new = css[css.index('NT') + 2]
        state7new = state7new.replace(',','')
    else:
        state7 = "NT"
        state7cases = "-"
        state7new = "-"
        
    if css[css.index('WA')] == 'WA':
        state8 = "WA"
        state8cases = css[css.index('WA') + 1]
        state8cases = state8cases.replace(',','')
        state8new = css[css.index('WA') + 2]
        state8new = state8new.replace(',','')
    else:
        state8 = "WA"
        state8cases = "-"
        state8new = "-"
        
    if css[css.index('Australia')] == 'Australia':
        australiacases = css[css.index('Australia') + 1]
        australiacases = australiacases.replace(',','')
        australianew = css[css.index('Australia') + 2]
        australianew = australianew.replace(',','')
    else:
        australiancases = "-"
        australianew = "-"
    
    database = firebase1.database()  # tak$
    CovidUpdate = database.child("COVID")
    time.sleep(2)
    CovidUpdate.child("state1").set(state1)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state1new").set(state1new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state1cases").set(state1cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state2").set(state2)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state2cases").set(state2cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state2new").set(state2new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state3").set(state3)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state3cases").set(state3cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state3new").set(state3new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state4").set(state4)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state4cases").set(state4cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state4new").set(state4new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state5").set(state5)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state5cases").set(state5cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state5new").set(state5new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state6").set(state6)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state6cases").set(state6cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state6new").set(state6new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state7").set(state7)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state7cases").set(state7cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state7new").set(state7new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state8").set(state8)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state8cases").set(state8cases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("state8new").set(state8new)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("australiacases").set(australiacases)
    database = firebase1.database()
    CovidUpdate.child("COVID").child("australianew").set(australianew)



    #first = r.find('td.VACCINATIONS',first=True).text.split()
    #firstdose = first [0]
    second = r.find('td.MA',first=True).text.split()
    seconddose = second [0]
    ICU = r.find('td.ICU',first=True).text.split()
    ICU = ICU[0]    
    database = firebase1.database()  # tak$
    CovidUpdate = database.child("COVID")
  
    CovidUpdate.child("COVID").child("ICU").set(ICU)
    #time.sleep(10)
    print("state")
    NSW()

def NSW():
    r = session.get(urlnsw).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        
    if css[css.index('Doses')] == 'Doses':
        TotalDoses = css[css.index('Doses') + 1]
        TotalDoses = TotalDoses.replace(',','')
        NewDoses = css[css.index('Doses') + 2]
        NewDoses = NewDoses.replace(',','')
    else:
        TotalDoses = ("-")
        NewDoses = ("-")
        
  
    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")


    
        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
#         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("NSW")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("NewCases").set(NewCases)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("TotalDoses").set(TotalDoses)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("NewDoses").set(NewCases)
    database = firebase1.database()
  
    CovidUpdate.child("NSW").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("NSW").child("NewActive").set(NewActive)
    database = firebase1.database()
#    CovidUpdate.child("NSW").child("firstdose").set(firstdose)
#    database = firebase1.database()
#    CovidUpdate.child("NSW").child("seconddose").set(seconddose)
#     database = firebase1.database()
#     CovidUpdate.child("NSW").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("NSW").child("recnew").set(recnew)
    print("NSW")
    VIC()
    
def VIC():

    r = session.get(urlvic).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        
#    if css[css.index('Doses')] == 'Doses':
#        TotalDoses = css[css.index('Doses') + 1]
#        TotalDoses = TotalDoses.replace(',','')
#        NewDoses = css[css.index('Doses') + 2]
#        NewDoses = NewDoses.replace(',','')
#   else:
#        TotalDoses = ("-")
#        NewDoses = ("-")
        
#    if css[css.index('Tests')] == 'Tests':
#        TotalTests = css[css.index('Tests') + 1]
#        TotalTests = TotalTests.replace(',','')
#        NewTests = css[css.index('Tests') + 2]
#        NewTests = NewTests.replace(',','')
#    else:
#        TotalTests = ("-")
#        NewTests = ("-")
    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")


#    first = r.find('td.VACCINATIONS',first=True).text.split()
#    if first >= ['']:
#        firstdose = first [0]
#        second = r.find('td.MA',first=True).text.split()
#       seconddose = second [0]

#    else:
#        firstdose = ("-")
#        seconddose = ("-")
        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
# #         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("VIC")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("NewCases").set(NewCases)
    database = firebase1.database()
#    CovidUpdate.child("VIC").child("TotalDoses").set(TotalDoses)
#    database = firebase1.database()
    CovidUpdate.child("VIC").child("NewDoses").set(NewCases)
    database = firebase1.database()
#    CovidUpdate.child("VIC").child("TotalTests").set(TotalTests)
#    database = firebase1.database()
#    CovidUpdate.child("VIC").child("NewTests").set(NewTests)
#    database = firebase1.database()
    CovidUpdate.child("VIC").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("VIC").child("NewActive").set(NewActive)
    database = firebase1.database()
#    CovidUpdate.child("VIC").child("firstdose").set(firstdose)
#    database = firebase1.database()
#    CovidUpdate.child("VIC").child("seconddose").set(seconddose)
#     database = firebase1.database()
#     CovidUpdate.child("VIC").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("VIC").child("recnew").set(recnew)
    print("VIC")
    TAS()

def TAS():

    r = session.get(urltas).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        

    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")


        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
# #         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("TAS")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("NewCases").set(NewCases)
    database = firebase1.database()

    CovidUpdate.child("TAS").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("TAS").child("NewActive").set(NewActive)
    database = firebase1.database()

#     CovidUpdate.child("TAS").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("TAS").child("recnew").set(recnew)
    print("TAS")
    SA()
    
def SA():    
        
    r = session.get(urlsa).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        

    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")



        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
#         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("SA")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("SA").child("NewCases").set(NewCases)
    database = firebase1.database()

    CovidUpdate.child("SA").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("SA").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("SA").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("SA").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("SA").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("SA").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("SA").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("SA").child("NewActive").set(NewActive)
    database = firebase1.database()

#     CovidUpdate.child("SA").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("SA").child("recnew").set(recnew)
    print("SA")
    ACT()
    
def ACT():

    r = session.get(urlact).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")

    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")



        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
#         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("ACT")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("NewCases").set(NewCases)
    database = firebase1.database()

    CovidUpdate.child("ACT").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("ACT").child("NewActive").set(NewActive)
  
#     CovidUpdate.child("ACT").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("ACT").child("recnew").set(recnew)
    print("ACT")
    QUEEN()

def QUEEN():
    
    r = session.get(urlqld).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        

    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")



        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
#         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("QLD")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("NewCases").set(NewCases)
    database = firebase1.database()

    CovidUpdate.child("QLD").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("QLD").child("NewActive").set(NewActive)
    database = firebase1.database()
 
#     CovidUpdate.child("QLD").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("QLD").child("recnew").set(recnew)
    print("QLD")
    NT()
  
def NT():
    
    r = session.get(urlnt).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        

    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")



        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
#         recnew = recnew.replace(',','')
# 
#     else:
#         rectotal = ("-")
#         recnew = ("-")

    database = firebase1.database()
    CovidUpdate = database.child("NT")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("NT").child("NewCases").set(NewCases)
    database = firebase1.database()

    CovidUpdate.child("NT").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("NT").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("NT").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("NT").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("NT").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("NT").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("NT").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("NT").child("NewActive").set(NewActive)
    database = firebase1.database()

#     CovidUpdate.child("NT").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("NT").child("recnew").set(recnew)
    print("NT")
    WA()
    
def WA():
    
    r = session.get(urlwa).html
    css = r.find('table.DAILY-SUMMARY',first=True).text.split()
    
    if css[css.index('Cases')] == 'Cases':
        TotalCases = css[css.index('Cases') + 1]
        TotalCases = TotalCases.replace(',','')
        NewCases = css[css.index('Cases') + 2]
        NewCases = NewCases.replace(',','')
    else:
        Totalcases = ("-")
        NewCases = ("-")
        

    
    if css[css.index('Hospitalised')] == 'Hospitalised':
        TotalHosp = css[css.index('Hospitalised') + 1]
        TotalHosp = TotalHosp.replace(',','')
        NewHosp = css[css.index('Hospitalised') + 2]
        NewHosp = NewHosp.replace(',','')
    else:
        TotalHosp = ("-")
        NewHosp = ("-")

    if css[css.index('ICU')] == 'ICU':
        TotalICU = css[css.index('ICU') + 1]
        TotalICU = TotalICU.replace(',','')
        NewICU = css[css.index('ICU') + 2]
        NewICU = NewICU.replace(',','')
    else:
        TotalICU = ("-")
        NewICU = ("-")

    if css[css.index('Deaths')] == 'Deaths':
        TotalDeaths = css[css.index('Deaths') + 1]
        TotalDeaths = TotalDeaths.replace(',','')
        NewDeaths = css[css.index('Deaths') + 2]
        NewDeaths = NewDeaths.replace(',','')
    else:
        TotalDeaths = ("-")
        NewDeaths = ("-")
        
    if css[css.index('Active')] == 'Active':
        TotalActive = css[css.index('Active') + 1]
        TotalActive = TotalActive.replace(',','')
        NewActive = css[css.index('Active') + 2]
        NewActive = NewActive.replace(',','')
    else:
        TotalActive = ("-")
        NewActive = ("-")


        
#     rec = r.find('table.DAILY-RECOVERIES',first=True).text.split()
#     
#     if first >= ['']:
#         rectotal = rec [7]
#         rectotal = rectotal.replace(',','')
#         recnew = rec [8]
#         recnew = recnew.replace(',','')

#     else:
#         rectotal = ("-")
#         recnew = ("-")
    
    database = firebase1.database()
    CovidUpdate = database.child("WA")
    CovidUpdate.child("TotalCases").set(TotalCases)
    database = firebase1.database()
    CovidUpdate.child("WA").child("NewCases").set(NewCases)
    database = firebase1.database()

    CovidUpdate.child("WA").child("TotalHosp").set(TotalHosp)
    database = firebase1.database()
    CovidUpdate.child("WA").child("NewHosp").set(NewHosp)
    database = firebase1.database()
    CovidUpdate.child("WA").child("TotalICU").set(TotalICU)
    database = firebase1.database()
    CovidUpdate.child("WA").child("NewICU").set(NewICU)
    database = firebase1.database()
    CovidUpdate.child("WA").child("TotalDeaths").set(TotalDeaths)
    database = firebase1.database()
    CovidUpdate.child("WA").child("NewDeaths").set(NewDeaths)
    database = firebase1.database()
    CovidUpdate.child("WA").child("TotalActive").set(TotalActive)
    database = firebase1.database()
    CovidUpdate.child("WA").child("NewActive").set(NewActive)
    database = firebase1.database()

#     CovidUpdate.child("WA").child("rectotal").set(rectotal)
#     database = firebase1.database()
#     CovidUpdate.child("WA").child("recnew").set(recnew)
    print("WA")
    time.sleep(20)
    #run = run + 1
    print("finished")
    #return run,
    scheduler()
    #state()
    #NT()

def scheduler():
    import datetime
    #import time
    #from subprocess import call
    #import sys
    #print(sys.getrecursionlimit())
    
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    #print (f'The time of the day:   {hour}:{minute}')
    
    if hour == 6 and minute == 0:
        time.sleep(20)
        print("run1")
        state()

    elif hour == 7 and minute == 0 :
        time.sleep(20)
        print("run2")
        state()

    elif hour == 8 and minute == 0 :
        time.sleep(20)
        print("run3")
        state()
        
    elif hour == 9 and minute == 0 :
        time.sleep(20)
        print("run4")
        state()
        
    elif hour == 10 and minute == 0 :
        time.sleep(20)
        state()
        
    elif hour == 11 and minute == 0 :
        time.sleep(20)
        state()
        
    elif hour == 12 and minute == 0 :
        time.sleep(20)
        state()
        
    elif hour == 13 and minute == 0 :
        time.sleep(20)
        state()
        
    elif hour == 14 and minute == 0 :
        time.sleep(20)
        state()
        
    elif hour == 15 and minute == 0 :
        time.sleep(20)
        state()
        
    elif hour == 16 and minute == 0 :
        time.sleep(20)
        state()    

    else:
        time.sleep(20)
        scheduler()
        
print("started")

#WA()
import sys
sys.setrecursionlimit(10000)
#scheduler()    #//use for presert scan /update times
#print ("cont")
state()
#print (firstdose)# = csss[2]
#print (secondose)# = csss[3]
# = csss[4]
#print (csss)
#print ("Western Australia")
#print (f"new: {new}")
#print (f"total: {total}")
