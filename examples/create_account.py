
import csv
import labstep
TOKEN = 'WORKSPACE_SHARELINK_CODE'
with open('users') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      try:
        user = labstep.user.newUser(first_name=row[0], last_name=row[1], email=row[2], password=row[3], share_link_token=TOKEN)
      except:
        print(row[2],' Failed')