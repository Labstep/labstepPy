# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project (tries to) adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.21.1] - 2023.05.30

### Added
- `DeviceCategory` model and repository
- `getDeviceCategory` and `setDeviceCategory` methods on `Device` model.
- `device_category_id` parameter added to newDevice methods

### Fixed
- Bugs related to fetching locations and setting position

## [3.21.0] - 2023.05.18

### Added
- `filterEntities` method

### Changed
- `count` is now infinite by default.
## [3.20.2] - 2023.04.23
### Fixed
- getTime helper method was not taking into account local time zone correctly.
- Ejected file and experiment from ElasticSearch
## [3.20.1] - 2023.04.11
#### Fixed
- Experiment Step -> Protocol Step
## [3.20.0] - 2023.03.13
### Added
- `NotificationAlert` model and repository
- `getNotificationAlert` and `setNotificationAlert` methods on `Metadata` model.
## [3.19.5] - 2022.03.02
### Fixed
- Protocol getDataFields bug
## [3.19.4] - 2022.03.02
### Fixed
- Bug in `addMetadata` method - crashes if no thread on parent.

## [3.19.3] - 2022.11.30
### Fixed
- Bug in `Resource.getItemTemplate` method - crashes if no template. Now returns None.
## [3.19.2] - 2022.11.30
### Fixed
- Bug in `Protocol.export` method - crashing on inline image file paths not found.
## [3.19.1] - 2022.11.28
### Fixed
- Bug in `Protocol.export` method. Now includes PDF option.
  
## [3.19.0] - 2022.11.28
### Added
- `setLocation` and `getLocation` methods for `ResourceItem` which include ability to set the position within the location.
- `getInnerLocations`, `addInnerLocation` , `setOuterLocation` and `createPositionMap` methods for `ResourceLocation`.
- `linearToCartesianCoordinates` helper function
- `alphanumericToCartesianCoordinates` helper function


## [3.18.0] - 2022.09.22

### Added
- `resource_category_id` filter parameter to `getResources` method on `User` and `Workspace`
## [3.18.1] - 2022.10.24
### Fixed
- `exportEntity` filenames were too long for windows.
## [3.18.0] - 2022.09.22

### Added
- `resource_category_id` filter parameter to `getResources` method on `User` and `Workspace`

### Fixed
- `resource.getData` and `resourceItem.getData`
## [3.17.6] - 2022.08.24
### Fixed
- `jupyter.getParent` for protocols
## [3.17.5] - 2022.08.23
### Added
- `getJupyterNotebooks` and `addJupyterNotebook` methods to `Experiment`,`ExperimentProtocol` and `Protocol` models.
- `ProtocolVersion` model
### Removed
- `Workspace.setAutosharing` method
## [3.17.4] - 2022.08.19
### Fixed
- Better filepath sanitisation for export
## [3.17.3] - 2022.08.15
### Fixed
- Html fetched without embedded images by default unless PDF needed
## [3.17.2] - 2022.07.28
### Changed
- When exporting file names now contain ID and name
### Fixed
- Bug in entity export method "NoneType has no attribute 'replace'"
## [3.17.0] - 2022.05.23
### Added
- `Sequence` model
- `dataFrameToDataTable` helper
## [3.16.2] - 2022.05.23
### Fixed
- `ResourceItem` metadata bug
## [3.16.1] - 2022.05.20
### Fixed
- `ExperimentTable.edit` bug

### Fixed
- `getFile` method can now get deleted files
## [3.16.0] - 2022.04.29
### Added
- `ChemicalReaction` model
- `Chemical` model
- `addChemicalReaction` and `getChemicalReactions` methods on `Experiment` and `ExperimentProtocol`
- `addChemicalMetadata` and `getChemicalMetadata` methods on `Resource`

### Fixed
- `getFile` method can now get deleted files
## [3.15.2] - 2022.04.19
### Fixed
- Export bugs.
  
## [3.15.1] - 2022.04.19
### Fixed
- Export foldering name bug.
## [3.15.0] - 2022.04.14
### Added
- `getUserAgent` and `setUserAgent` in `labstep.service.config.configService`
## [3.14.0] - 2022.04.04

### Added
- New Entity `Molecule`
### Changed
- Entity name for `ExperimentInventoryField`
### Fixed
- Setting value for options field bug.

## [3.13.0] - 2022.02.18

### Added
- Include PDF in experiment export

### [3.12.0] - 2022.02.18

- `ExperimentMaterial` class renamed to `ExperimentInventoryField`
- `ProtocolMaterial` class renamed to `ProtocolInventoryField`
- `Experiment.addMaterials` deprecated in favour or `Experiment.addInventoryField`
- `Protocol.addMaterials` deprecated in favour or `Experiment.addInventoryField`
### [3.11.1] - 2022.02.06

- Experiment children serialization backwards compatibility

### [3.11.0] - 2022.01.07
### Added
- Custom export methods 
### Fixed
- Thread is none bug

### [3.10.0] - 2021.12.09

### Added
- `Collection.getSubCollections` method
- `Collection.addSubCollections` method

### [3.9.0] - 2021.12.08
### Added
-`Experiment.lock` method
-`Experiment.unlock` method
-`Experiment.complete` method
- htmlToPDF service
-`Experiment.getExperimentLinks` method
-`Experiment.addExperimentLink` method
-`ExperimentLink` model

### Fixed
- getEntities capped out at 100000
- `Experiment.getEntry` from list of experiments.
### Changed
- Passing parameters as `None` will now set those fields to `NULL`

### [3.8.0] - 2021.11.19

### Added
-`Workspace.getResourceItems` method
-`Metadata.getValue` method
-`Metadata.setValue` method

### Changed
-`getComments` no longer does API call if comment count is zero
-`getComments` updates entity if thread not found.
-`getMetadata` no longer does API call if metadata already on entity.
### [3.7.0] - 2021.11.15

### Added
-`ExperimentTable.getDataFrame` method
-`ProtocolTable.getDataFrame` method

### Changed
- Generic Entity Class inheritance structure updated
### 3.6.0 - 2021-10-28

### Added
-`ExperimentProtocol.getExperiment` method
-`ExperimentDataField.getValue` method
-`ExperimentDataField.setValue` method
- `EntityList` class
  -  Entities in a list can now be accessed by name / label via `get` method

### Changed
-`User.newFile` filepath no longer required param
### 3.5.0 - 2021-10-08

### Added
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
  
### Changed
- `Experiment.addDataElement` -> `Experiment.addDataField`
- `ExperimentProtocol.addDataElement` -> `ExperimentProtocol.addDataField`
- `Protocol.addDataElement` -> `Protocol.addDataField`
- Renamed class `Member` to `WorkspaceMember`

### 3.4.0 - 2021-05-21
#### Added
- `User.getResourceItems` method
### 3.3.2 - 2021-04-19
#### Changed
- `OrganizationUser.setAdmin` method
- `OrganizationUser.revokeAdmin` method
### 3.3.1 - 2021-04-13
#### Changed
- `entityNameInFolderName` now in global config
### 3.3.0 - 2021-04-13
#### Added
- `Member.remove` method for removing members from workspaces.
- `Organization.getPendingInvitations` method 
- `nameInFolderName` parameter to export methods.
- Model and Methods for organization invitations
#### Changed
- `inviteUsers` method no longer in `OrganisationRepository`
#### Fixed
- Sanitisation of file / folder names
- OrganizationUser entityName bug
- Disable OrganizationUser bug
- Boolean GET parameter handling
### 3.2.0 - 2021-04-12
#### Added
- Impersonate user method for Organisation Admins

#### Changed
- Export methods now include entity name in folder path

#### Fixed
- UTF-8 encoding of HTML exports

### 3.1.0 - 2021-03-30
#### Added
- ExperimentSignatureRequest Entity Model + Methods
- `getSignatureRequest` method for User Entity Model
- `requestSignature` method for User Entity Model
### 3.0.5 - 2021-03-25

#### Changed

#### Added
- Organization Entity Model + Methods
- OrganizationUser Entity Model + Methods
- `getOrganization` method for User Entity Model
- `resource_category_id` parameter for newResource method
#### Fixed

- Pass `group_id` to bulk entity create endpoint.
- Links in html export point to correct file.
### 3.0.4 - 2021-03-24

#### Changed

#### Added

#### Fixed

- Bugs in entity export