import os, csv, sys
csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('Resources', 'Pybank_Results.txt')


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    results = list(csvreader)

del results[0] 

TotalMonths = len(results)
TotalRevenue = 0
PreviousMonthRevenue = 0
TotalRevenueChange = []
GreatestRevenueIncrease, GreatestRevenueDecrease = [0, 0], [0, 0]

for row in results:
    TotalRevenue += int(row[1])
    RevenueChange = int(row[1]) - int(PreviousMonthRevenue)
    
    if len(TotalRevenueChange) > 0:
        if RevenueChange > int(GreatestRevenueIncrease[1]):
            GreatestRevenueIncrease = [row[0], RevenueChange]

        if RevenueChange < int(GreatestRevenueDecrease[1]):
            GreatestRevenueDecrease = [row[0], RevenueChange]

    TotalRevenueChange.append(RevenueChange)
    PreviousMonthRevenue = row[1]

del TotalRevenueChange[0] 

with open(output_file, "w") as datafile:
    
    oldstdout = sys.stdout
    sys.stdout = datafile

    print('Financial Analysis:')
    print('----------------------------')
    print('Total Months:', TotalMonths) 
    print('Total: ${:,.2f}'.format(TotalRevenue))
    print('Average Change: ${:,.2f}'.format(sum(TotalRevenueChange)/len(TotalRevenueChange)))
    print('Greatest Increase in Profits: {} ${:,.2f}'.format(
        GreatestRevenueIncrease[0], GreatestRevenueIncrease[1])) 
        
    print('Greatest Decrease in Profits: {} ${:,.2f}'.format(
        GreatestRevenueDecrease[0], GreatestRevenueDecrease[1]))

    sys.stdout = oldstdout

with open(output_file, "r") as datafile:
   
    print(datafile.read())

    