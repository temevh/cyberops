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

while True:
    options = ["read file", "analyze file", "save results", "quit"]
    analysis_options = ["transport-layer packets", "list IP's"]
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
                transport_analysis = transport_packets(capture)
                print(transport_analysis)
                if "transport_analysis" not in results:
                    results["transport_analysis"] = transport_analysis

            elif analysis_selection == "list IP's":
                ip_results = ip_list(capture)
                print(ip_results)
                if "ip_list" not in results:
                    results["ip_list"] = ip_results

            input("Press enter to continue")

    elif selected_option == "save results":
        with open("results.txt", "w") as f:
            json.dump(results, f, indent=4)
        print("Results saved successfully!")

    elif selected_option == "quit":
        print("Exiting program...")
        break
