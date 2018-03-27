

HEX_COLOURS = {"alice blue" : "#f0f8ff", "antique white4" : "#8b8378", "azure1" : "#f0ffff", "beige" : "#f5fdc", "black"
: "#000000", "blue1" : "#0000ff", "blue violet" : "#8a2be2", "brown" : "#a52a2a", "burlywood" : "#deb887"}

colour = input("Please enter colour name:").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("{:>10} colour number is {:<7}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Error not a colour in the database")
        for key in HEX_COLOURS:
            print("{:>15} is in the list".format(key))
    colour = input("Please enter colour name:").lower()