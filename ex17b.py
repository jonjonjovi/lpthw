from sys import argv
script, file_in,new_file = argv

print(f"file name to be copied: {file_in}")
in_data=open(file_in).read()

new=open(new_file,'w')
new.write(in_data)
new.close()
