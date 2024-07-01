import csv
from collections import defaultdict
import os
import datetime

def list_files_in_folder(folder):
    freqs = defaultdict(int)
    try:
        files = os.listdir(folder)
        for file in files:
            category = str(file).split("_")
            if len(category) > 1:
                if '?' in category[1]:
                    freqs[category[1].split("?")[0]] += 1
                    continue
                freqs[category[1].strip()] += 1
        return freqs
    except Exception as e:
        print(f"Error reading folder: {e}")

def write_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Count"])
        for category, count in data:
            writer.writerow([category, count])

if __name__ == "__main__":
    folder = "/Users/smoolaga/Desktop/safe_computing/site_data"
    categories = list_files_in_folder(folder)

    # Sort the categories by count in descending order
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    
    # Create a filename with the current date and time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = f"reports/category_counts_{timestamp}.csv"

    # Write the sorted data to a CSV file
    write_to_csv(sorted_categories, csv_filename)
    print(f"Data has been written to {csv_filename}")
