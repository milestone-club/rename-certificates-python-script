import pandas as pd
import os

df = pd.read_excel('CERTIFICATE-DETAILS.xlsx')

df.columns = df.columns.str.strip()

names = df['Name'].tolist()

certs_path = r'D:\MILESTONE_CLUB\CERTIFICATES\ilovepdf_extracted-pages'  # Correct location

print("Files in the certificate directory:")
for file in os.listdir(certs_path):
    print(file)

for index, name in enumerate(names, start=1):
    old_filename = f'CERTFICATES-{index}.pdf'
    new_filename = f'{name}.pdf'
    
    old_file_path = os.path.join(certs_path, old_filename)
    new_file_path = os.path.join(certs_path, new_filename)
    
    if os.path.exists(old_file_path):
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {old_filename} to {new_filename}')
    else:
        print(f'File not found: {old_filename}')
