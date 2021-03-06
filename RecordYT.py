from time import sleep
from selenium import webdriver
from datetime import datetime


def evaluatetonum(string):
    retstr = ""
    for i in string:
        if i.isnumeric():
            retstr += i
    return retstr



currdate = datetime.now()
print(str(currdate))
browser = webdriver.Edge(executable_path=r'<PATH of WebDriver>') # Modify Path accordingly
browser.get('https://www.youtube.com/watch?v=GODAlxW5Pes')  # Modify Path Accordingly
browser.set_page_load_timeout(240)
browser.maximize_window()
sleep(10)                           #Let the Window load up properly



viewcount = 0


#  This Section helps in case of failure by maintaing datapoints as CSVs--------------------------------------
# when running for first time ensure slnrecord.txt has the int64 value 0 only
# Also this section sometimes causes notorious errors
storeslnr = open('slnrecord.txt', 'r')
sln = int(storeslnr.read())
storeslnr.close()
storeslnw = open('slnrecord.txt', 'w')
#--------------------------------------------------------------------------------------------------------------


# This Section is supposed to run for a very Long Time(approx. 150+ Hours)-----------------------------------------------
while True:
    sln += 1
    for elem in browser.find_elements_by_xpath('.//span[@class = "view-count style-scope yt-view-count-renderer"]'):
        viewcount = elem.text
        print(viewcount)
    for elem in browser.find_elements_by_css_selector('h1.title yt-formatted-string'):
        title = elem.text
        print(title)
    datepublished = browser.find_element_by_id("date").text
    print(datepublished)
    viewcount = int(evaluatetonum(viewcount))
    mathstring = str(str(sln) + "," + str(viewcount) + "\n")
    plotFile = open('plotFile', 'a')
    File_object = open('Dil Bechara.txt', "a")
    writestring = "Time Now is: " + str(
        currdate) + " and Views till Now are " + str(viewcount) + " views since it was " + datepublished + "\n"
    File_object.write(writestring)
    plotFile.write(mathstring)
    plotFile.close()
    storeslnw.write(str(sln))
    File_object.close()
    # Something Causes the execution to be stuck somewhere above this line and browser never refreshes.
    # Use Ctrl+C in such case
    browser.refresh()
    sleep(15)
#---------------------------------------------------------------------------------------------------------------------------



storeslnw.close()
