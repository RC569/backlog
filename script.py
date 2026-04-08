import json

# Example: load your JSON from a file called "albums.json"
with open("albums.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Markdown file to write to
output_file = "albums.md"

# Define the table header
headers = ["Date Added", "Artist", "Album", "Genre", "Subgenre", "Status", "Notes"]

with open(output_file, "w", encoding="utf-8") as f:
    # Write title
    f.write("# Music Log\n\n")
    f.write("A simple table to track albums.\n\n")
    
    # Write table header
    f.write("| " + " | ".join(headers) + " |\n")
    f.write("|" + "|".join(["-"*len(h) for h in headers]) + "|\n")
    
    # Write each row
    for entry in data:
        row = [entry.get(h, "") for h in headers]  # leave empty if key missing
        f.write("| " + " | ".join(row) + " |\n")

print(f"Markdown file '{output_file}' generated successfully!")