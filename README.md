🏠 Property Finder Automation
This project automates the process of finding properties and sending inquiry emails based on predefined criteria. The script searches a German real estate website and matches properties to the specified conditions.

📋 Project Overview
This automation tool simplifies the process of searching for properties by:

Matching Properties to Given Criteria: The script reads from an Excel file to identify the criteria, such as location, price, size, etc., and then searches the website accordingly.
Automated Email Inquiries: Once matching properties are found, it automatically sends inquiry emails to the property owners or agents.
📁 Excel File Information
The Excel file contains the criteria for matching properties.
The file headers are mostly in German, as the website being searched is a German website.
🛠️ Getting Started
Prerequisites
To run this project, you'll need:

Python (I used 3.11.3)
Required Python libraries:
requests
pandas


Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/Vonomia.git
cd Vonomia
Install Required Libraries:

bash
Copy code
pip install -r requirements.txt
🔍 How to Use
Update the Excel File:

Open the provided Excel file (client_info.xlsx) and update it with your desired property search criteria.
Run the Script:

bash
Copy code
python script.py
Check the Output:

The script will start sending inquiry emails while showing good logs along the way.

Note: All headers should be in German as the website is a German real estate site.

⚠️ Important Notes
Ensure the Excel file is correctly formatted with the required headers.
Verify your email settings in the script to successfully send inquiry emails.
🤝 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

📧 Contact
For any questions or feedback, please reach out at waqassahmed03@gmail.com
