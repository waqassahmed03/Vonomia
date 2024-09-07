# 🏠 Vonovia Automation

This project automates the process of finding properties and sending inquiry emails based on predefined criteria. The script searches a German real estate website and matches properties to the specified conditions.

## 📋 Project Overview

This automation tool simplifies the process of searching for properties by:

- **Matching Properties to Given Criteria**: The script reads from an Excel file to identify the criteria, such as location, price, size, etc., and then searches the website accordingly.
- **Automated Email Inquiries**: Once matching properties are found, it automatically sends inquiry emails to the property owners or agents.

## 📁 Excel File Information

- The Excel file contains the criteria for matching properties.
- The file headers are mostly in German, as the website being searched is German.

## 🛠️ Getting Started

### Prerequisites

To run this project, you'll need:

- **Python** (I used 3.11.3)
- **Required Python libraries**:
  - `requests`
  - `pandas`

### Installation

#### Clone the Repository:
Copy code
```bash
git clone https://github.com/your-username/Vonovia.git
```
Copy code
```bash
cd Vonovia
```
#### Install Required Libraries:

Copy code
```bash
pip install -r requirements.txt
```

### 🔍 How to Use

#### Update the Excel File:


- Open the provided Excel file (client_info.xlsx) and update it with your desired property search criteria.
  
#### Run the Script:

Copy code
```bash
python script.py
```

#### Enter your file name 
- in this case "client_info.xlsx" 
- make sure the file is in the same directory


### Check the Output:
The script will start sending inquiry emails while showing good logs along the way.

*Note: All headers should be in German as the website is a German real estate site.*

## ⚠️ Important Notes
- Ensure the Excel file is correctly formatted with the required headers.
- The headings are case-sensitive.

## 🤝 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📧 Contact
For any questions or feedback, please reach out at waqassahmed03@gmail.com.

