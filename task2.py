"""
Student Name : Sampreeth Amith Kumar
Student ID : 31169317
Start Date : 24/04/2020
Last Modified Date : 30/04/2020
Description : Reading data from AU_INV_START.txt and storing
              the calculated stock and revenue of the given
              year in AU_INV_END.txt
"""

def cal_stock_revenue(input_dict):
    """
    cal_stock_revenue()
    - Calculates the stock and revenue at the end of the simulation year.
    """

    """Start year provided in the txt file is split to separate integer value."""
    str_start_year = str(input_dict["start_year"])
    mid_index = int(len(str_start_year) / 2)
    year_start = int(str_start_year[:mid_index])
    month_date = str_start_year[mid_index:]
    mid_index = int(len(month_date) / 2)
    month_start = int(month_date[:mid_index])
    date_start = int(month_date[mid_index:])

    """Initial year, stock and revenue are pre defined"""
    initial_year = 2000
    initial_stock = 1000
    initial_revenue = 0
    difference_year = abs(year_start - initial_year)

    """End Stock and Revenue are calculated from 20000101 
    until the year before provided in txt file."""
    end_stock = stock(initial_stock, initial_year, 1, 1, difference_year)
    total_revenue = round(revenue(initial_revenue, initial_year, 1, 1, difference_year), 2)

    """End stock and Revenue calculated from above step is given as 
    input to find the stock and revenue until the given month."""
    end_stock = stock(end_stock, year_start, 1, 1, ((month_start - 1) / 12))
    total_revenue = round(revenue(total_revenue, year_start, 1, 1, ((month_start - 1) / 12)), 2)

    """End stock and Revenue calculated from above step is given as 
    input to find the stock and revenue untill the given date."""
    end_stock = stock(end_stock, year_start, month_start, date_start, 0)
    start_revenue = round(revenue(total_revenue, year_start, month_start, date_start, 0), 2)

    """Start of Full Simulation. Simulation is done for Number of 
    years of simulation provided."""
    end_stock = stock(end_stock, year_start, month_start, date_start, NO_YEAR_SIM)
    total_revenue = round(revenue(start_revenue, year_start, month_start, date_start, NO_YEAR_SIM), 2)

    total_revenue = total_revenue - start_revenue                                                   # Revenue generated during the simulation year.

    if (month_start == 2 and date_start == 29 and leap_year_or_not(year_start + NO_YEAR_SIM) == 0):
        """If the simulation end year is not a leap year, then end year 
            will be march 1st, if the start year is 29th february."""
        date_start = 1
        month_start = 3

    if (month_start < 10):
        """Add zero to integer beginning if a number is less then 10."""
        month_start = "0" + str(month_start)

    if date_start < 10:
        """Add zero to integer beginning if a number is less then 10."""
        date_start = "0" + str(date_start)

    output_dict = {"end_year": int(str(year_start + NO_YEAR_SIM) + str(month_start) + str(date_start)),
                   "end_stock": end_stock,
                   "end_revenue": total_revenue}                                                     # End year,end stock and end revenue are stored.

    return output_dict

def distribution(year):
    """
    distribution() will return the normal distribution of the particular year.
    - On the year 2000 there is distribution of 27 items every day henceforth, there will be 10% increase in
    - the distribution.
    - there will be a recession at every 9 years. 20% reduction in distribution, 10% the year after and 5% on the
    - 3rd year.
    """

    """Distribution is of particular year is found by simulating from the year 2000."""
    begin_year = 2000
    normal_distribution = round(36 / 1.35)                                                  # Provided peak distribution rate at 2000 is divided by 1.35
                                                                                            # to find normal distribution.

    """Crisis Year Counter."""
    first_crisis_year = 0                                                                   # first_crisis year happens every 9th years
    second_crisis_year = 0                                                                  # second crisis year happens every 10th year
    third_crisis_year = 0                                                                   # third crisis year happens every 11th year

    if year == begin_year:
        return normal_distribution
    else:
        while begin_year != (year):  # Simulation of distribution year.
            begin_year = begin_year + 1

            if ((first_crisis_year + 1) % CRIS_RECUR_FREQUENCY == 0):
                """20% reduce in distribution during 1st crisis year"""
                normal_distribution = round(normal_distribution - (normal_distribution * (20 / 100)))
                first_crisis_year += 1
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((second_crisis_year + 1) % (CRIS_RECUR_FREQUENCY + 1) == 0):
                """10% reduce in distribution during 2nd crisis year"""
                normal_distribution = round(normal_distribution - (normal_distribution * (10 / 100)))
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((third_crisis_year + 1) % (CRIS_RECUR_FREQUENCY + 2) == 0):
                """5% reduce in distribution during 3rd crisis year"""
                normal_distribution = round(normal_distribution - (normal_distribution * (5 / 100)))
                third_crisis_year += 1

            else:
                """normal increase in distribution other years"""
                normal_distribution = round(normal_distribution + (normal_distribution * (10 / 100)))
                first_crisis_year += 1
                second_crisis_year += 1
                third_crisis_year += 1

        return round(normal_distribution)

def leap_year_or_not(year):
    """
    leapyear_or_not() : Checks if the input year is a leap year or not.
    - leap year has 366 days(29 days in february)
    - leap year is divisible by 4,except for year that are exactly divisible by 100
    - century year is a leap year if they are divisible by 400.
    - return:
        - 1: is a leap year
        - 0: is not a leap year
    - Leap year Source - https://en.wikipedia.org/wiki/Leap_year Date: 10/04/2020
    """

    if year % 4 == 0:
        """Check if the given year is divisible by 4."""
        if (year % 100 != 0):
            return 1
        elif (year % 400 == 0):
            return 1
        else:
            return 0
    else:
        return 0

def read_data():
    """
    read_data() : reads the data from the file and stores the data to a dictionary
    -file is first read, stored in a list,
    -newly generated list is used to store the data in a dictionary.
    """

    dict = {}

    """Read data from AU_INV_START.txt file and store the data in a list."""
    file = open("AU_INV_START.txt", "r")
    l_list = file.read().splitlines()

    """Data in list is stored to dictionary variable."""
    dict["start_year"] = int(l_list[0])
    dict["start_stock"] = int(round(float(l_list[1])))
    dict["start_revenue"] = float(l_list[2])

    return dict

def refurbished(days, distribution_rate, rrp_rate):
    """refurbished() will return the revenue generated from refurbished products sold."""
    month_sale = distribution_rate * days
    product_returned = round(month_sale * (PER_DEF / 100))
    refurbised_revenue = product_returned * (rrp_rate * (80 / 100))

    return refurbised_revenue

def revenue(revenue, year, month, date_start, simulation_year):
    """revenue() will return the revenue generated at the end of the month."""

    add_day = leap_year_or_not(year)
    normal_distribution = distribution(year)
    normal_rrp = rrp(year)
    date = date_start
    month_counter = 1

    while (month_counter <= (12 * simulation_year)):


        """Distribution value at different time."""
        initial_peak_distribution = round(normal_distribution + (normal_distribution * (35 / 100)))
        hike_distribution = round(normal_distribution + (normal_distribution * (10 / 100)))
        final_peak_distribution = round(hike_distribution + (hike_distribution * (35 / 100)))

        """Revenue value at different time."""
        initial_peak_rrp = round(normal_rrp + (normal_rrp * (20 / 100)), 2)
        hike_rrp = round(normal_rrp + (normal_rrp * (5 / 100)), 2)
        final_peak_rrp = round(hike_rrp + (hike_rrp * (20 / 100)), 2)

        """Peak Month January to February end."""
        if (month == 1 or month == 2):
            if (month == 1):
                """January"""
                while (date <= 31):
                    revenue = revenue + (initial_peak_distribution * initial_peak_rrp)
                    if (date == 31):
                        revenue = revenue + refurbished(31, initial_peak_distribution, initial_peak_rrp)
                    date += 1
                date = 1

            if (month == 2):
                """February"""
                while (date <= (28 + add_day)):
                    revenue = revenue + (initial_peak_distribution * initial_peak_rrp)
                    if (date == (28 + add_day)):
                        revenue = revenue + refurbished((28 + add_day), initial_peak_distribution, initial_peak_rrp)
                    date += 1
                date = 1

        """Normal months 1st of March to 31st June."""
        if (month == 3 or month == 4 or month == 5 or month == 6):
            """March or May"""
            if (month == 3 or month == 5):
                while (date <= 31):
                    revenue = revenue + (normal_distribution * normal_rrp)
                    if (date == 31):
                        revenue = revenue + refurbished(31, normal_distribution, normal_rrp)
                    date += 1
                date = 1

            """April or june"""
            if (month == 4 or month == 6):
                while (date <= 30):
                    revenue = revenue + (normal_distribution * normal_rrp)
                    if (date == 30):
                        revenue = revenue + refurbished(30, normal_distribution, normal_rrp)
                    date += 1
                date = 1

        """10% hike in the distibution from 1st July to 31st October"""
        if (month == 7 or month == 8 or month == 9 or month == 10):
            """July or August or October."""
            if (month == 7 or month == 8 or month == 10):

                while (date <= 31):
                    revenue = revenue + (hike_distribution * hike_rrp)
                    if (date == 31):
                        revenue = revenue + refurbished(31, hike_distribution, hike_rrp)
                    date += 1
                date = 1

            """Septemper."""
            if month == 9:
                while (date <= 30):
                    revenue = revenue + (hike_distribution * hike_rrp)
                    if (date == 30):
                        revenue = revenue + refurbished(30, hike_distribution, hike_rrp)
                    date += 1
                date = 1

        """Peak distribution 1st November to 31st December"""
        if (month == 11 or month == 12):
            """November."""
            if month == 11:
                while (date <= 30):
                    revenue = revenue + (final_peak_distribution * final_peak_rrp)
                    if (date == 30):
                        revenue = revenue + refurbished(30, final_peak_distribution, final_peak_rrp)
                    date += 1
                date = 1

            """December Month"""
            if month == 12:
                """December."""
                while (date <= 31):
                    revenue = revenue + (final_peak_distribution * final_peak_rrp)
                    if (date == 31):
                        revenue = revenue + refurbished(31, final_peak_distribution, final_peak_rrp)
                    date += 1
                date = 1

        month_counter += 1                                                              # Month Incremented
        if (month == 12):
            """If the month has reached the end of the year.
            Increment the year to next year and begin the month again from 1st."""
            month = 0
            year += 1
            add_day = leap_year_or_not(year)                                           # given year is a leap year or not.
            normal_distribution = distribution(year)                                   # Distribution rate at that year is found.
            normal_rrp = rrp(year)                                                     # RRP rate at that year is found.

        month += 1

    date = 1
    if (month == 2 and date_start == 29 and leap_year_or_not(year) == 0):
        date_start -= 1
    while (date < date_start):
        """Simulation from 1st day of the month till the end of the given date."""

        """Distribution value at different time."""
        initial_peak_distribution = round(normal_distribution + (normal_distribution * (35 / 100)))
        hike_distribution = round(normal_distribution + (normal_distribution * (10 / 100)))
        final_peak_distribution = round(hike_distribution + (hike_distribution * (35 / 100)))

        """Revenue Value at diffenent time."""
        initial_peak_rrp = round(normal_rrp + (normal_rrp * (20 / 100)), 2)
        hike_rrp = round(normal_rrp + (normal_rrp * (5 / 100)), 2)
        final_peak_rrp = round(hike_rrp + (hike_rrp * (20 / 100)), 2)

        if (month == 1 or month == 2):
            revenue = revenue + (initial_peak_distribution * initial_peak_rrp)

        if (month == 3 or month == 4 or month == 5 or month == 6):
            revenue = revenue + (normal_distribution * normal_rrp)

        if (month == 7 or month == 8 or month == 9 or month == 10):
            revenue = revenue + (hike_distribution * hike_rrp)

        if (month == 11 or month == 12):
            revenue = revenue + (final_peak_distribution * final_peak_rrp)
        date += 1
    return round(revenue, 2)

def rrp(year):
    """
    rrp() will find the Recommended retail price of the given year.
    - normal rrp will be 705/1.20 at the beginning as mention in the case study.
    - every year there will be a increase of 5% in rrp.
    - during the global financial crisis there will be a increase of additional 10%
    - 2nd year will have a 5
    """

    """Begin year and Normal rrp of the year 2000 is stored."""
    begin_year = 2000
    normal_rrp = round(705 / 1.20, 2)                                                               # RRP is divided by 1.20 to find the normal RRP rate.

    first_crisis_year = 0                                                                           # first_crisis year happens every 9th years
    second_crisis_year = 0                                                                          # second crisis year happens every 10th year
    third_crisis_year = 0                                                                           # third crisis year happens every 11th year

    if year == begin_year:
        return normal_rrp                                                                           # if rrp to find year is 2000 then return calculated value above.
    else:
        while begin_year != (year):
            begin_year = begin_year + 1                                                             # begin year is incremented, untill the given year.

            if ((first_crisis_year + 1) % CRIS_RECUR_FREQUENCY == 0):
                """Additional 10% increase in rrp during 1st crisis year."""
                normal_rrp = round(normal_rrp + (normal_rrp * (15 / 100)), 2)
                first_crisis_year += 1
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((second_crisis_year + 1) % (CRIS_RECUR_FREQUENCY + 1) == 0):
                """Additional 5% increase in rrp during 2nd crisis year."""
                normal_rrp = round(normal_rrp + (normal_rrp * (10 / 100)), 2)
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((third_crisis_year + 1) % (CRIS_RECUR_FREQUENCY + 2) == 0):
                """Additional 8% increase in rrp during 3rd crisis year."""
                normal_rrp = round(normal_rrp + (normal_rrp * (8 / 100)), 2)
                third_crisis_year += 1

            else:
                """Normal increase in rrp during other years"""
                normal_rrp = round(normal_rrp + (normal_rrp * (5 / 100)), 2)
                first_crisis_year += 1
                second_crisis_year += 1
                third_crisis_year += 1

        return round(normal_rrp, 2)

def stock(stock_value, year, month, date_start, simulation_year):
    """
    stock() returns the available stock at the end of the year.
    - stocks are normal distributed during the non peak months
    - stocks have increase in distribution during 1st Nov to end of feb
    - every financial year there will be a hike in stock
    - at the end of each month, 5% of stocks are returned as defective.
    """

    add_day = leap_year_or_not(year)
    normal_distribution = distribution(year)
    date = date_start
    month_counter = 1

    while (month_counter <= (12 * simulation_year)):

        if normal_distribution >= 1000:
            write_error()

        """Distribution rate at the given time of interval is found."""
        initial_peak_distribution = round(normal_distribution + (normal_distribution * (35 / 100)))
        hike_distribution = round(normal_distribution + (normal_distribution * (10 / 100)))
        final_peak_distribution = round(hike_distribution + (hike_distribution * (35 / 100)))

        """Peak Month January to February end."""
        if (month == 1 or month == 2):
            if (month == 1):
                stock_value = stock_calculation(date, 31, stock_value, initial_peak_distribution)
                date = 1

            if (month == 2):
                stock_value = stock_calculation(date, (28 + add_day), stock_value, initial_peak_distribution)
                date = 1

        """Normal months 1st of March to 31st June."""
        if (month == 3 or month == 4 or month == 5 or month == 6):
            """March or May"""
            if (month == 3 or month == 5):
                stock_value = stock_calculation(date, 31, stock_value, normal_distribution)
                date = 1

            """April or june"""
            if (month == 4 or month == 6):
                stock_value = stock_calculation(date, 30, stock_value, normal_distribution)
                date = 1

        """10% hike in the distibution from 1st July to 31st October"""
        if (month == 7 or month == 8 or month == 9 or month == 10):
            """July or August or October."""
            if (month == 7 or month == 8 or month == 10):
                stock_value = stock_calculation(date, 31, stock_value, hike_distribution)
                date = 1

            """Septemper."""
            if month == 9:
                stock_value = stock_calculation(date, 30, stock_value, hike_distribution)
                date = 1

        """Peak distribution 1st November to 31st December."""
        if (month == 11 or month == 12):
            """November Month."""
            if month == 11:
                stock_value = stock_calculation(date, 30, stock_value, final_peak_distribution)
                date = 1

            """December Month."""
            if month == 12:
                stock_value = stock_calculation(date, 31, stock_value, final_peak_distribution)
                date = 1

        month_counter += 1                                                                          # Counter incremented.
        if (month == 12):
            """If the month has reached the end of the year.
            Increment the year to next year and begin the month again from 1st."""
            month = 0
            year += 1
            add_day = leap_year_or_not(year)                                                        # find if the given year is leap year or not
            normal_distribution = distribution(year)                                                # find the normal distribution of the given year.
        month += 1

    date = 1
    if (month == 2 and date_start == 29 and leap_year_or_not(year) == 0):
        date_start -= 1
    while (date < date_start):
        """Stock from the beginning of the month till the given date."""

        """distribution value at different time"""
        initial_peak_distribution = round(normal_distribution + (normal_distribution * (35 / 100)))
        hike_distribution = round(normal_distribution + (normal_distribution * (10 / 100)))
        final_peak_distribution = round(hike_distribution + (hike_distribution * (35 / 100)))

        if (month == 1 or month == 2):
            if (stock_value <= 400):
                stock_value = stock_value + 600
            stock_value = stock_value - initial_peak_distribution

        if (month == 3 or month == 4 or month == 5 or month == 6):
            if (stock_value <= 400):
                stock_value = stock_value + 600
            stock_value = stock_value - normal_distribution

        if (month == 7 or month == 8 or month == 9 or month == 10):
            if (stock_value <= 400):
                stock_value = stock_value + 600
            stock_value = stock_value - hike_distribution

        if (month == 11 or month == 12):
            if (stock_value <= 400):
                stock_value = stock_value + 600
            stock_value = stock_value - final_peak_distribution

        date += 1

    if stock_value < 0:
        write_error()

    return round(stock_value)

def stock_calculation(date, days, stock_value, distribution_rate):
    """stock_calculation() will return the stock value at the end of the month."""

    month_sale = 0
    while (date <= days):
        if (stock_value <= 400):
            """Restocked each time the stock goes below 400."""
            stock_value = stock_value + 600
        stock_value = stock_value - distribution_rate
        month_sale = month_sale + distribution_rate
        if (date == days):
            """Defective Items are returned back."""
            stock_value = stock_value + (month_sale * (PER_DEF / 100))
        date += 1

    return stock_value

def write_data(output_dict):
    """
    write_data() writes the data in dictionary to a txt file.
    Make sure AU_INV_END.txt is not present in the directory.
    """

    file = open("AU_INV_END.txt", "w")                                   # AU_INV_END.txt is created

    """Integer values are converted to string. Before writing it on the txt file."""
    end_year = str(output_dict["end_year"])
    end_stock = str(output_dict["end_stock"])
    end_revenue = str(output_dict["end_revenue"])

    """Writing data to txt file."""
    file.write(end_year)
    file.write("\n")                                                    # pussing the write to next line
    file.write(end_stock)
    file.write("\n")
    file.write(end_revenue)

def write_error():
    """
    write_error() thorws an error when the execution has not be completed.
    """

    file = open("AU_INV_END.txt", "w")

    file.write("Invalid : distribution is more than 1000 perday")                               # Displaying error Message on txt file.

    raise SystemExit()                                                                          # Exit Program Execution

"""Global Variables Declaration."""
NO_YEAR_SIM = 3
PER_DEF = 5
CRIS_RECUR_FREQUENCY = 9

"""read_data() reads the data from txt file and stores in dictionary."""
input_dict = read_data()

"""cal_stock_revenue() is called to find stock and revenue at the end of simulation."""
output_dict = cal_stock_revenue(input_dict)

"""writes the data present in output dictionary to a txt file."""
write_data(output_dict)
