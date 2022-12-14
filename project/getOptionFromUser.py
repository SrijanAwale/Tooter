def getOptionFromUser(optionList):
    """Takes a list of strings, prints them, prompts user for a selection,
    and returns the index of the selected option. returns -1 if failed/exiting."""

    print("Please select an option from the list below:")
    for idx in range(len(optionList)):
        print(str(idx+1) + ": " + optionList[idx])

    while True:
        try:
            selection = input("Enter your selection: ")
            exitCodes = ["exit", "q", "quit"]
            if selection in exitCodes: # user typed in exit code
                return -1

            option = int(selection)
            if option < 1 or option > len(optionList):
                print("Invalid selection. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        except EOFError: # ctrl-d
            return -1
        except KeyboardInterrupt: # ctrl-c
            print() # adds newline to clean up output
            return -1

        # return option back down to 0-based index
        return option - 1



# DON'T COPY THIS INTO YOUR FILE!!
if __name__ == "__main__":
    print("output from getOptionFromUser(): " + str(getOptionFromUser(["Option A", "Option B", "Option C"])))