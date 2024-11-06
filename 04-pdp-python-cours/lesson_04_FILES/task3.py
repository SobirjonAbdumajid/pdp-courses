# import csv

# from pprint import pprint
# data = []
# dir = {}
# counter = '2013'
# index = 0
# with open('hospitals.csv', encoding='utf-8') as file:
    
#     for dt in csv.DictReader(file, delimiter=';'): # (;) ajartib olish
#         for k, v in dt.items():
#             # print(k)
#             print(v)
#             break
#         # data.append(dt[counter])
#         # break
# print(dir)
# print(data)
# # print(counter)
        
# from pprint import pprint
# import csv
# dir = {}
# data = []
# counter = ['2012', '2013', '2014', '2015', '2016', '2017']

# with open('hospitals.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=';')

#     for dt in reader:
#         pprint(dt)
        # for key, value in dt.items():            
            # if key in counter:
                # # print(key)
                # data.append(value)
                # dir[dt['Hududlar']] = data
        # print(dt['Hududlar'], dt["2012"])
        # break
        # if len(data) == len(counter):
        #     break

# import csv
# dir = {}
# data = []
# counter = ['2012', '2013', '2014', '2015', '2016', '2017']

# with open('hospitals.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=';')

#     for dt in reader:
#         # print(dt)``
#         # for key, value in dt.items():      
#         for i in counter:      
#             # print(dt[i])
#             data.append(dt[i])
#             dir[dt['Hududlar']] = data
# data.clear()
        # break
        # if len(data) == len(counter):
        #     break
        # break
# print(data)
# print(dir)

# import csv

# dir = {}
# counter = ['2012', '2013', '2014', '2015', '2016', '2017']

# with open('hospitals.csv', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=';')

#     for dt in reader:
#         region = dt['Hududlar']
#         data = []
#         total_hospitals = 0

#         for key, value in dt.items():            
#             if key in counter:
#                 hospitals = int(value) if value.strip() else 0
#                 total_hospitals += hospitals
#                 data.append(hospitals)

#         dir[region] = total_hospitals

# # Sort the regions based on the total number of hospitals in descending order
# sorted_regions = sorted(dir.items(), key=lambda x: x[1], reverse=True)

# # Display the top 3 regions with the largest number of hospitals
# print("Top 3 Regions with the Largest Number of Hospitals (2012-2017):")
# for i in range(3):
#     region, total_hospitals = sorted_regions[i]
#     print(f"{i+1}. {region}: {total_hospitals} hospitals")
import csv

with open('hospitals.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')

    regions = []
    hospitals_by_region = {}

    for row in reader:
        region = row['Hududlar']
        hospitals = [int(row[str(year)]) for year in range(2012, 2018)]
        total_hospitals = sum(hospitals)
        hospitals_by_region[region] = total_hospitals
        regions.append(region)

    regions.sort(key=lambda x: hospitals_by_region[x], reverse=True)

    print("Top 3 Regions with the Largest Number of Hospitals (2012-2017):")
    for i in range(3):
        region = regions[i]
        total_hospitals = hospitals_by_region[region]
        print(f"{i+1}. {region}: {total_hospitals} hospitals")