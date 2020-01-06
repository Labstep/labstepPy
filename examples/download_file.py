import labstep

user = labstep.login('myaccount@labstep.com', 'mypassword')

# A List of the authenticated user's files can be accessed
# via the getFiles method
my_files = user.getFiles()
my_file = my_files[0]

# Alternatively retrieve a list of files from a workspace
my_workspace = user.getWorkspaces()[0]
workspace_files = my_workspace.getFiles()

# Access the data via the getData method
rawData = my_file.getData()

# Or save directly as a new file
my_file.save()

# If you come across a file_id attached to another labstep entity
# you can retrieve the file using the User getFile method
my_file = user.getFile(123)
my_file.save()
