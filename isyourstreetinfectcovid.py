# isyourstreetinfectcovid.py - gives the infected street lists(of covid) of your area in chennai
# Usage : python isyourstreetinfectcovid.py area

import sys
import requests
import bs4

area = []
# get street name from user as command line argument

if len(sys.argv) == 2:
    area.append(sys.argv[1:][0].upper())

else:
    print("Usage : python isyourstreetinfectcovid.py street name")

# for each category open the url in chennai corporation website
urls = ["http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=1",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=3",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=4",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=2",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=5"]

for url in urls:
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")

    table = soup.find_all("table")
    trs = table[0].find_all('tr')

    if(len(trs) == 2):
        continue
    for i in range(len(trs)):
        # in each row .contents returns a list
        if area[0] in trs[i].contents[7].contents[0].split()[0].upper():
            # 7 is area 9 is locality 11 is street name and 13 is no of cases
            print(f"{trs[i].contents[11].contents[0]} has {trs[i].contents[13].contents[0]} cases")