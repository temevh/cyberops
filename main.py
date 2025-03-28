from selection import select_option
from analyzer import analyze

filename = ""
analyzed = False

def readFile():
    global filename 
    filename = input("File name: ")

while True:
    options = ["read file", "analyze file", "display results", "quit"]
    selected_option = select_option(options)

    print(f"\nYou selected: {selected_option}")

    if selected_option == "read file":
        readFile()
        print("Reading the file...\n")
    elif selected_option == "analyze file":
        if filename == "":
            print("Read file first\n")
        else:
            print("Analyzing the file...\n")
            analyze(filename)
    elif selected_option == "quit":
        print("Exiting program...")
        break
