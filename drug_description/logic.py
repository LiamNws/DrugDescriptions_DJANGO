import pandas as pd
import re

def process_description(search_term):
    excel = "C:/Users/liamn/IdeaProjects/TestSite/PT_portfolio/drug_description/source/DrugDescriptions.xlsx"

    df = None
    
    try:
        df = pd.read_excel(excel)
    except Exception as e:
        print("An error has occurred while reading the file", str(e))
        
        
    if df is not None:
        matching = df[df["Drug Name"].str.contains(search_term, case=False, na=False)]

        results = []

        if not matching.empty:
            for i, row in matching.iterrows():

                form = row["Form"]

                if pd.isna(row["Shape"]) or row["Shape"] == "":
                    shape = ""
                else:
                    shape = row["Shape"]

                colour = row["Colour"]

                if row["Imprint"] == "none":
                    imprint = ""
                    imp_found = False
                else:
                    imprint = row["Imprint"]
                    imp_found = True

                name = row["Drug Name"]

                sentence1 = f"{name}: {colour} {shape} {form}, '{imprint}' imprinted. \n -LN"
                sentence1 = re.sub(r"(?<!\n)\s+", " ", sentence1)

                sentence2 = f"{name}: {colour} {shape} {form}, no imprint. \n -LN"
                sentence2 = re.sub(r"(?<!\n)\s+", " ", sentence2)

                if imp_found:
                    results.append(sentence1)
                elif not imp_found:
                    results.append(sentence2)

        return results