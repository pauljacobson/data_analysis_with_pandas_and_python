from datetime import datetime
import re
import pandas as pd
from rich.pretty import pprint
from rich.traceback import install

# The reference file contains a file directory that my files are contained in
import reference as ref

def list_files():
    """
    Lists all files in a journal directory
    Scrape the journal files for the interaction counts
    """

    journal_files = {}

    # List all files in the journal directory
    for file in ref.Path(ref.journal_dir).iterdir():
        # Check if the filename includes "Happiness Journal Notes"
        if f"Happiness Journal Notes" in file.name:
            # Extract the date from the filename
            # as a datetime object
            date_str = datetime.strptime(file.name.split(" ")[0], "%Y%m%d_%H%M")
            # Add the date_str to the journal_files dictionary
            # with the file as the value
            journal_files[date_str] = str(file)

    # Sort the journal_files dictionary by the date_str
    sorted_journal_files = dict(sorted(journal_files.items()))

    # pprint(sorted_journal_files)
    return sorted_journal_files


def generate_data():
    """List all entries in the sorted_journal_files dictionary and
    create a dataframe that indicates the type of each entry based
    on regex pattern matches for each entry type"""
    sorted_journal_files = list_files().values()
    # Define regex patterns to search for
    entry = re.compile(r"^(\d{,3}\.|\D)\s(?P<entry>.+)$", re.MULTILINE)
    datetime_pattern = r"\d{8}_\d{4}"


    # pprint(sorted_journal_files.items())
    # Create a dictionary to store the results
    journal_entries = {}
    # dates = sorted_journal_files.keys()
    # journal_files = sorted_journal_files.values()
    # pprint(dates)

    # Open each file and read the contents
    for journal_file in sorted_journal_files:
        # Extract datetime from the filename
        dates = re.findall(datetime_pattern, journal_file)
        # Open each journal_file and read the contents
        if dates:
            datetime_str = dates[0]
            # Open each journal_file and read the contents
            with open(journal_file, 'r') as f:
                # Read the contents of the file and search for 
                # entries using matches for the entry pattern
                contents = f.read()
                matches = re.findall(entry, contents)
                if matches:
                    journal_entries[datetime_str] = matches

    return datetime_pattern, journal_entries


def analyze_entries():
    """Read the journal_entries dictionary and create a dataframe
    that indicates the type of each entry based on regex patterns"""
    # Define entry patterns
    zen_pattern = re.compile(r"\d{,3}\.\s\[\d{7,}-(?P<zen_int>zen)")
    hc_pattern = re.compile(r"\d{,3}\.\s\[\d{7,}-(?P<hc_int>hc)")
    fm_pattern = r"\d{,3}\.\s\[\d{7,}-(?P<fm_int>fm)"
    sales_pattern = r"\d{,3}\.\s\[\d{7,}-(?P<int_type>(fm|zen|hc)).+(?P<sales_int>#project_sales)"
    datetime_pattern, file_dict = generate_data()

    interaction_types = ["zen", "hc", "fm", "sales"]
    
    # This is where the wheels come off. I can't seem to read each row,
    # create a column for each of the required columns in my example table in Readme
    # and then state under the "Boolean" columns either `True` or `False` to indicate
    # whether the row contains a match based on the regex patterns above
    
    
    # # Define the list of files to read
    # # Create a dataframe from the file_dict
    # df = pd.DataFrame.from_dict(file_dict, orient="index")
    # # Sort the dataframe by the Index
    # df.sort_index(inplace=True)

    # # Iterate through each row in the dataframe and create columns for each interaction type
    # for row in df.itertuples():
    #     # pprint(row[2])
    #     df["zen"] = df[1].str.extract(zen_pattern)["zen_int"]
    #     df["hc"] = df[1].str.extract(hc_pattern)["hc_int"]


    # pprint(df)
    
    
if __name__ == "__main__":
    # list_files()
    # generate_data()
    analyze_entries()
