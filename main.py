from selection import select_option
from analyzer import analyze

filename = ""
analysis_results = {} 

def readFile():
    global filename 
    filename = input("File name: ")

while True:
    options = ["read file", "analyze file", "show results", "quit"]
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
            analysis_results = analyze(filename)  # Store results
            print("Analysis complete.\n")
    elif selected_option == "show results":
        if not analysis_results:
            print("No analysis results available. Analyze a file first.\n")
        else:
            print("\n--- Analysis Results ---")
            print(f"UDP PACKETS: {analysis_results['udp_count']}")
            print(f"TCP PACKETS: {analysis_results['tcp_count']}")
            if analysis_results["udp_packets"]:
                print(f"First UDP Packet: {analysis_results['udp_packets'][0]}")
            else:
                print("No UDP packets found.")
            if analysis_results["tcp_packets"]:
                print(f"First TCP Packet: {analysis_results['tcp_packets'][0]}")
            else:
                print("No TCP packets found.")
            input("\nPress Enter to continue...")
    elif selected_option == "quit":
        print("Exiting program...")
        break
