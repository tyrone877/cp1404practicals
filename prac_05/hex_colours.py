COLOUR_TO_HEX = {"Alice Blue": "#f0f8ff", "Beige": "#f5f5dc", "Black": "#000000", "Brown": "#a52a2a",
                 "Chocolate": "#d2691e", "Coral": "#ff7f50", "Dark Green": "#006400", "Gray": "#bebebe",
                 "Khaki": "#f0e68c", "Lavender": "#e6e6fa"}

colour = input("Enter colour: ").title()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(COLOUR_TO_HEX[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour: ").title()
