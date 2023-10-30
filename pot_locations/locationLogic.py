import pandas as pd
import os


def process_location(search_term):

    # excel = os.path.join("source", "DrugLocations.xlsx") --causing issues--

    excel = r"C:/Users/liamn/IdeaProjects/TestSite/PT_portfolio/PT_portfolio\source/DrugLocations.xlsx"
    try:
        df = pd.read_excel(excel)
    except FileNotFoundError:
        print("File not found.")
        exit(1)
    except Exception as e:
        print("An error has occurred while reading the file")
        exit(1)

    matching = df[(df["Medication"].str.contains(search_term, case=False, na=False))]

    result = []
    if not matching.empty:
        for i, row in matching.iterrows():
            
            name = row["Medication"]
            location = row["Location"]
            result.append({"name": name, "location": location})

    else:
        result.append("No matches found")

    return result