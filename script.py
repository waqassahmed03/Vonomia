import pandas as pd
import requests
import json

file_path = str(input("Enter the File Name : "))

def excel_to_dataframe(file_path):
    # Read the Excel file
    excel_data = pd.ExcelFile(file_path)
    # Initialize an empty DataFrame
    combined_df = pd.DataFrame()
    # Iterate over each sheet in the Excel file
    for sheet_name in excel_data.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.columns = df.columns.str.strip()

        # Append the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    
    return combined_df

df = excel_to_dataframe(file_path)

for index, row in df.iterrows():
    wrk_ids = []
    first_name       = row['Vorname']
    last_name        = row['Nachname']
    telephone_number = row['Telefonnummer']
    email            = row['Email']
    address          = row['Aktuelle Adresse']
    max_price        = row['Preis']
    earning          = row['Einkomm']
    minRooms         = row['Zimmer']
    city             = row['Wohnort'].split(",")[0]
    emailText        = str(row['emailText'])

    print( index+1," Working on : ", first_name,last_name,telephone_number)

    total = 500
    cur = 0
    while total>cur:

        params = {
            'rentType': 'miete',       
            'city': city,      # location to enter
            'lift': '0',
            'parking': '0',
            'cellar': '0',
            'perimeter': '15',        # area in km around
            'immoType': 'wohnung',    # property type
            'priceMax': max_price,    # Max Price
            'minRooms': minRooms,
            'floor': 'Beliebig',
            'bathtub': '0',
            'bathwindow': '0',
            'bathshower': '0',
            'furnished': '0',
            'kitchenEBK': '0',
            'toiletSeparate': '0',
            'disabilityAccess': 'egal',
            'seniorFriendly': '0',
            'balcony': 'egal',
            'garden': '0',
            'subsidizedHousingPermit': 'egal',
            'limit': '50',
            'offset': cur,
            'orderBy': 'dist_asc',
        }

        response = requests.get('https://www.wohnraumkarte.de/api/getImmoList', params=params)

        json_data = json.loads(response.text)
        all_results = json_data['results']
        paging = json_data['paging']['info']
        total = paging['count']
        cur_ids = [result['wrk_id'] for result in all_results]
        wrk_ids.extend(cur_ids)
        print("Total : ",total, " Offset : ",cur)

        cur +=50
        
    print("Total Results : ",len(wrk_ids))
    for wrk_id in wrk_ids:
        data = {
            'wrkID': wrk_id,
            'name': last_name,
            'prename': first_name,
            'phone': telephone_number,
            'email': email,
            'emailText': emailText,
            'currentEmployment': 'angestellte',
            'incomeType': '1',
            'monthlyNetIncome': 'M_2',
            'referrer': 'null',
        }
        response = requests.post('https://www.wohnraumkarte.de/Api/sendMailRequest', data=data)
        print("Response for : ",index+1, first_name,last_name,telephone_number," : ",response.text,"For the Work ID : ",wrk_id)
