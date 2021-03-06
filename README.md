# Project End Planner (Python3)
***
### The program has two versions: for shell and Jupyter Notebook: read instructions get more info about how to use them
***
### What is this project about?
It's about predicting the end date of the project based on some conditions:
* You have a start date of your project
* You have some front-end and back-end developers
* You have some front-end and back-end tasks that should be done
* All tasks can be done at the same time
* Developers work 8 hours per day and only from Monday to Friday. Of course, they don't work on public holidays.

**You just input the required data - and get the result (shell version):**

![image #1](/images/1.png)

**or (Jupyter version):**

![gif #1](/images/screen.gif)
***
### How to (for *nix systems):
1. **Install**
    * `git clone https://github.com/itiievskyi/Project-End-Python3.git ~/project-end/`
    * `cd ~/project-end/`
    * `pip3 install -r requirements.txt` (for shell version)
    * `pip3 install -r requirements-jupyter.txt` (for Jupyter version)

2. **Use**
    * Shell version:
        * `python3 project_end.py`
        * Answer the questions and use on-screen instructions for navigating
    * Jupyter version:
        * `jupyter notebook Project-End.ipynb` or
        * `jupyter notebook` and open **Project-End.ipynb** through the Jupyter Notebook menu (for Jupyter version)
        ![image #4](/images/4.png)
        * Go to **Cell** -> **Run All** and scroll to the bottom of the page
        * Adjust parameteres to get the result you need
***
### Main questions
   * **Starting date of project** - type the date when you're going to start the project (or when it started). Use only `YYYY-MM-DD` notation so if the projects starts on January, 20th 2019, type 2019-01-20. This date will be the first day when developers work on project (in case if it's not a holiday and doesn't fall on weekend).
   * **Number of front-end developers** - the number of developers that will work on this project (assuming that nobody will leave or meet the team).
   * **Hours required for front-end tasks** - estimated amount of hours required in order to finish all front-end tasks. This number should represent the overall hours (regardless of the number of developers).
   * **Number of back-end developers** , **Hours required for back-end tasks** - see the previos instructions.
   * **Select a country where the company operates** - use the arrow keys and Enter to choose the country for which public holidays should be found. Look at the table below to see the full list of supported countries. 
***
### Choosing a province or state
Depend on country you have chosen the program can also propose you to choose a state or province.
![image #2](/images/2.png)
If you pressed 'Y' but no longer want to choose, just pick the '-NONE-' to pass a default value to the main algorithm. Default value may be either the exact province or the whole country without special regional holidays. Look at the table below to see the full list of supported provinces.
***
### Holiday observation
In many countries, if the holiday falls on weekend, it will observe the next working day (it's usually Monday). But if you don't want to use this option (maybe your corporate rules provide another rule for this case) just type 'n' when the question about observation (*'Should holidays falling on weekend observe the next working day?'*) appears.
***
## Developer notes

### What technologies or libraries does this project use?
In the core of the project are:
* Python 3
* [Holidays](https://pypi.org/project/holidays/) package
* [Questionary](https://github.com/tmbo/questionary) package for shell version
* [Jupyter Notebook](https://jupyter.org/index.html) environment for Jupyter version
* [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/index.html) package for Jupyter version
***
### Why using package instead of API?
I discovered a few popular APIs for getting national holidays and found the next problems with them:
* All extended functions are available only in paid plans
* Some of APIs have request limits (per day, per month, etc.) or give access only to historical data
* The most of them have a gaps on national holidays schedule (for example, [CalendarIndex](https://www.calendarindex.com/) doesn't provide information about catholic Christmass in Ukraine despite the fact that it was already celebrated twice here).
* Some APIs (for example, [HolidayApi](https://holidayapi.com/)) allow only simple requests and their Python libraries are no longer updated.

[Holidays](https://pypi.org/project/holidays/) package is permanently developing and provides an information about holidays in bunch of countries and provinces:

Country            |Abbr    |Provinces/States Available
-------------------|--------|-------------------------------------------------------------
Argentina          |AR      |None
Australia          |AU      |prov = **ACT** (default), NSW, NT, QLD, SA, TAS, VIC, WA
Austria            |AT      |prov = B, K, N, O, S, ST, T, V, **W** (default)
Belarus            |BY      |None
Belgium            |BE      |None
Brazil             |BR      |state = AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG,PA, PB, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO
Canada             |CA      |prov = AB, BC, MB, NB, NL, NS, NT, NU, **ON** (default), PE, QC, SK, YU
Colombia           |CO      |None
Croatia            |HR      |None
Czech              |CZ      |None
Denmark            |DK      |None
England            |        |None
Finland            |FI      |None
France             |FRA     |prov = **Métropole** (default), Alsace-Moselle, Guadeloupe, Guyane, Martinique, Mayotte, Nouvelle-Calédonie, La Réunion, Polynésie Française, Saint-Barthélémy, Saint-Martin, Wallis-et-Futuna
Germany            |DE      |prov = BW, BY, BE, BB, HB, HH, HE, MV, NI, NW, RP, SL, SN, ST, SH, TH
Hungary            |HU      |None
India              |IND     |prov = AS, SK, CG, KA, GJ, BR, RJ, OD, TN, AP, WB, KL, HR, MH, MP, UP, UK, TN
Ireland            |IE      |None
Isle of Man        |        |None
Italy              |IT      |prov = MI, RM
Japan              |JP      |None
Mexico             |MX      |None
Netherlands        |NL      |None
New Zealand        |NZ      |prov = NTL, AUK, TKI, HKB, WGN, MBH, NSN, CAN, STC, WTL, OTA, STL, CIT
Northern Ireland   |        |None
Norway             |NO      |None
Polish             |PL      |None
Portugal           |PT      |None
Portugal Ext       |PTE     |*Portugal plus extended days most people have off*
Scotland           |        |None
Slovenia           |SI      |None
Slovakia           |SK      |None
South Africa       |ZA      |None
Spain              |ES      |prov = AND, ARG, AST, CAN, CAM, CAL, CAT, CVA, EXT, GAL, IBA, ICA, MAD, MUR, NAV, PVA, RIO
Sweden             |SE      |None
Switzerland        |CH      |prov = AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
Ukraine            |UA      |None
United Kingdom     |UK      |None
United States      |US      |state = AL, AK, AS, AZ, AR, CA, CO, CT, DE, DC, FL, GA, GU, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MH, MA, MI, FM, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, MP, OH, OK, OR, PW, PA, PR, RI, SC, SD, TN, TX, UT, VT, VA, VI, WA, WV, WI, WY
Wales              |        |None
***
### Interface
To provide a dialog with the user I implemented nice CLI library for shell version: [Questionary](https://github.com/tmbo/questionary).
It allows to use different types of questions ('text', 'confirm', 'checkbox', etc.) and returns inputted data.
It's very similar to [PyInquirer](https://github.com/CITGuru/PyInquirer/) library but uses the latest version of promt-toolkit (I have 2.0.7) while PyInquirer now can work only with 1.0.1x versions. Using PyInquirer could cause some problems with another software like Jupyter that also uses the latest promt-toolkit staff. 

The Jupyter version uses Jupyter notebook environment instead and provides interacting via **ipywidgets** library.
***
### Error management
The program uses a try/except system to catch the most part of possible errors (they usually occur during input).
![Error management](/images/3.png)
***
### Code style
The code (*project_end.py*) is written according to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) and checked using [Pylint](https://www.pylint.org/).
***
### Enjoy!
