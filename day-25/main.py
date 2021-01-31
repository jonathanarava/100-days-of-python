# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)    # type '_csv.reader' object
# #     temperatures =[]
# #     # _csv.reader objects can be looped through
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")  # type  'pandas.core.frame.DataFrame' object
# # print(type(data["temp"]))      # type  'pandas.core.series.Series' object
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # # Approach 1
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # approach_1 = sum(temp_list) / len(temp_list)
# # print(approach_1)
# #
# # # Approach 2
# # approach_2 = data["temp"].mean()
# #
# # print(approach_2)
#
# # print(data["temp"].max())
#
# # #Get Data in Column
# # print(data["condition"])
# # print(data.condition)
# #
# #
# # #Get Data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])   #print(data[criteria])
# # print(data.day == "Monday")
#
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# #
# # m_t_F = monday.temp * (9/5) + 32
# # print(m_t_F)
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
# TODO: How many squirrels are there for each fur
# print(data["Primary Fur Color"])
# squirrel_count = data["Primary Fur Color"].value_counts()
# print(squirrel_count)
# squirrel_count.to_csv("squirrel_count.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
