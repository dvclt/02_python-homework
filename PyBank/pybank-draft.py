# The total number of months included in the dataset.

# The net total amount of Profit/Losses over the entire period.

# The average of the changes in Profit/Losses over the entire period.

# The greatest increase in profits (date and amount) over the entire period.

# The greatest decrease in losses (date and amount) over the entire period.

# Your final script should print the analysis to the terminal and export a text file with the results.

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# pseudo code:
#     read csv file
#     interate through all rows 
#     find: total, avg, max, min
#     export to export csv
from pathlib import Path

import csv

filepath = Path("./Resources/budget_data.csv")

records =[]

with open (filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    headers = next(csvreader)
    headers.append("Change")
    print(headers)
    
    total_month = 0
    total = 0
    
    change = 0
    last_month = 0
    avg_change = 0
    total_change =0
    
    grt_increase = True
    grt_increase_date = 0
    
    grt_decrease = True
    grt_decrease_date = 0
    
    for row in csvreader:
        total_month += 1
        total += int(row[1])
        
        records.append(row)
        
        if last_month ==0:
            last_month = int(row[1])
        
        change = int(row[1]) - last_month
        records[total_month-1].append(change)
        
        total_change +=change
        last_month = int(row[1])
        
        #find max increase:
        if change >= 0:
            if grt_increase == True:
                grt_increase = change
                grt_increase_date = row[0]
            elif change > grt_increase:
                grt_increase = change
                grt_increase_date = row[0]

        #find max decrease:
        else:
            if grt_decrease == True:
                grt_decrease = change
                grt_decrease_date = row[0]
                
            elif change < grt_decrease:
                grt_decrease = change
                grt_decrease_date = row[0]

        #note: can use max() and min(), also can create list of records        
        
    avg_change = round(total_change / total_month,2)


print(records)

output_filepath = Path('./output.txt')

with open (output_filepath, 'w') as file:
    filewriter = file.write(f'Total Months: {total_month}')

    
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total}')
print(f'Average  Change: ${avg_change}')
print(f'Greatest Increase in Profits: {grt_increase_date} (${grt_increase})')
print(f'Greatest Decrease in Profits: {grt_decrease_date} (${grt_decrease})')
