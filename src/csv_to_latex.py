import argparse
import os
import subprocess

content = r'''
\newcommand\firstName{%(fname)s}
\newcommand\lastName{%(lname)s}
'''

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--fname',) 
parser.add_argument('-ln', '--lname',) 


args = parser.parse_args()

with open('reports/info.tex','w') as f:
    f.write(content%args.__dict__)

cmd = ['make', 'reports/template_format.pdf']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('reports/template_format.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink('reports/info.tex')