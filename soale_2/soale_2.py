import csv

# step 1 : Read a CSV file containing sales information.

dict={}
with open('sales_info.csv', 'r') as csv_file1:
    info_file1=csv.reader(csv_file1)
    line1=next(info_file1)
    print(line1)


    for row in info_file1:
        print(row)

dict3={}
list1=[]
list2=[]

# step 2: Calculate the total revenue for each product using a dictionary comprehension.

with open('sales_info.csv', 'r') as csv_file2:
    info_file2=csv.DictReader(csv_file2)
    for row in info_file2:
        dict = row


        dict1=dict['product']
        list1=dict['price']
        list1=int(list1)
        list2=dict['number_of_sales']
        list2=int(list2)
        list3=list1*list2
        # total revenue for each product

        dict3[dict1]=list3

# spet 3 :Sort the products based on revenue and write the sorted results to a
# new CSV file.

# sorted results.

results=sorted(dict3.items(),key=lambda x:x[1])


# new CSV file.
with open('results.csv', 'w') as csv_file3:
    info_file3=csv.writer(csv_file3)
    info_file3.writerow(results)


