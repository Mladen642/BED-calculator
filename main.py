def BED(n, d, alfabeta):

    # Calc
    BED = round(float(n * d * (1 + (d / (alfabeta)))), 2)

    print("###############################")
    print(f"Total BED equals to {BED} Gy!")
    print("###############################")


if __name__ == "__main__":
    while True:
        try:
            # num of fractions
            n = int(input("Number of fractions (n): "))

            # fraction
            d = float(input("Dose fraction (d): "))

            # ratio
            alfabeta = int(input("Alfa/beta: "))
            print()

            BED(n, d, alfabeta)
            break
        except:
            print("Please enter right format of the variables!")
