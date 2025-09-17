# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project (tries to) adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.34.0] - XXXX-XX-XX
### Added
- `CustomIdentifierSet` model and repository


## [3.33.0] - 2025-06-11

### Added

- `shareWith` and `assign` methods added to `Folder`
- `addUsers` method to `Organization` model
- Action `view` now supported in `setWorkspaceRolePermission`

## [3.32.1] - 2025-05-22

### Fixed

- `getDataFrame` method now works on multisheet tables for `ExperimentTable` and `ProtocolTable`

## [3.32.0] - 2025-05-20

### Added

- `getVersions` method to `Protocol` model

## [3.31.0] - 2024-12-28

### Added

- `getLineageParents` and `getLineageChildren` methods to `ResourceItem`

### Removed

- `linkToInventoryField` and `getLinkedInventoryFields` from `ExperimentDataField` (manual linking no longer required)

## [3.30.0] - 2024-12-28

### Changed

- To support Protocol Draft, added getter getCurrentVersion to return draft_version or last_version

## [3.29.0] - 2024-12-13

### Added

- JupyterInstance data

## [3.28.2] - 2024-11-05

### Added

- Option to save export PDF as file

## [3.28.1] - 2024-11-04

### Fixed

- PDF export request too large error

## [3.28.0] - 2024-09-19

### Changed

- serializerGroups requires 'default'

## [3.27.0] - 2024-09-13

### Changed

- `JupyterInstance` model and repository for edit

## [3.26.0] - 2024-09-04

### Added

- `newCollaboratorRole()`, `getCollaboratorRoles()`, `newExperimentTemplate()`, `getExperimentTemplates()`,
  `newEntityStateWorkflow()`, `getEntityStateWorkflows()` to `Workspace` model
- `newExperimentTemplate()`, `getExperimentTemplates()`,`newEntityStateWorkflow()`, `getEntityStateWorkflows()` to `User` model
- `EntityStateWorkflow` model and repository
- `EntityState` model and repository
- `CollaboratorRole` model and repository
- `CollaboratorRoleRequirement` model and repository
- `SignatureRequirement` model and repository

## [3.25.3] - 2024-05-22

### Added

- `getEntityCount` method

## [3.25.2] - 2024-04-30

### Fixed

- `getDataFieldValue()` was crashing when there were default options but no selected values
- Bug in `User.getNotification` method

## [3.25.1] - 2024-03-01

### Fixed

- `getDataFieldValue()` was crashing when there were no options values

## [3.25.0] - 2024-02-16

### Added

- `PurchaseOrder` model and repository
- `newPurchaseOrder`, `getPurchaseOrder`, `getPurchaseOrders` to `User` model
- `Collaborator` model and repository
- `assign` method to assignable entities
- `ExperimentTemplate` model
- `WorkspaceRolePermission` model and repository

### Changed

- Rename `PermissionRole` to `WorkspaceRole`

### Fixed

- Bug in `User.update` method
- `Device.getDeviceCategory` would crash if there was no device category

## [3.24.1] - 2024-01-09

### Added

- `description` parameter to `Device.addDeviceBooking` and `DeviceBooking.edit`

## [3.24.00] - 2024-01-08

### Added

- `ApiKey` model and repository
- `newAPIKey`, `getAPIKey`, `getAPIKeys` to `User` model
- `JupyterSchedule` model and repository
- `newJupyterSchedule` and `getJupyterSchedule` methods added to `JupyterNotebook` model
- `run` method added to `JupyterNotebook` model
- `Notification` model and repository
- `getNotification` and `getNotifications` to `User` model
- `DeviceBooking` model and repository
- `addDeviceBooking`, `getDeviceBooking`, `getDeviceBookings` to `Device` model

## [3.23.3] - 2023-12-08

### Fixed

- Export handles TIFF images by converting to png

## [3.23.2] - 2023-11-30

### Fixed

- Bug in helper methods when converting between Data Tables and Data Frames

## [3.23.0] - 2023-10-10

### Added

- `PermissionRole` model and repository
- `newPermissionRole` to `Organization` model
- `setPermissionRole` to `WorkspaceMember` model

## [3.22.0] - 2023-08-08

### Added

- `ProtocolCondition` model and repository
- `ExperimentCondition` model and repository
- `addConditions` and `getConditions` methods added to `ProtocolVersion`,`Protocol`, `ExperimentProtocol` and `Experiment` models

### Changed

- `quantity_unit` and `quantity_amount` parameters in `ResourceItem` are now `unit` and `amount`, respectively. `quantity_unit` and `quantity_amount` can still be used

### Fixed

- `getInventoryFields` crashing for Experiments if fetched in a list

## [3.21.3] - 2023-06-06

### Changed

- `labstep.login` method. Use `labstep.authenticate` instead

## [3.21.2] - 2023-06-06

### Fixed

- `getData` methods

## [3.21.1] - 2023-05-05

### Added

- `DeviceCategory` model and repository
- `getDeviceCategory` and `setDeviceCategory` methods on `Device` model
- `device_category_id` parameter added to newDevice methods

### Fixed

- Bugs related to fetching locations and setting position

## [3.21.0] - 2023-05-05

### Added

- `filterEntities` method

### Changed

- `count` is now infinite by default

## [3.20.2] - 2023-04-04

### Fixed

- getTime helper method was not taking into account local time zone correctly
- Ejected file and experiment from ElasticSearch

## [3.20.1] - 2023-04-04

### Fixed

- Experiment Step -> Protocol Step

## [3.20.0] - 2023-03-03

### Added

- `NotificationAlert` model and repository
- `getNotificationAlert` and `setNotificationAlert` methods on `Metadata` model

## [3.19.5] - 2022-03-03

### Fixed

- Protocol getDataFields bug

## [3.19.4] - 2022-03-03

### Fixed

- Bug in `addMetadata` method - crashes if no thread on parent

## [3.19.3] - 2022-11-11

### Fixed

- Bug in `Resource.getItemTemplate` method - crashes if no template. Now returns None

## [3.19.2] - 2022-11-11

### Fixed

- Bug in `Protocol.export` method - crashing on inline image file paths not found

## [3.19.1] - 2022-11-11

### Fixed

- Bug in `Protocol.export` method. Now includes PDF option

## [3.19.0] - 2022-11-11

### Added

- `setLocation` and `getLocation` methods for `ResourceItem` which include ability to set the position within the location
- `getInnerLocations`, `addInnerLocation` , `setOuterLocation` and `createPositionMap` methods for `ResourceLocation`
- `linearToCartesianCoordinates` helper function
- `alphanumericToCartesianCoordinates` helper function

## [3.18.0] - 2022-09-09

### Added

- `resource_category_id` filter parameter to `getResources` method on `User` and `Workspace`

## [3.18.1] - 2022-10-10

### Fixed

- `exportEntity` filenames were too long for windows

## [3.18.0] - 2022-09-09

### Added

- `resource_category_id` filter parameter to `getResources` method on `User` and `Workspace`

### Fixed

- `resource.getData` and `resourceItem.getData`

## [3.17.6] - 2022-08-08

### Fixed

- `jupyter.getParent` for protocols

## [3.17.5] - 2022-08-08

### Added

- `getJupyterNotebooks` and `addJupyterNotebook` methods to `Experiment`,`ExperimentProtocol` and `Protocol` models
- `ProtocolVersion` model

### Removed

- `Workspace.setAutosharing` method

## [3.17.4] - 2022-08-08

### Fixed

- Better filepath sanitisation for export

## [3.17.3] - 2022-08-08

### Fixed

- Html fetched without embedded images by default unless PDF needed

## [3.17.2] - 2022-07-07

### Changed

- When exporting file names now contain ID and name

### Fixed

- Bug in entity export method "NoneType has no attribute 'replace'"

## [3.17.0] - 2022-05-05

### Added

- `Sequence` model
- `dataFrameToDataTable` helper

## [3.16.2] - 2022-05-05

### Fixed

- `ResourceItem` metadata bug

## [3.16.1] - 2022-05-05

### Fixed

- `ExperimentTable.edit` bug

### Fixed

- `getFile` method can now get deleted files

## [3.16.0] - 2022-04-04

### Added

- `ChemicalReaction` model
- `Chemical` model
- `addChemicalReaction` and `getChemicalReactions` methods on `Experiment` and `ExperimentProtocol`
- `addChemicalMetadata` and `getChemicalMetadata` methods on `Resource`

### Fixed

- `getFile` method can now get deleted files

## [3.15.2] - 2022-04-04

### Fixed

- Export bugs

## [3.15.1] - 2022-04-04

### Fixed

- Export foldering name bug

## [3.15.0] - 2022-04-04

### Added

- `getUserAgent` and `setUserAgent` in `labstep.service.config.configService`

## [3.14.0] - 2022-04-04

### Added

- New Entity `Molecule`

### Changed

- Entity name for `ExperimentInventoryField`

### Fixed

- Setting value for options field bug

## [3.13.0] - 2022-02-02

### Added

- Include PDF in experiment export

## [3.12.0] - 2022-02-02

- `ExperimentMaterial` class renamed to `ExperimentInventoryField`
- `ProtocolMaterial` class renamed to `ProtocolInventoryField`
- `Experiment.addMaterials` deprecated in favour or `Experiment.addInventoryField`
- `Protocol.addMaterials` deprecated in favour or `Experiment.addInventoryField`

## [3.11.1] - 2022-02-02

- Experiment children serialization backwards compatibility

## [3.11.0] - 2022-01-01

### Added

- Custom export methods

### Fixed

- Thread is none bug

## [3.10.0] - 2021-12-12

### Added

- `Collection.getSubCollections` method
- `Collection.addSubCollections` method

## [3.9.0] - 2021-12-12

### Added

- `Experiment.lock` method
- `Experiment.unlock` method
- `Experiment.complete` method
- `Experiment.getExperimentLinks` method
- `Experiment.addExperimentLink` method
- `ExperimentLink` model
- htmlToPDF service

### Fixed

- getEntities capped out at 100000
- `Experiment.getEntry` from list of experiments

### Changed

- Passing parameters as `None` will now set those fields to `NULL`

## [3.8.0] - 2021-11-11

### Added

- `Workspace.getResourceItems` method
- `Metadata.getValue` method
- `Metadata.setValue` method

### Changed

- `getComments` no longer does API call if comment count is zero
- `getComments` updates entity if thread not found
- `getMetadata` no longer does API call if metadata already on entity

## [3.7.0] - 2021-11-11

### Added

- `ExperimentTable.getDataFrame` method
- `ProtocolTable.getDataFrame` method

### Changed

- Generic Entity Class inheritance structure updated

## [3.6.0] - 2021-10-28

### Added

- `ExperimentProtocol.getExperiment` method
- `ExperimentDataField.getValue` method
- `ExperimentDataField.setValue` method
- `EntityList` class
- Entities in a list can now be accessed by name / label via `get` method

### Changed

- `User.newFile` filepath no longer required param

## [3.5.0] - 2021-10-08

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

## [3.4.0] - 2021-05-21

### Added

- `User.getResourceItems` method

## [3.3.2] - 2021-04-19

### Changed

- `OrganizationUser.setAdmin` method
- `OrganizationUser.revokeAdmin` method

## [3.3.1] - 2021-04-13

### Changed

- `entityNameInFolderName` now in global config

## [3.3.0] - 2021-04-13

### Added

- `Member.remove` method for removing members from workspaces
- `Organization.getPendingInvitations` method
- `nameInFolderName` parameter to export methods
- Model and Methods for organization invitations

### Changed

- `inviteUsers` method no longer in `OrganisationRepository`

### Fixed

- Sanitisation of file / folder names
- OrganizationUser entityName bug
- Disable OrganizationUser bug
- Boolean GET parameter handling

## [3.2.0] - 2021-04-12

### Added

- Impersonate user method for Organisation Admins

### Changed

- Export methods now include entity name in folder path

### Fixed

- UTF-8 encoding of HTML exports

## [3.1.0] - 2021-03-30

### Added

- ExperimentSignatureRequest Entity Model + Methods
- `getSignatureRequest` method for User Entity Model
- `requestSignature` method for User Entity Model

## [3.0.5] - 2021-03-25

### Added

- Organization Entity Model + Methods
- OrganizationUser Entity Model + Methods
- `getOrganization` method for User Entity Model
- `resource_category_id` parameter for newResource method

### Fixed

- Pass `group_id` to bulk entity create endpoint
- Links in html export point to correct file

## [3.0.4] - 2021-03-24

### Fixed

- Bugs in entity export
