#import our operating system and csv modules.
import os
import csv

#define paths to resource files
pybank = os.path.join("resources","budget_data.csv")

with open(pybank) as csvfile:

        #Read in the csv file.
        #Define name for csv file
        csvreader = csv.reader(csvfile, delimiter =',')
        csv_header = next(csvreader)

        #declare variables 
        month_start = 0
        total_pl = 0
        change = 0
        change_list = []
        month_list = []
        prev_month = 0
        this_month = 0

        #For loop = row becaue it iterates through them but we specify the column with "[#]"...
        #Use to iterate through the rows... capture specefied values for financial analysis
        for index, row in enumerate(csvreader):
            month_start += + 1
            total_pl += int(row[1])
            month_str = str(row[0])

            #Nested conditional.  If index is 0, then set [previous & current month] equal to column 2.
            #This is to create two variables that hold the value for the current and previous months in order to calculate the change.  
            if index ==0:
                prev_month=int(row[1])
                this_month=int(row[1])
            
            #If not, store this month as column 2 value...calculate change....set previous month to the current month(which will then become the previous)...
            #...and add the next month and value to the "Change & Month" list.
            else:
                this_month=int(row[1])
                change = this_month-prev_month
                prev_month = this_month
                change_list.append(change)
                month_list.append(month_str)

        #Re-Assigning variables and their calculations after the For Loop. 
        sum_list = sum(change_list)
        count_list = len(change_list)
        average = round((sum_list/count_list),2)
        max_increase = max(change_list)
        max_decrease = min(change_list)

        #[index funtion] = .index() for month & amount to create a unique row indentifier to reference when tracking the months.
        max_increase_index = change_list.index(max_increase)
        max_decrease_index = change_list.index(max_decrease)

        #Referencing the Index to identify the corresponding month 
        max_increase_month = month_list[max_increase_index]
        max_decrease_month = month_list[max_decrease_index]

        #Print Results
        print("Financial Analysis")
        print("-------------------------------")
        print("Total Months: ", month_start)
        print("Total: $",total_pl)
        print("Average Change: $",average)
        print("Greatest Increase in Profits: ",max_increase_month," ($",max_increase,")")
        print("Greatest Decrease in Profits: ",max_decrease_month ," ($",max_decrease,")")




    
