# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import legiscan

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Runs legiscan code.
    base_api = legiscan.get_base_api("potato")
    desired_bills = legiscan.get_bill_ids(base_api, state = 'US', op = 'getSearchRaw', year = '2')
    legiscan.get_bill_info(base_api, 'super-bills.xlsx', desired_bills)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
