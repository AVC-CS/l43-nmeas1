def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    count = 0
    while count < 5:
        numbers = int(input('Enter a number: '))
        total += numbers
        count += 1
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
