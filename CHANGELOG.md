# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project (tries to) adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 3.12.0 2022-02-18

- `ExperimentMaterial` class renamed to `ExperimentInventoryField`
- `ProtocolMaterial` class renamed to `ProtocolInventoryField`
- `Experiment.addMaterials` deprecated in favour or `Experiment.addInventoryField`
- `Protocol.addMaterials` deprecated in favour or `Experiment.addInventoryField`
## 3.11.1 2022-02-06

- Experiment children serialization backwards compatibility

## 3.11.0 2022-01-07
## Added
- Custom export methods 
## Fixed
- Thread is none bug

## 3.10.0 2021-12-09

## Added
- `Collection.getSubCollections` method
- `Collection.addSubCollections` method

## 3.9.0 2021-12-08
## Added
-`Experiment.lock` method
-`Experiment.unlock` method
-`Experiment.complete` method
- htmlToPDF service
-`Experiment.getExperimentLinks` method
-`Experiment.addExperimentLink` method
-`ExperimentLink` model

## Fixed
- getEntities capped out at 100000
- `Experiment.getEntry` from list of experiments.
## Changed
- Passing parameters as `None` will now set those fields to `NULL`

## 3.8.0 2021-11-19

## Added
-`Workspace.getResourceItems` method
-`Metadata.getValue` method
-`Metadata.setValue` method

## Changed
-`getComments` no longer does API call if comment count is zero
-`getComments` updates entity if thread not found.
-`getMetadata` no longer does API call if metadata already on entity.
## 3.7.0 2021-11-15

## Added
-`ExperimentTable.getDataFrame` method
-`ProtocolTable.getDataFrame` method

## Changed
- Generic Entity Class inheritance structure updated
## 3.6.0 - 2021-10-28

## Added
-`ExperimentProtocol.getExperiment` method
-`ExperimentDataField.getValue` method
-`ExperimentDataField.setValue` method
- `EntityList` class
  -  Entities in a list can now be accessed by name / label via `get` method

## Changed
-`User.newFile` filepath no longer required param
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