import json
from selection import select_option
from analyzer import transport_packets

filename = ""
results = {}

def readFile():
    global filename 
    #filename = input("File name: ")
    filename = "capture.pcapng"

while True:
    options = ["read file", "analyze file", "save results", "quit"]
    analysis_options = ["transport-layer packets"]
    selected_option = select_option(options)

    if selected_option == "read file":
        readFile()
        print("Reading the file...\n")

    elif selected_option == "analyze file":
        if filename == "":
            print("Read file first\n")
        else:
            analysis_selection = select_option(analysis_options)
            if analysis_selection == "transport-layer packets":
                transport_analysis = transport_packets(filename)
                print(transport_analysis)
                if "transport_analysis" not in results:
                    results["transport_analysis"] = transport_analysis

                input("Press enter to continue")

    elif selected_option == "save results":
        with open("results.txt", "w") as f:
            json.dump(results, f, indent=4)
        print("Results saved successfully!")

    elif selected_option == "quit":
        print("Exiting program...")
        break
