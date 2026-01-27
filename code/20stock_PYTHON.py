import pandas as pd

sector_mapping = {
    'Banks': [
        'AMEN BANK', 'ATB', 'ATTIJARI BANK', 'BH BANK', 'BIAT', 
        'BNA', 'BT', 'STB', 'UIB', 'WIFAK INTERNATIONAL BANK', 'UBCI','BTE'
    ],
    'Insurance': [
        'ASSURANCES MAGHREBIA', 'ASSURANCES MAGHREBIA VIE', 'BH ASSURANCE', 
        'BNA ASSURANCES', 'STAR', 'TUNIS RE', 'ASTREE'
    ],
    'Leasing & Financial Services': [
        'ATTIJARI LEASING', 'BEST LEASE', 'BH LEASING', 
        'HANNIBAL LEASE', 'TUNISIE LEASING ET FACTORING','ATL'
    ],
    'Investment/Holding Companies': [
        'TAWASOL GROUP HOLDING', 'Tunisie SICAF', 
        'SPDIT-SICAF', 'TUNINVEST-SICAR'
    ],
    'Industrials': [
        'CARTHAGE CEMENT', 'CIMENTS DE BIZERTE', 'Office Plast ', 'ONE TECH HOLDING', 
        'SIAME', 'SOMOCER', 'SOTEMAIL', 'SOTIPAPIER', 'SOTUVER', 'STIP', 
        'TPR', 'ASSAD', 'ICF', 'MPBS', 'CIL', 'SITS', 'SOTUMAG', 'SANIMED'
    ],
    'Consumer Goods': [
        'DELICE HOLDING', 'EURO-CYCLES', 'LAND OR', 'NEW BODY LINE', 
        'Poulina', 'SFBT', 'SAH', 'ESSOUKNA', 'SIMPAR'
    ],
    'Consumer Services': [
        'ARTES', 'CITY CARS', 'ENNAKL AUTOMOBILES', 'MAGASIN GENERAL', 
        'MONOPRIX', 'STA', 'TUNISAIR', 'UADH', 'SAM'
    ],
    'Technology': [
        'AETECH', 'CELLCOM', 'SMART TUNISIE', 'TELNET HOLDING'
    ],
    'Basic Materials': [
        'AIR LIQUIDE TUNISIE', 'ALKIMIA'
    ],
    'Telecommunications': [
        'SOTETEL'
    ],
    'Oil & Gas': [
        'SOTRAPIL'
    ],
    'Health Care': [
        'SIPHAT', 'UNIMED'
    ]
}


df = pd.read_excel('FM project.xlsm', sheet_name='20 Stock Selection', header=0)

df.columns = df.columns.str.strip()


company_to_sector = {}
for sector, companies in sector_mapping.items():
    for company in companies:
        company_to_sector[company] = sector

if 'Company_Name' in df.columns:
    company_col = 'Company_Name'
elif 'Company Name' in df.columns:
    company_col = 'Company Name'
else:
    company_col = df.columns[0]
    print(f"Using first column: {company_col}")


df['Sector'] = df[company_col].map(company_to_sector)


cols = df.columns.tolist()
cols.remove('Sector')
df = df[['Sector'] + cols]


df = df.sort_values(by=['Sector', company_col])


df.to_excel('companies_organized_by_sector.xlsx', index=False)
