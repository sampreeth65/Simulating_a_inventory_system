# Simulating_a_inventory_system
Stocking level of Cantilever Umbrella inside an inventory management system in an Australian firm.
The firm privides this products to its distributors together with a recommended retail price(RRP).

# Background Information
The Australian firm was established in January 1st, 2000. For the past 20 years, there have been no
changes to the inventory management system. There was also no change in product model in the
past 20 years as it is quite robust design, the product model will not change in the future either.
On January 1st, 2000, when the firm was first open for business, there were 1000 cantilever umbrellas
in stock, the distribution number of the cantilever umbrella on that day to the distributors was 36,
and each cantilever umbrella’s RRP was $705 AUD

Note:
When the inventory stock drops to 400, the firm will restock 600 cantilever umbrellas back to the warehouse.

Cantilever umbrella has a peak selling season. It isfrom 1st November to end of February each year. During the peask season,the company is expected to have a 35% increase in quantity for distribution. It is also expected tohave 20% increasein RRP during peak season as it is hard to supply enough umbrellas to meet the demand.

The stocking system is updated daily at 11:59 pm. This number has been consistent every day until
the beginning of a new financial year.

At the beginning of the new financial year each year (1st July), the company will impose a 10% increase
in the supply of cantilever umbrellas to its distributors (rounded up) and 5% increase of the RRP due
to inflation. 

Based on statistics, global financial crisis happens every 9 years, and lasts for another 2 years, the
number of cantilever umbrella distributed to distributors will drop by 20% in the first year when
global financial crisis hit the market, the number will continue to drop by 10% and 5% for the next 2
years when the economy is recovering.
In order to make up the losses, during the year that a global financial crisis starts, the company will
add an additional 10% increase in RRP to the product, the increase of the product RRP will become
5% in the next year, and 3% the year after to make up the loss. 

It is expected that 5% of items will be defective and returned to warehouse every month
Defective items will be refurbished and redistributed at 80% of original price (original price is the RRP
at the time the product is returned) in the following months.

# Project:

# Task 1:
Finds the revenue and the total stock at the end of a given year(year provided by the user in txt file)
simulation runs from 2000 1st jan till the end of year provided by the user. (Example: if the file has start year = 2010, simulation of stock and revenue value at the end of 2010 or beginning of 2011 is found by running simulation starting from 2000 with a start stock of 1000 and a start revenue of 0)
Stock and revenue calculated at the end of the year is for one year.
Simulation calculates values accordingly if the given year is a global financial crisis year.
Simulation only runs for 1 year.

# Task 2
Simulation takes in data(start year,start,revenue,start stock) from the txt file. 
Simulation runs for 3 year by default.(Changes can be made if needed)

Note: In Task 2 start year is also provided with date and month. Hence, Stocks and revenue at the end of 3 years from the provided date is found.
