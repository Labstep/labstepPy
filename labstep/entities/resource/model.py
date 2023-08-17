#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.helpers import getTime
from labstep.generic.entityPrimary.model import EntityPrimary
from labstep.generic.entityWithMetadata.model import EntityWithMetadata
from labstep.entities.resourceItem.model import ResourceItem
from labstep.constants import PLACEHOLDER_SVG, UNSPECIFIED


class Resource(EntityPrimary, EntityWithMetadata):
    """
    Represents a Resource on Labstep.

    To see all attributes of the resource run
    ::
        print(my_resource)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_resource.name)
        print(my_resource.id)
    """

    __entityName__ = "resource"

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Resource.

        Parameters
        ----------
        name (str)
            The new name of the Resource.

        Returns
        -------
        :class:`~labstep.entities.resource.model.Resource`
            An object representing the edited Resource.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.edit(name='A New Resource Name')
        """
        import labstep.entities.resource.repository as resourceRepository

        return resourceRepository.editResource(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Resource.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.delete()
        """
        import labstep.entities.resource.repository as resourceRepository

        return resourceRepository.editResource(self, deleted_at=getTime())

    def getResourceCategory(self):
        """
        Get the ResourceCategory of the Resource.

        Returns
        -------
        :class:`~labstep.entities.resourceCategory.model.ResourceCategory`
            An object representing the Resource Category on Labstep.

        Example
        -------
        ::

            # Get a Resource
            resource = user.getResource(170)

            # Get the Resource Category of the resource
            resourceCategory = resource.getResourceCategory()
        """
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        return resourceCategoryRepository.getResourceCategory(
            self.__user__, self.template["id"]
        )

    def setResourceCategory(self, resource_category_id, extraParams={}):
        """
        Add a Labstep ResourceCategory to a Resource.

        Parameters
        ----------
        resource_category_id (int)
            The id of :class:`~labstep.entities.resourceCategory.model.ResourceCategory`
            to set for
            the Resource.

        Returns
        -------
        :class:`~labstep.entities.resource.model.Resource`
            An object representing the Resource on Labstep.

        Example
        -------
        ::

            # Get a ResourceCategory
            resource_category = user.getResourceCategory(170)

            # Set the Resource Category
            my_resource = my_resource.setResourceCategory(resource_category.id)
        """
        import labstep.entities.resource.repository as resourceRepository

        return resourceRepository.editResource(
            self, resource_category_id=resource_category_id, extraParams=extraParams
        )

    def newOrderRequest(self, quantity=1, extraParams={}):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        quantity (int)
            The quantity of the new OrderRequest.

        Returns
        -------
        :class:`~labstep.entities.orderRequest.model.OrderRequest`
            An object representing the new OrderRequest on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            order_request = my_resource.newOrderRequest(quantity=2)
        """
        import labstep.entities.orderRequest.repository as orderRequestRepository

        return orderRequestRepository.newOrderRequest(
            self.__user__,
            resource_id=self.id,
            quantity=quantity,
            extraParams=extraParams,
        )

    def getItems(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
        """
        Returns the items of this Resource.

        Parameters
        ----------
        count (int)
            The number of ResourceItems to retrieve.
        search_query (str)
            Search for ResourceItems with this 'name'.
        extraParams (dict)
            Dictionary of extra filter parameters.

        Returns
        -------
        List[:class:`~labstep.entities.resourceItem.model.ResourceItem`]
            A list of ResourceItem objects.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            items = my_resource.getItems()
        """
        import labstep.entities.resourceItem.repository as resourceItemRepository

        return resourceItemRepository.getResourceItems(
            self.__user__,
            resource_id=self.id,
            count=count,
            search_query=search_query,
            extraParams=extraParams,
        )

    def newItem(
        self,
        name=UNSPECIFIED,
        availability="available",
        amount=UNSPECIFIED,
        unit=UNSPECIFIED,
        resource_location_guid=UNSPECIFIED,
        extraParams={},
        **kwargs
    ):
        """
        Create a new Labstep ResourceItem.

        Parameters
        ----------
        name (str)
            The new name of the ResourceItem.
        availability (str)
            The status of the ResourceItem. Options are:
            "available" and "unavailable".
        amount (float)
            The quantity of the ResourceItem.
        unit (str)
            The unit of the quantity.
        resource_location_guid (str)
            The guid of the ResourceLocation of the ResourceItem.

        Returns
        -------
        :class:`~labstep.entities.resourceItem.model.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            item = my_resource.newItem(name='Test Item')
        """
        import labstep.entities.resourceItem.repository as resourceItemRepository

        if 'quantity_amount' in kwargs:
            amount = kwargs['quantity_amount']

        if 'quantity_unit' in kwargs:
            unit = kwargs['quantity_unit']

        return resourceItemRepository.newResourceItem(
            self.__user__,
            name=name,
            resource_id=self.id,
            availability=availability,
            amount=amount,
            unit=unit,
            resource_location_guid=resource_location_guid,
            extraParams=extraParams,
        )

    def getItemTemplate(self):
        """
        Get the template used for initialising new items of the resource.

        Returns
        -------
        :class:`~labstep.entities.resourceItem.model.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            itemTemplate = my_resource.getItemTemplate()

            itemTemplate.addMetadata('Expiry Date')

        """
        self.update()
        if self.resource_item_template is None:
            return None

        return ResourceItem(self.resource_item_template, self.__user__)

    def enableCustomItemTemplate(self):
        """
        Enable a custom item template for this resource.
        If disabled the template for the Resource Category will be used.

        Returns
        -------
        None

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.enableCustomItemTemplate()

            itemTemplate = my_resource.getItemTemplate()

            itemTemplate.addMetadata('Expiry Date')

        """
        self.update()
        if self.resource_item_template is None:
            self.newItem(extraParams={"is_template": 1})
        else:
            self.getItemTemplate().edit(extraParams={"deleted_at": None})

    def disableCustomItemTemplate(self):
        """
        Disable custom item template for this resource.
        If disabled the template for the Resource Category will be used.

        Returns
        -------
        None

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.disableCustomItemTemplate()
        """
        self.getItemTemplate().delete()

    def getData(self):
        """
        Returns data linked to this resource via experiments.

        Returns
        -------
        List[:class:`~labstep.entities.experimentDataField.model.ExperimentDataField`]

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.getData()
        """
        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.getDataFields(self)

    def addChemicalMetadata(self, structure=UNSPECIFIED, iupac_name=UNSPECIFIED, cas=UNSPECIFIED, density=UNSPECIFIED, inchi=UNSPECIFIED, molecular_formula=UNSPECIFIED, molecular_weight=UNSPECIFIED, smiles=UNSPECIFIED, safety={}, svg=UNSPECIFIED):
        """
        Add chemical metadata to a Resource.

        Parameters
        ----------
        structure (str)
            The chemical structure as SMILES or MOL
        iupac_name (str)
            The IUPAC Name
        cas (str)
            The CAS Number
        denstity (str)
            The density of the chemicals
        inchi (str)
            The InChI of the chemical
        molecular_formula (str)
            The Molecular Formula
        molecular_weight (str)
            The Molecular Weight
        smiles (str)
            The SMILES string describing the chemical
        svg (str)
            An SVG preview of the chemical structure

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`]

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.addChemicalMetadata(
                            structure='C1=CC=CC=C1',
                            iupac_name="benzene",
                            cas="71-43-2",
                            density="0.879 at 68 °F (USCG, 1999)",
                            inchi="InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H",
                            molecular_formula="C6H6",
                            molecular_weight="78.11",
                            smiles='C1=CC=CC=C1',
                            safety={
                                 "precautionary": {
                                     "General": [],
                                     "Prevention": [
                                         "P203",
                                     ],
                                     "Storage": [
                                         "P403+P235",
                                     ],
                                     "Disposal": [
                                         "P501"
                                     ]
                                 },
                                 "ghs_hazard_statements": [
                                     "H372"
                                 ],
                                 "pictograms": [
                                     "GHS02",
                                 ]
                             }
                            )
        """
        metadata = {
            "IUPACName": iupac_name if iupac_name is not UNSPECIFIED else None,
            "InChI": inchi if inchi is not UNSPECIFIED else None,
            "MolecularFormula": molecular_formula if molecular_formula is not UNSPECIFIED else None,
            "CAS": cas if cas is not UNSPECIFIED else None,
            "Density": density if density is not UNSPECIFIED else None,
            "SMILES": smiles if smiles is not UNSPECIFIED else None,
            "MolecularWeight": molecular_weight if molecular_weight is not UNSPECIFIED else None,
            "Safety": safety if safety is not UNSPECIFIED else {}
        }

        return self.addMetadata('Structure', 'molecule', extraParams={'molecule': {
            'name': 'Untitled',
            'data': structure if structure is not UNSPECIFIED else smiles,
            'svg': svg if svg is not UNSPECIFIED else PLACEHOLDER_SVG,
            'pubchem': {
                'reactants': [metadata],
                'products': []
            }
        }})

    def getChemicalMetadata(self):
        '''
        Returns the chemical metadata associated with the resource

        Returns
        -------
        {
            "Structure": string,
            "IUPACName": string,
            "InChI": string ,
            "MolecularFormula": string,
            "CAS": string,
            "Density": string,
            "SMILES": string,
            "MolecularWeight": string,
            "Safety": {
                "precautionary": {
                    "General": [string],
                    "Prevention": [string],
                    "Response": [string],
                    "Storage": [string],
                    "Disposal": [string]
                },
                "ghs_hazard_statements": [string],
                "pictograms": [string]
            }
            "SVG": string
        }

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            my_resource.getChemicalMetadata()
        '''
        self.update()
        metadata = self.molecule['pubchem']['reactants'][0]

        metadata['Structure'] = self.molecule['data']

        metadata['SVG'] = self.molecule['svg']

        return metadata
