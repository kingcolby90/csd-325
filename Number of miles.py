# Colby King January 27 2025 Module 4.2 Programming Assignment for miles to kilometers #
def miles_to_kilometers(miles):
    # 1 mile = 1.60934 kilometers
    return miles * 1.60934
def main():
    miles = float(input("Please enter the number of miles:"))
    print("Kilometers:", miles_to_kilometers(miles))
    if miles < 0:
                print("Please enter a enter a valid number.")
if __name__ == "__main__":
    main()
    
