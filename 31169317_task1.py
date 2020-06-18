"""
Student Name : Sampreeth Amith Kumar
Student ID : 31169317
Start Date : 10/04/2020
Last Modified Date : 30/04/2020
Description : Reading data from AU_INV_START.txt and storing
              the calculated stock and revenue of the given
              year in AU_INV_END.txt
"""

def cal_stock_revenue(input_dict):
    """
    cal_stock_revenue()
    - finds if the given year is a leap year or not.
    - finds the distribution rate at that year
    - finds the rrp at that year
    - calculates the stock at the end of the year
    - calculates the revenue at the end of the year.
    """

    """Start year, start stock, start revenue are always 2000, 1000, 0 respectively."""
    start_year = 2000
    start_stock = 1000
    start_revenue = 0

    while start_year <= input_dict["start_year"]:
        """Calculated from year: 2000 to the end of the given year."""

        add_day = leap_year_or_not(start_year)                                                              # checks if the given year is a leap year or not.

        normal_distribution = distribution(start_year)                                                      # Distribution rate during no peak time is calculated
        normal_rrp = rrp(start_year)                                                                        # RRP rate during non peak time is calculated

        """If the distributiton per day crosses 1000 per day. 
        Throw an error on in txt file."""
        if(normal_distribution >= 1000):
            write_error()

        end_stock=stock(start_stock,normal_distribution,add_day)                                            # One year Stock of the given year is calculated.
        total_revenue = revenue_made(start_revenue,normal_rrp,normal_distribution,add_day)                  # One year Revenue of the given year is calculated.

        start_year += 1                                                                                     # Year is incremented,until the given year
        start_stock = end_stock
        start_revenue = round(total_revenue - start_revenue,2)


    output_dict = {"end_year": start_year,"end_stock": start_stock,"end_revenue": start_revenue}              # End_year, end stock, end revenue of One year is stored in dictionary

    return output_dict

def distribution(year):
    """
    distribution() will return the normal distribution of the particular year.
    - On the first year there is distribution of 27 items every day henceforth, there will be 10% increase in
    - the distribution.
    - there will be a recession at every 9 years. 20% reduction in distribution, 10% the year after and 5% on the
    - 3rd year.
    """

    """Start year and initial distibution value is stored."""
    begin_year = 2000
    normal_distribution = round(36 / 1.35)                                                              # Given distribution is divided by 1.35 to find the
                                                                                                        # noraml distribution of the year 2000

    """Crisis year Counter"""
    first_crisis_year  = 0                                                                              # Counter for 9th crisis year.
    second_crisis_year = 0                                                                              # Counter for 10th crisis year
    third_crisis_year  = 0                                                                              # Counter for 11th crisis year

    """Return the distribution of the given year."""
    if year == begin_year:
        return normal_distribution
    else:
        while begin_year != year:
            begin_year = begin_year + 1

            if ((first_crisis_year + 1) % 9 == 0) :
                """20% reduce in distribution during 1st crisis year, 1st crisis happens every 9th years."""
                normal_distribution = round(normal_distribution - (normal_distribution * (20/100)))
                first_crisis_year  += 1
                second_crisis_year += 1
                third_crisis_year  += 1

            elif ((second_crisis_year + 1) % 10 == 0) :
                """10% reduce in distribution during 2nd crisis year,2nd crisis happens every 10th year."""
                normal_distribution = round(normal_distribution - (normal_distribution * (10/100)))
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((third_crisis_year + 1) % 11 == 0) :
                """5% reduce in distribution during 3rd crisis year,3rd crisis happens every 11th year."""
                normal_distribution = round(normal_distribution - (normal_distribution * (5/100)))
                third_crisis_year += 1

            else :
                """10% increase in distribution during normal years."""
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
            return 1                                            # Return 1 to add a day to the number of days in a year.
        elif (year % 400 == 0):
            return 1
        else:
            return 0
    else:
        return 0                                               # Return 0 to add a day to the number of days in a year.

def read_data():
    """
    read_data() : reads the data from the file and stores the data to a dictionary
    -file is fist read, stored in a list,
    -newly generated list is used to store the data in a dictionary.
    """

    dictionary = {}

    """Read data from AU_INV_START.txt file and store the data in a list."""
    file = open("AU_INV_START.txt","r")
    l_list = file.read().splitlines()

    """Data in list is stored to dictionary variable."""
    dictionary["start_year"]    = int(l_list[0])
    dictionary["start_stock"]   = int(l_list[1])
    dictionary["start_revenue"] = float(l_list[2])

    return dictionary

def revenue_made(revenue,normal_rrp,normal_distribution,add_day):
    """
    revenue_made() returns the revenue made at the end of the year.
    revenue is calculated by multiplying number of quantity distributed and rrp of the product.
    """

    """Distribution rate at different interval in a given year is calculated."""
    initial_peak_distribution = round(normal_distribution + (normal_distribution * (35/100)))
    hike_distribution = round(normal_distribution + (normal_distribution * (10/100)))
    final_peak_distribution = round(hike_distribution + (hike_distribution * (35/100)))

    """Recommended Retail Price at different interval in a given year is calculated."""
    initial_peak_rrp = round(normal_rrp + (normal_rrp * (20/100)),2)
    hike_rrp= round(normal_rrp + (normal_rrp * (5/100)),2)
    final_peak_rrp = round(hike_rrp + (hike_rrp * (20/100)),2)

    """Revenue from starting of January to the end of february."""
    for i in range(59 + add_day):

        if (i == 30 or i == (58 + add_day)):
            """5% return in stocks at the end of the month."""
            if (i == 30):
                """End of January."""
                month_sale = initial_peak_distribution * 31
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (initial_peak_rrp * (80 / 100))                 # Returned stocks are sold at 80% of the price.
                revenue = revenue +   refurbised_revenue

            elif (i == 58 + add_day):
                """End of February."""
                month_sale = initial_peak_distribution * (28 + add_day)
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (initial_peak_rrp * (80 / 100))
                revenue = revenue + refurbised_revenue

        revenue = revenue + (initial_peak_distribution * initial_peak_rrp)                              # Revenue made every day.

    """Revenue from 1st March to 30th June at normal distribution and RRP rate."""
    for i in range(122):

        if (i == 30 or i == 60 or i == 91 or i == 121):
            """5% Return in stock at the end of the month."""
            if (i == 60 or i == 121):
                """End of April or June."""
                month_sale = normal_distribution * 30                                                   # 30 - Number of days in April/June.
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (normal_rrp * (80 / 100))
                revenue = revenue + refurbised_revenue

            elif (i == 30 or i == 91):
                """End of March/May."""
                month_sale = normal_distribution * 31                                                   # 31 - Number of days in March/May.
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (normal_rrp * (80 / 100))
                revenue = revenue + refurbised_revenue

        revenue = revenue + (normal_distribution * normal_rrp)                                          # Revenue made each day.

    """Revenue from 1st July to 31st October. - 10% increase in distribution and 5% increase in RRP."""
    for i in range(123):

        if (i == 30 or i == 61 or i == 91 or i == 122):
            """5% return in stock at the end of the month."""
            if (i == 91 ):
                """End of September."""
                month_sale = hike_distribution * 30                                                     # 30 - Nomber of days in September
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (hike_rrp * (80 / 100))
                revenue = revenue + refurbised_revenue

            elif (i == 30 or i == 61 or i == 122):
                """End of July,August,October."""
                month_sale = hike_distribution * 31                                                     # 31 - Number of days in the given month.
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (hike_rrp * (80 / 100))
                revenue = revenue + refurbised_revenue

        revenue = revenue + (hike_distribution * hike_rrp)                                              # Revenue made each day.

    """Revenue from 1st November to 31st December - Peak distribution and RRP"""
    for i in range(61):

        if (i == 29 or i == 60):
            """5% return in products at the end of month."""
            if (i == 29):
                """End of November month."""
                month_sale = final_peak_distribution * 30
                product_returned = round(month_sale * (5/100))                                          #5% of the distributed products are returned.
                refurbised_revenue = product_returned * (final_peak_rrp * (80/100))
                revenue = revenue + refurbised_revenue
            elif (i == 60):
                """End of December month."""
                month_sale = final_peak_distribution * 31                                               # 31 - Number of days in the month.
                product_returned = round(month_sale * (5 / 100))
                refurbised_revenue = product_returned * (final_peak_rrp * (80 / 100))
                revenue = revenue + refurbised_revenue

        revenue = revenue + (final_peak_distribution * final_peak_rrp)

    return round(revenue,2)

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
    normal_rrp = round(705 / 1.20,2)                                                        # RRP is divided by 1.20 to find the normal RRP rate.

    first_crisis_year = 0                                                                   # first_crisis year happens every 9th years
    second_crisis_year = 0                                                                  # second crisis year happens every 10th year
    third_crisis_year = 0                                                                   # third crisis year happens every 11th year

    if year == begin_year:
        return normal_rrp                                                                   # if rrp to find year is 2000 then return calculated value above.
    else:
        while begin_year != (year):
            begin_year = begin_year + 1                                                     # begin year is incremented, untill the given year.

            if ((first_crisis_year + 1) % 9 == 0):
                """Additional 10% increase in rrp during 1st crisis year."""
                normal_rrp = round(normal_rrp + (normal_rrp * (15/100)),2)
                first_crisis_year += 1
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((second_crisis_year + 1) % 10 == 0) :
                """Additional 5% increase in rrp during 2nd crisis year."""
                normal_rrp = round(normal_rrp + (normal_rrp * (10/100)),2)
                second_crisis_year += 1
                third_crisis_year += 1

            elif ((third_crisis_year + 1) % 11 == 0) :
                """Additional 8% increase in rrp during 3rd crisis year."""
                normal_rrp = round(normal_rrp + (normal_rrp * (8/100)),2)
                third_crisis_year += 1

            else :
                """Normal increase in rrp during other years."""
                normal_rrp = round(normal_rrp + (normal_rrp * (5/100)),2)
                first_crisis_year += 1
                second_crisis_year += 1
                third_crisis_year += 1

        return round(normal_rrp,2)

def stock(stock_value, normal_distribution, add_day):
    """
    stock() returns the available stock at the end of the year.
    - stocks are normal distributed during the non peak months
    - stocks have increase in distribution during 1st Nov to end of feb
    - every financial year there will be a hike in stock
    - at the end of each month, 5% of stocks are returned as defective.
    """

    """Distribution rate at the given time of interval is found."""
    initial_peak_distribution = round(normal_distribution + (normal_distribution * (35/100)))
    hike_distribution = round(normal_distribution + (normal_distribution * (10/100)))
    final_peak_distribution = round(hike_distribution + (hike_distribution * (35/100)))

    month_sale = 0
    for i in range(59 + add_day):
        """Stock calculated from 1st January to end of February.35% increase in distribution rate."""
        if stock_value <= 400:
            stock_value = stock_value + 600                                                     # Stocks are restocked every time stock value goes below 400.

        stock_value = stock_value - initial_peak_distribution
        month_sale = month_sale + initial_peak_distribution

        if (i == 30 or i == (58+add_day)):
            """5% of the stocks are returned back at the end of the month."""
            stock_value = stock_value + (month_sale * (5 / 100))
            month_sale = 0

    month_sale = 0
    for i in range(122):
        """Stock value from 1st march - 30th june. Distribution at normal rate."""
        if stock_value <= 400:
            stock_value = stock_value + 600                                                     # Restocking

        stock_value = stock_value - normal_distribution
        month_sale = month_sale + normal_distribution

        if(i == 30 or i == 60 or i == 91 or i ==121):
            """Returned stocks."""
            stock_value = stock_value + (month_sale * (5 / 100))
            month_sale = 0

    month_sale = 0
    for i in range(123):
        """Stock value from 1st july - 31st oct (10% - financial year increase)"""
        if stock_value <= 400:                                                                  # Restocking
            stock_value = stock_value + 600

        stock_value = stock_value - hike_distribution
        month_sale = month_sale + hike_distribution

        if (i == 30 or i == 61 or i == 91 or i == 122):
            """Returned stocks end of month."""
            stock_value = stock_value + (month_sale * (5 / 100))
            month_sale = 0

    month_sale = 0
    for i in range(61):
        """Stock value from 1st November to 31st December. 35% Peak distribution rate."""
        if stock_value <= 400:
            stock_value = stock_value + 600                                                    # Restocking

        stock_value = stock_value - final_peak_distribution
        month_sale = month_sale + final_peak_distribution

        if (i == 29 or i == 60):
            """Stocks returned at the end of the month."""
            stock_value = stock_value + (month_sale * (5 / 100))
            month_sale = 0

    if stock_value < 0:
        write_error()

    return round(stock_value)

def write_data(output_dict):
    """
    write_data() writes the data in dictionary to a txt file.
    """

    file = open("AU_INV_END.txt","w")                                                       # AU_INV_END.txt is created

    """Dictionary data is converted to String, as writing a file takes in String."""
    end_year = str(output_dict["end_year"])
    end_stock = str(output_dict["end_stock"])
    end_revenue = str(output_dict["end_revenue"])


    """Writing the data to the file."""
    file.write(end_year)
    file.write("\n")                                                                        # Pussing the write to next line
    file.write(end_stock)
    file.write("\n")
    file.write(end_revenue)

def write_error():
    """
    write_error() thorws an error when the execution has not be completed.
    """

    file = open("AU_INV_END.txt", "w")

    file.write("Invalid : distribution is more than 1000 perday")                               # Displaying error Message on txt file.

    raise SystemExit()                                                                          # Exit program when error has occured.


input_dict = read_data()                                                                        # Calling the read_data() and storing
                                                                                                # the data returned to input_dict

output_dict = cal_stock_revenue(input_dict)                                                     # Cal_stock_revenue() is called to find
                                                                                                # the stock and revenue at the end of
                                                                                                # the year.
write_data(output_dict)
