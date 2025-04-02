import json
import pyshark
from selection import select_option
from analyzer import transport_packets
from ip_analyze import list_all_ips

filename = ""
results = {}

def readFile():
    global filename 
    global capture
    # filename = input("File name: ")
    filename = "capture.pcapng"
    capture = pyshark.FileCapture(filename)

def show_ip_options(capture): #Too lazy to come up with a fix, pass the capture to avoid error
    ip_options = list(ip_functions.keys()) + ["Back"]
    ip_selection = select_option(ip_options)

    if ip_selection in ip_functions and ip_selection:
        result = ip_functions[ip_selection](capture)
        results[ip_selection] = result
        print(f"Analysis result for {ip_selection}:\n{result}")
        input("Press ENTER to continue")

analysis_functions = {
    "transport-layer packets": transport_packets,
    "IP analysis options": show_ip_options 
}

ip_functions = {
    "list IP's": list_all_ips
}

while True:
    options = ["read file", "analyze file", "save results", "debug", "quit"]
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

                if result:
                    results[analysis_selection] = result

    elif selected_option == "save results":
        with open("results.txt", "w") as f:
            json.dump(results, f, indent=4)
        print("Results saved successfully to results.txt!")
        input("Press ENTER to continue")

    elif selected_option == "quit":
        print("Exiting program...")
        break