import csv
pybank_path=r"PyBank/Resources/budget_data.csv"
with open(pybank_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_profit=[]
    total_months=[]
    monthly_profit_change=[]
    

    for row in csvreader:
        total_profit.append(int(row[1]))
        total_months.append(row[0])
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
    max_inc_value=max(monthly_profit_change) 
    max_dec_value=min(monthly_profit_change)    
    sumofprofit=sum(total_profit)
    l=len(total_months)
    average=sumofprofit/l
    max_inc_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_dec_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 
print("Here is the Financial Analysis")
print("----------------------------")
print(f"Total Months: {l} months")
print(f"Total: ${sumofprofit}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_inc_month]} (${(str(max_inc_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_dec_month]} (${(str(max_dec_value))})")
output_file = r"PyBank/analysis/ Financial_Analysis_Summary.txt"
with open(output_file,"w") as file:
     
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {l} months")
    file.write("\n")
    file.write(f"Total: ${sumofprofit}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_inc_month]} (${(str(max_inc_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_dec_month]} (${(str(max_dec_value))})")

        
       
       
        
 