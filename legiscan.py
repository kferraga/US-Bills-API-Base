import requests
import pandas as pd
import openpyxl
from classes.itemized_list import ItemizedList
from classes.api_call import APICall
from general_api import check_correct_api

legiscan_url = 'https://api.legiscan.com/'

def get_base_api(query = False):
    """Sets up a base legiscan API. Will request query if none is given on input."""
    if not query:
        print("Please input the desired query (i.e.\"anti-asian\" without the quotations).")
        query = input()

    # Set up the API request parameters
    legiscan_base = APICall(legiscan_url, key = 'c99429e615cca188924c1fd950c29ba5',
                            query = query)
    return legiscan_base

@check_correct_api(legiscan_url)
def get_bill_ids(base_api, **kwargs):
    """Returns a dictionary of all bill hashes and ids that match the given legiscan API."""
    print("getting bill IDs")
    # Send the API request and parse the response.
    api = base_api.create_api(**kwargs)
    data = api.request_json()

    # Gathers the bill hashes and ids from the gathered data.
    desired_bills = {}
    for result in data["searchresult"]["results"]:
        if result != "summary":
            bill_hash = result['change_hash']
            bill_id = result['bill_id']
            desired_bills[bill_hash] = bill_id
    return desired_bills

@check_correct_api(legiscan_url)
def get_bill_info(base_api, file_path, desired_bills, year = 2):
    """Gathers bill information. File name is the output file, desired bills is a dictionary of
    legiscan bill hashes and ids, base_api is a base legiscan api, and the default year is the
    current."""
    print(f"Getting bill info and exporting to {file_path} (will take some time)")

    bill_status = {
        0: "N/A", 1: "Introduced", 2: "Engrossed", 3: "Enrolled", 4: "Passed",
        5: "Vetoed", 6: "Failed", 7: "Override", 8: "Chaptered", 9: "Refer",
        10: "Report Pass", 11: "Report DNP", 12: "Draft"
    }
    bill_list = ItemizedList()
    total_number = len(desired_bills)

    for bill_id in desired_bills.values():
        api = base_api.create_api(op = 'getBill', id = bill_id, year = year)
        data = api.request_json()['bill']
        bill_list.add_kwrd_item(bill_id, origin = data['state'], title = data['title'],
                                doi = data['history'][0]['date'],
                                status = bill_status.get(data['status']), link = data['url'],
                                bill_number = data['bill_number'],
                                query = base_api.get_param('query'))
        print(f"Saved Bill {bill_list.length()} of {total_number}")

    # Create a pandas DataFrame from the list of bill information dictionaries
    bill_info_df = pd.DataFrame(bill_list.give_values())
    bill_info_df.to_excel(file_path, index = False)
    print(f"Saved {len(bill_info_df)} bills to {file_path}.")
