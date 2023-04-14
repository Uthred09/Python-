#  x - create a new file, return error if file exist
# a - will create a file if the specified file doesnot exist
# w - will create a file  if the specified file doesnot exist

#  write to an existing file

# a "append" - will append to the end of the file
# w "write" will overwrite any existing content in a file

# to delet a file impoet os module
# os.remove
# to delete folder  os.rmdir(only empty dir can removed)


ls = ['susan','bashyal', 90, 'newyork']
with open ("example", 'a') as file_:
    for x in ls:
        values = "".join(str(x))
        file_.write(values + "," + " ")
    
