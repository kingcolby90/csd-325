#colby king module 4.2 sitka highs#
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))  # Read low temperatures

# Program loop
while True:
    print("\nWeather Data Menu:")
    print("1. High temperatures")
    print("2. Low temperatures")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")

    if choice == "1":
        # Plot high temperatures in red
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "2":
        # Plot low temperatures in blue
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == "3":
        print("Thank you for using the weather data viewer. Goodbye!")
        sys.exit()  # Exit the program

    else:
        print("Invalid selection. Please choose 1, 2, or 3.")