from selection import select_option
from analyzer import transport_packets

filename = ""
analysis_results = {} 

def readFile():
    global filename 
    filename = input("File name: ")

while True:
    options = ["read file", "analyze file",  "quit"]
    analysis_options = ["transport-layer packets"]
    selected_option = select_option(options)

    if selected_option == "read file":
        readFile()
        print("Reading the file...\n")
    elif selected_option == "analyze file":
        if filename == "":
            print("Read file first\n")
        else:
            analysis_selection = select_option(analysis_options)  # Use 'analysis_options' here
            if analysis_selection == analysis_options[0]:
                transport_analysis = transport_packets(filename)
                print(transport_analysis)
                input("press enter to continue")

    
    elif selected_option == "quit":
        print("Exiting program...")
        break
