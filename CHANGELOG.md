# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project (tries to) adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 3.5.0 - 2021-10-08

## Added
- `ExperimentDataField` class
  - `ExperimentDataField.linkToMaterial` method
  - `ExperimentDataField.getLinkedMaterials` method
- `ProtocolDataField` class
  - `ProtocolDataField.linkToMaterial` method
  - `ProtocolDataField.getLinkedMaterials` method
- `Resource.getData` method
- `ResourceItems.getData` method
- `Experiment.getTables` method
- `Comment.delete` method
- `Workspace.addMembers` method
- `ResourceLocation.getItems` method
  
## Changed
- `Experiment.addDataElement` -> `Experiment.addDataField`
- `ExperimentProtocol.addDataElement` -> `ExperimentProtocol.addDataField`
- `Protocol.addDataElement` -> `Protocol.addDataField`
- Renamed class `Member` to `WorkspaceMember`

## 3.4.0 - 2021-05-21
### Added
- `User.getResourceItems` method
## 3.3.2 - 2021-04-19
### Changed
- `OrganizationUser.setAdmin` method
- `OrganizationUser.revokeAdmin` method
## 3.3.1 - 2021-04-13
### Changed
- `entityNameInFolderName` now in global config
## 3.3.0 - 2021-04-13
### Added
- `Member.remove` method for removing members from workspaces.
- `Organization.getPendingInvitations` method 
- `nameInFolderName` parameter to export methods.
- Model and Methods for organization invitations
### Changed
- `inviteUsers` method no longer in `OrganisationRepository`
### Fixed
- Sanitisation of file / folder names
- OrganizationUser entityName bug
- Disable OrganizationUser bug
- Boolean GET parameter handling
## 3.2.0 - 2021-04-12
### Added
- Impersonate user method for Organisation Admins

### Changed
- Export methods now include entity name in folder path

### Fixed
- UTF-8 encoding of HTML exports

## 3.1.0 - 2021-03-30
### Added
- ExperimentSignatureRequest Entity Model + Methods
- `getSignatureRequest` method for User Entity Model
- `requestSignature` method for User Entity Model
## 3.0.5 - 2021-03-25

### Changed

### Added
- Organization Entity Model + Methods
- OrganizationUser Entity Model + Methods
- `getOrganization` method for User Entity Model
- `resource_category_id` parameter for newResource method
### Fixed

- Pass `group_id` to bulk entity create endpoint.
- Links in html export point to correct file.
## 3.0.4 - 2021-03-24

### Changed

### Added

### Fixed

- Bugs in entity export