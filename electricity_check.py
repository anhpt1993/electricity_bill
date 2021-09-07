def analyze_number(number, list):
    ladder = []
    for i in list:
        if number > i:
            ladder.append(i)
            number -= i
        else:
            ladder.append(number)
            break
    else:
        ladder.append(number)
    return ladder

def input_number():
    while True:
        try:
            number = int(input("Enter your electricity index here (kWh): "))
            if number >= 0:
                return number
                break
            else:
                print("\nInvalid Value. Try again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try again!!!\n")

if __name__ == '__main__':
    number = input_number()

    check = [1678, 1734, 2014, 2536, 2834, 2927]
    list = [50, 50, 100, 100, 100]

    analyze = analyze_number(number, list)

    total = 0
    for i in range(len(analyze)):
        total += check[i] * analyze[i]

    print("Your total bill is {:.2f} VND".format(1.1 * total))