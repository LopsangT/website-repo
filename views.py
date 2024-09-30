def convert():
    us_dollar = float(input("Enter the amount you want to convert: $"))
    pounds = us_dollar / 1.87
    return f"{pounds:.2f}"



def main():
    print ("This program converts US dollars into pounds")
    print(convert())


main()