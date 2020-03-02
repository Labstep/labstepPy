import labstep

user = labstep.login('apitest@labstep.com', 'apitestpass')

# Create a Protocol to Share
protocol = user.newProtocol('Protocol to Share')

# Create a new Workspace to Share it with
workspace = user.newWorkspace('Workspace to Share to')

# Pass the workspace id to the shareWith method on the protocol
# Pass permission level 'view' as second arg
protocol.shareWith(workspace.id, 'view')

# Retrieve the sharing permissions for the protocol to see which workspaces it
# is shared with
resourceCategory = user.newResourceCategory('Test')

resourceCategory.shareWith(workspace.id, 'view')

permissions = resourceCategory.getPermissions()

# We can alter the permission to 'edit' if we want
permissions[0].set('edit')

# Or we can revoke the permission entirely
permissions[0].revoke()

# We can also transfer ownership completely to a different workspace
protocol.transferOwnership(workspace.id)
