from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import re

options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

#driver = webdriver.Firefox()

driver.get('https://kusis.ku.edu.tr/psp/ps/?cmd=login&languageCd=ENG&')
driver.find_element_by_name('userid').send_keys('KUSIS_USERNAME_HERE')
driver.find_element_by_name('pwd').send_keys('KUSIS_PASSWORD_HERE')
driver.find_element_by_name('Submit').click()

driver.get('https://kusis.ku.edu.tr/psp/ps/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_MY_CRSEHIST.GBL?PORTALPARAM_PTCNAV=HC_SSS_MY_CRSEHIST_GBL&EOPP.SCNode=SA&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=HCCC_ACADEMIC_RECORDS&EOPP.SCLabel=Academic%20Records&EOPP.SCPTfname=HCCC_ACADEMIC_RECORDS&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ACADEMIC_RECORDS.HC_SSS_MY_CRSEHIST_GBL&IsFolder=false')
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

src= driver.page_source

soup = BeautifulSoup(src, 'html.parser')

course_names= [item.contents[0] for item in soup.find_all('span', id=lambda x: x and x.startswith('CRSE_NAME'))]

terms= [item.contents[0] for item in soup.find_all('span', id=lambda x: x and x.startswith('CRSE_TERM'))]

grades= [item.contents[0] for item in soup.find_all('span', id=lambda x: x and x.startswith('CRSE_GRADE'))]

units= [item.contents[0] for item in soup.find_all('span', id=lambda x: x and x.startswith('CRSE_UNITS'))]

included_in_gpa= [item.contents[0] for item in soup.find_all('span', id=lambda x: x and x.startswith('KU_AH_DERIVED_INCLUDE_IN_GPA'))]


combined_list =[ [course_names[i],  terms[i], grades[i], units[i], included_in_gpa[i]] for i in range(len(course_names))]


print(combined_list)


