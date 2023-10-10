# with open("weather_data.csv", mode="r") as file:
#     weather_data = file.readlines()
# weather_data = [f.strip() for f in weather_data]
#
# print(weather_data)
#
# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     data.__next__()  # skip first row
#     for index, row in enumerate(data):
#         print(row[1])
#         temperatures.append(int(row[1]))
#     print(temperatures)
#
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/ len(temp_list)
# avg_temp = round(avg_temp, 2)
# print(temp_list)
# print(avg_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(f"temp is {monday_temp}C or {(monday_temp *1.8)+32}F")

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#read in the csv to pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# wrong_grey_squirrel_count = data["Primary Fur Color"] == "Gray"
black_squirrel_df = data.loc[data["Primary Fur Color"] == "Black"]
black_squirrel_count = sum(black_squirrel_df["Hectare Squirrel Number"])
gray_squirrel_df = data.loc[data["Primary Fur Color"] == "Gray"]
gray_squirrel_count = sum(gray_squirrel_df["Hectare Squirrel Number"])
red_squirrel_df = data.loc[data["Primary Fur Color"] == "Cinnamon"]
red_squirrel_count = sum(red_squirrel_df["Hectare Squirrel Number"])
NA_squirrel_df = data.loc[data["Primary Fur Color"] == ""]
NA_squirrel_count = sum(NA_squirrel_df["Hectare Squirrel Number"])
print(black_squirrel_count)
print(gray_squirrel_count)
print(red_squirrel_count)
print(NA_squirrel_count)

squirrel_counted = {
    "Fur Color": ["Black", "Grey", "Red", "NA"],
    "Count": [black_squirrel_count, gray_squirrel_count, red_squirrel_count, NA_squirrel_count]
}
print(squirrel_counted)
squirrel_counted_df = pandas.DataFrame(squirrel_counted)
squirrel_counted_df.to_csv("squirrel_counted.csv")
