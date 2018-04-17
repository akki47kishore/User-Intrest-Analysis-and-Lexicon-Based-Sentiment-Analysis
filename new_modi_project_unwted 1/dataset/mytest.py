import subprocess

line = (subprocess.check_output(['tail', '-1', "wordset.txt"]))
for lines in line:
  maxword = lines

     
