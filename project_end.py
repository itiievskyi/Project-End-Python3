'''
Program that estimates the end date of the project based on input data
'''

# Standard libraries
from time import strptime
import datetime

# Side libraries
import questionary
import holidays

# Initializing country list that contains all countries supported by 'holidays'
COUNTRIES = ['Argentina', 'Australia', 'Austria', 'Belarus',
             'Belgium', 'Brazil', 'Canada', 'Colombia', 'Croatia', 'Czech',
             'Denmark', 'England', 'Finland', 'France', 'Germany', 'Hungary',
             'India', 'Ireland', 'Isle of Man', 'Italy', 'Japan', 'Mexico',
             'Netherlands', 'NewZealand', 'Northern Ireland', 'Norway',
             'Polish', 'Portugal', 'Portugal Ext', 'Scotland', 'Slovenia',
             'Slovakia', 'South Africa', 'Spain', 'Sweden', 'Switzerland',
             'Ukraine', 'United Kingdom', 'United States', 'Wales']

PROVINCES = {
    'Australia':['ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA'],
    'Austria':['B', 'K', 'N', 'O', 'S', 'ST', 'T', 'V', 'W'],
    'Brazil':['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT',
              'MS', 'MG', 'PA', 'PB', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR',
              'SC', 'SP', 'SE', 'TO'],
    'Canada':['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC',
              'SK', 'YU'],
    'France':['Métropole', 'Alsace-Moselle', 'Guadeloupe', 'Guyane',
              'Martinique', 'Mayotte', 'Nouvelle-Calédonie', 'La Réunion',
              'Polynésie Française', 'Saint-Barthélémy', 'Saint-Martin',
              'Wallis-et-Futuna'],
    'Germany':['BW', 'BY', 'BE', 'BB', 'HB', 'HH', 'HE', 'MV', 'NI', 'NW', 'RP',
               'SL', 'SN', 'ST', 'SH', 'TH'],
    'India':['AS', 'SK', 'CG', 'KA', 'GJ', 'BR', 'RJ', 'OD', 'TN', 'AP', 'WB',
             'KL', 'HR', 'MH', 'MP', 'UP', 'UK', 'TN'],
    'Italy':['MI', 'RM'],
    'NewZealand':['NTL', 'AUK', 'TKI', 'HKB', 'WGN', 'MBH', 'NSN', 'CAN', 'STC',
                  'WTL', 'OTA', 'STL', 'CIT'],
    'Spain':['AND', 'ARG', 'AST', 'CAN', 'CAM', 'CAL', 'CAT', 'CVA', 'EXT',
             'GAL', 'IBA', 'ICA', 'MAD', 'MUR', 'NAV', 'PVA', 'RIO'],
    'Switzerland':['AG', 'AR', 'AI', 'BL', 'BS', 'BE', 'FR', 'GE', 'GL', 'GR',
                   'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SZ', 'SO', 'TG',
                   'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH'],
    'UnitedStates':['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
                    'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
                    'LA', 'ME', 'MD', 'MH', 'MA', 'MI', 'FM', 'MN', 'MS', 'MO',
                    'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP',
                    'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN',
                    'TX', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']
}

def calculate_project_duration(fe_devs, fe_task, be_devs, be_task):
    '''
    Returns the number of days required to complete all tasks
    '''
    fe_hours = 0
    be_hours = 0
    # Calculating required number of hours for both front-end and back-end tasks
    try:
        if fe_task > 0:
            fe_hours = fe_task / fe_devs
        if be_task > 0:
            be_hours = be_task / be_devs
    except ZeroDivisionError:
        print('It seems like you have no enough developers to finish the task.')
        return -1

    # Calculating the number of days (rounding up without using a 'math')
    max_days = max(fe_hours, be_hours) / 8 + (max(fe_hours, be_hours) % 8 > 0)

    return int(max_days)

def get_holidays(country, state_prov, years):
    '''
    Creates a dictionary that contains all public national holidays for
    specific country, state or province and for period specified in 'years' list
    '''
    state = None
    province = None

    # Defining if there is any state or province specified
    if state_prov != '':
        if country in ['US', 'BR']:
            state = state_prov
        else:
            province = state_prov

    # Sending a request to 'holidays' library API
    holydays_list = getattr(holidays, country)(
        state=state,
        prov=province,
        years=years
    )

    return holydays_list

def get_end_date(start_date, proj_days, holidays_schedule, observe):
    '''
    Calculates the end date of the project based on start date, duration and
    considering that people don't work on weekends and holidays
    '''

    current_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    weekend_days = 0
    holiday_days = 0
    days_to_observe = 0

    if proj_days > 0:

        days_to_add = proj_days

        current_date = datetime.datetime.strptime(start_date, '%Y-%m-%d') \
        - datetime.timedelta(days=1)

        while days_to_add > 0:
            current_date += datetime.timedelta(days=1)
            weekday = current_date.weekday()
            # Checking if the the day falls on weekend
            if weekday >= 5:
                weekend_days += 1
                if observe and current_date in holidays_schedule:
                    holiday_days += 1
                    days_to_observe += 1
                continue
            elif days_to_observe > 0:
                days_to_observe -= 1
                continue
            # Checking if the day doesn't fall on weekend but it's a holiday
            if current_date in holidays_schedule:
                holiday_days += 1
                continue
            days_to_add -= 1

    end_data = {
        'date':current_date.strftime("%Y-%m-%d"),
        'holidays':holiday_days,
        'weekends':weekend_days
    }

    return end_data

def get_start_date():
    '''
    Asks user for the start date
    '''
    while True:
        try:
            start_date = questionary.text(
                'Starting date of project (YYYY-MM-DD):').ask()
            strptime(start_date, '%Y-%m-%d')
            return start_date
        except ValueError:
            print('Error! Invalid date format. Please use YYYY-MM-DD notation.')
            continue
        except TypeError:
            return 'interrupt'

def get_front_end_data():
    '''
    Asks user for number of front-end developers and the amount of work to do
    '''
    front_end_data = {}
    # Getting the number of front-end developers
    while True:
        try:
            front_end_data['fe_devs'] = int(questionary.text(
                'Number of front-end developers:').ask())
            if front_end_data['fe_devs'] < 0:
                print('Error! You can\'t use negative numbers')
                continue
            break
        except ValueError:
            print('Error! Please type a valid number')
            continue
        except TypeError:
            return {-1:-1}

    # Getting the number of working hours required to finish all front-end tasks
    while True:
        try:
            front_end_data['fe_task'] = int(questionary.text(
                'Hours required for front-end tasks:').ask())
            if front_end_data['fe_task'] < 0:
                print('Error! You can\'t use negative numbers')
                continue
            break
        except ValueError:
            print('Error! Please type a valid number')
            continue
        except TypeError:
            return {-1:-1}

    return front_end_data

def get_back_end_data():
    '''
    Asks user for number of back-end developers and the amount of work to do
    '''
    back_end_data = {}
    # Getting the number of back-end developers
    while True:
        try:
            back_end_data['be_devs'] = int(questionary.text(
                'Number of back-end developers:').ask())
            if back_end_data['be_devs'] < 0:
                print('Error! You can\'t use negative numbers')
                continue
            break
        except ValueError:
            print('Error! Please type a valid number')
            continue
        except TypeError:
            return {-1:-1}

    # Getting the number of working hours required to finish all back-end tasks
    while True:
        try:
            back_end_data['be_task'] = int(questionary.text(
                'Hours required for back-end tasks:').ask())
            if back_end_data['be_task'] < 0:
                print('Error! You can\'t use negative numbers')
                continue
            break
        except ValueError:
            print('Error! Please type a valid number')
            continue
        except TypeError:
            return {-1:-1}

    return back_end_data

def get_projects_conditions():
    '''
    Collects the data from user via 'questionary' library and writes it to dict
    '''
    input_data = {}

    # Getting the start date and number of developers / task hours
    input_data['start_date'] = get_start_date()
    if input_data['start_date'] == 'interrupt':
        return -1
    input_data.update(get_front_end_data())
    if -1 in input_data.keys():
        return -1
    input_data.update(get_back_end_data())
    if -1 in input_data.keys():
        return -1

    # GETTING ADDITIONAL INFORMATION

    # Getting the country
    try:
        input_data['country'] = questionary.select(
            'Select a country where the company operates:',
            choices=COUNTRIES
        ).ask().replace(' ', '')
    except AttributeError:
        return -1

    # Checking whether states or provinces are available for selected country
    # and getting the appropriate user choice

    if input_data['country'] in PROVINCES:
        get_province = questionary.confirm(
            'Would you like to specify a state or province for this country?'
        ).ask()

        if get_province:
            input_data['state_prov'] = questionary.select(
                'Select the state or province:',
                choices=(['-NONE-'] + PROVINCES[input_data['country']])
            ).ask()
        else:
            input_data['state_prov'] = ''
    else:
        input_data['state_prov'] = ''

    # Asking user about observation
    input_data['observe'] = questionary.confirm(
        'Should holidays falling on weekend observe the next working day?'
    ).ask()

    return input_data

def main():
    '''
    The main function that calls all other ones and collect all the data
    '''

    # The main loop
    while True:
        # Getting user input and checking for pressed Ctrl+D
        try:
            setup = get_projects_conditions()
        except EOFError:
            print('An error occured. Try again. Use Enter to finish the input.')
            return

        if setup == -1:
            print('An error occured during input. The program was stopped.')
            return

        # Calculating the project duration in days
        proj_days = calculate_project_duration(
            setup['fe_devs'],
            setup['fe_task'],
            setup['be_devs'],
            setup['be_task']
        )

        if proj_days == -1:
            print('Please try again.')
            return

        # Parsing the starting year from the project start date
        min_year = int(strptime(setup['start_date'], '%Y-%m-%d').tm_year)
        # Calculating the max project year based on project duration
        max_year = int(min_year + (proj_days / 260) + 1)

        # Getting the list (dict) of public holidays for specific region and years
        holidays_schedule = get_holidays(
            setup['country'],
            setup['state_prov'],
            [y for y in range(min_year, max_year)]
        )

        # Getting the end date of the project along with non-working days stats
        end_date = get_end_date(
            setup['start_date'],
            proj_days,
            holidays_schedule,
            setup['observe']
        )

        # Printing the result
        print(f'Developers need {proj_days} working day(s) to finish the job.')
        print(f'The estimated end date of the project is: {end_date["date"]}.')
        print(f'There will be {end_date["weekends"]} weekend day(s) and',
              f'{end_date["holidays"]} holiday(s) during the working period.')

        # Asking user whether he wants to calculate end date of another project
        try:
            repeat = questionary.confirm(
                'Would you like to calculate the end date of another project?'
            ).ask()
            if repeat:
                continue
            else:
                break
        except EOFError:
            print('An error occured. Try again. Use Enter to finish the input.')
            return

if __name__ == '__main__':
    main()
