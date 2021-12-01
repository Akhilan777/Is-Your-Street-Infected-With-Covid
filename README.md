# CS50 FINAL PROJET - Is Your Street Infected With COVID
#### Video Demo:  [click here](https://www.youtube.com/watch?v=61eTFPU3TN0)
#### Description:
The project is a command line run python program. The implementation is simple.
I wanted to create a project like this so I can increase my knowledge in python and also use python libraries.

**Technologies used:**

1. Python
2. requests (python module)
3. Beautiful Soup
4. lxml

**How does the program work?:**

This program gets an area name in Chennai as a command line argument.
If the area name is not in Chennai then the program will not output anything.

The url's which show the details of the streets which have covid cases are included in the program.
```urls = ["http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=1",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=3",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=4",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=2",
        "http://covid19.chennaicorporation.gov.in/covid/positivecases/index_det.jsp?RptID=5"]
```

raise for status function is used to check whether the url is opened or if there are any errors like 404 etc.
```res = requests.get(url)
    res.raise_for_status()
```

Beautiful Soup is used to parse and extract the data from those urls.
For beautiful soup lxml parser is used.
```soup = bs4.BeautifulSoup(res.text, "lxml")```


The find all function is used to find all the table tags.
Inside the first table find all function is again used to find all the tr tags.
```table = soup.find_all("table")
    trs = table[0].find_all('tr')
```
.contents is used to get the data inside the tags.
```print(f"{trs[i].contents[11].contents[0]} has {trs[i].contents[13].contents[0]} cases")```

The program checks all those urls with the help of python libraries and give the street names and the
no of cases in those streets as output.

***To do this first the website's source code was looked upon and the structure was noted.***
***If the urls are changed or if the website's source code is changed then the program may not work properly.***

**Possible Improvements:**

1. The program can be extended to be used in other cities are places as well.
2. A webapp can be created which gets their location using IP address and display the results in a map.
3. The webapp can also have accounts which can notified via e-mail if their street has a covid case.
4. It can be implemented as an Android or ios App.

**How to run the program:**

1. ***Check that you have Python, bs4, requests and lxml parser.***
2. Make sure you have an internet connection.
3. In command prompt run the program as "python isyourstreetinfectcovid.py area_name" without the quotes and the
   name of your area in the place "area_name".
4. The program will output the street name and the number of cases in those streets.

**Documentation:**

1. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [requests](https://docs.python-requests.org/en/latest/)
