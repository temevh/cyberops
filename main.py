from selection import select_option

options = ["read file", "analyze file"]
selected_option = select_option(options)

print(f"\nYou selected: {selected_option}")

if selected_option == "read file":
    print("Reading the file...")
elif selected_option == "analyze file":
    print("Analyzing the file...")
