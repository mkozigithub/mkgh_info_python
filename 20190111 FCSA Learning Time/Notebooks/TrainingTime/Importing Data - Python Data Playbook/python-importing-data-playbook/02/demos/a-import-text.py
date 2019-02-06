# How to read a plain text file
# which_file = "./text/Creative Commons Attribution-ShareAlike 3.0 Unported.txt"
which_file = "D:\Git\Temp\mkgh_info_python\20190111 FCSA Learning Time\Notebooks\TrainingTime\Importing Data - Python Data Playbook\python-importing-data-playbook\02\demos\text\CreativeCommonsAttribution-ShareAlike30Unported.txt"
license_file = open(which_file, mode='r')
license_name = license_file.readline()
print(license_name)
license = license_file.read()
license_file.close()
print(license)

# Same as above, but using a context manager to avoid having to explicitly close the file
with open (which_file, 'r') as file:
    print(file.read())