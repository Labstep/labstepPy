import labstep

# Login to your Labstep account
user = labstep.login('myaccount@labstep.com', 'mypassword')

# Get a list of your experiments
new_requests = user.getOrderRequests(count=1000, status='new')

print(new_requests)
