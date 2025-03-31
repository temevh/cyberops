import json
import pyshark
from selection import select_option
from analyzer import transport_packets, ip_list

filename = ""
results = {}

def readFile():
    global filename 
    global capture
    # filename = input("File name: ")
    filename = "capture.pcapng"
    capture = pyshark.FileCapture(filename)

analysis_functions = {
    "transport-layer packets": transport_packets,
    "list IP's": ip_list
}

while True:
    options = ["read file", "analyze file", "save results", "quit"]
    selected_option = select_option(options)

    if selected_option == "read file":
        readFile()
        print("Reading the file...\n")

    elif selected_option == "analyze file":
        if filename == "":
            print("Read file first\n")
        else:
            analysis_selection = select_option(list(analysis_functions.keys()))
            if analysis_selection in analysis_functions:
                result = analysis_functions[analysis_selection](capture)
                print(result)

                if analysis_selection not in results:
                    results[analysis_selection] = result

            input("Press enter to continue")

    elif selected_option == "save results":
        with open("results.txt", "w") as f:
            json.dump(results, f, indent=4)
        print("Results saved successfully to results.txt!")
        input("Press ENTER to continue")

    elif selected_option == "quit":
        print("Exiting program...")
        break