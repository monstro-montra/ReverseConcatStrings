def main():
    while True:  # start a while loop
        try:  # implement try-except for error handling
            # get user input
            s1 = input("Enter the first string: ")
            s2 = input("Enter the second string: ")
            s3 = input("Enter the third string: ")
            if not s1 or not s2 or not s3:  # if s1 and s2 and s3 are not empty
                raise ValueError

            result = reverse_concat(s1, s2, s3)  # call reverse_concat function
            print(result)
            break  # break out of the loop

        except ValueError:  # if value error is thrown:
            print("Invalid input, please input three strings.")


def reverse_concat(s1, s2, s3):  # function for reverse concatenating the three strings
    return s3 + " " + s2 + " " + s1  # add a space in between each one


if __name__ == '__main__':  # define main() as the main function
    main()
