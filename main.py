"""
1 : Reading the file
2 : extract ip address and error and success logs
3 : save the output in csv/excel file
"""

import re
import pandas as pd
import pprint

logfile = open("serverlogs.log", "r")

ip_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+)')
success_pattern = re.compile(r'requestsuccessful: (\d+)')
failed_pattern = re.compile(r'requestfailed: (\d+)')

#list for CSV column
ip_address_list = []
success_list = []
failed_list = []

for log in logfile:
    #extracting ip address
    ip_add = ip_pattern.search(log).group()
    ip_address_list.append(ip_add)

    #extracting successful logs
    success = int(success_pattern.search(log).group(1))
    success_list.append(success)
    
    #extracting failed logs
    failed = int(failed_pattern.search(log).group(1))
    failed_list.append(failed)

total_s = sum(success_list)
success_list.append(total_s)
total_f = sum(failed_list)
failed_list.append(total_f)
ip_address_list.append("TOTAL")


#Dataframe
df =  pd.DataFrame(columns=['IP Address', 'Success', 'Failed'])
df['IP Address'] = ip_address_list
df['Success'] = success_list
df['Failed'] = failed_list

#saving
df.to_csv("output.csv", index=False)

## Display the DataFrame in a pretty printed format
pprint.pprint(df)

