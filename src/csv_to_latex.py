import argparse
import os
import subprocess
import pandas as pd

content = r'''
\newcommand\firstName{%(fname)s}
\newcommand\lastName{%(lname)s}
'''

def check_for_error_cmd(cmd, return_code, file_name):
    if not return_code == 0:
        os.unlink(f'reports/{file_name}')
        raise ValueError('Error {} executing command: {}'.format(return_code, ' '.join(cmd))) 

def generate_pdf(file_name):
    cmd = ['make', 'reports/template_format.pdf']
    proc = subprocess.Popen(cmd)
    proc.communicate()
    return_code = proc.returncode
    check_for_error_cmd(cmd, return_code, file_name)


users_data = pd.read_csv('data/example_data.csv')

for _, row in users_data.iterrows():
    otro_dict = {'fname': row["Nombre"], 'lname': row["Apellido"]}
    file_name = "constancia_{}_{}.pdf".format(row["Nombre"], row["Apellido"])
    with open('reports/info.tex'.format(),'w') as f:
        f.write(content%otro_dict)
    generate_pdf(file_name)
    os.rename("reports/template_format.pdf",f"reports/{file_name}")
    os.unlink('reports/info.tex')
    