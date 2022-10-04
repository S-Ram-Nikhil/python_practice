# Join Zoom Meeting
# https://zoom.us/j/6282753513?pwd=T0lNbEtBdE9iOXprb0lIdUhTM2FJZz09
# import pandas as pd
#
# accounts = [[1,2,3],[3,2,1]]
# accounts = [[1,5],[7,3],[3,5]]
# accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# wealth_list=[]
# for each in accounts:
#     wealth = 0
#     for i in  each:
#         wealth+=i
#     wealth_list.append(wealth)
# # print(wealth_list)
# print(max(wealth_list))
# # w_list=wealth_list
# for num in wealth_list:
#     if num==max(wealth_list):
#         print('The',(wealth_list.index(num)+1 ),"customer is the richest with a wealth of " +str(max(wealth_list)))
#
#     # print(each)

# def max_wealth(accounts):
#     wealth_list = list(map(lambda each: sum(each), accounts))
#     return (max(wealth_list))
# cust_1=[[1,2,3],[3,2,1]]
# cust_2 = [[1,5],[7,3],[3,5]]
# cust_3= [[2,8,7],[7,1,3],[1,9,5]]
# print(max_wealth(cust_1))
# print(max_wealth(cust_2))
# print(max_wealth(cust_3))

# from optparse import OptionParser
# ...
# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="write report to FILE", metavar="FILE")
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
#
# (options, args) = parser.parse_args()

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print(args.square**2)


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")
#
# (Task given by karthik: There is a list of tuples which contain details having(job_id, job_name, component_id,  job_url_name, component_name, branch_id, boolvalue)
# so the task is to extract the details based on job_name ( Ring1, Ring2, 3, 4)  and then convert it in to the excel file using python.



# class Employees:
#     def __init__(self, salary):
#         self.salary= salary
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
# e1= Employees(2000)
# e2 = Employees(1000)
# print(e1 + e2)
# e1 = Employees(1000, 'ram')
# res1 = e1.display()     # 1000   ram salary
#
# e2 = Employees(2000, 'vijay')
# res2= e2.display()
#
# res1 + res2

# e1 + e2   :    == res1 + res2

#
# import pandas as pd
# my_file= open("D:\Documents\PythonWorkspace\job_details.txt", "r")
# my_text= my_file.read()
# my_list= list(eval(my_text))
# print(my_list)
# df=pd.DataFrame(my_list,columns=["job_id","job_name", "comp_id",  "job_url_name", "component_name", "branch_id", "boolvalue"])
# print(df)
# dfobj=df.sort_values(by="job_name")
# print(dfobj)
#
# dfobj.to_excel("output.xlsx")


#
# import docx2txt
# import pandas as pd
#
# text_file=docx2txt.process(r"D:\Downloads\job_details.docx")
# list_data=(eval(text_file))
# print(list_data)
# data_frame= pd.DataFrame.from_records(list_data,columns=["job_id","joba_name", "comp_id",  "job_url_name", "component_name", "branch_id", "boolvalue"])
# print(data_frame)
# data_frame=data_frame.sort_values(by="joba_name")
# # data_frame.to_excel("fileexcel.xlsx")

# listData = [4, 4, 5, 6]
# for index, value in enumerate(listData):
#     print(index, ":", value)

class myClass:
    def __init__(self, value):
        print("Object initialization...")
        self.value = value
        print(value)


myClass("myobj")





