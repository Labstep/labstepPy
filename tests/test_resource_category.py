#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from fixtures import user, resourceCategory, testString

entity = resourceCategory()


class TestResourceCategory:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE CATEGORY'

    def test_delete(self):
        entityToDelete = user.newResourceCategory('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE CATEGORY'

    def test_addComment(self):
        result = entity.addComment(
            testString, './tests/test_resource_category.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testString)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

    def test_addMetadata(self):
        new_resource_category = user.newResourceCategory(testString)
        result = new_resource_category.getResourceTemplate().addMetadata(fieldName=testString,
                                                                         value=testString)
        assert result.label == testString, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getResourceTemplate().getMetadata()
        assert result[0].id is not None, \
            'FAILED TO GET METADATA'

    def test_enableItemTemplate(self):
        entity.enableItemTemplate()
        itemTemplate = entity.getItemTemplate()
        assert itemTemplate.deleted_at is None

    def test_disableItemTemplate(self):
        entity.enableItemTemplate()
        entity.disableItemTemplate()
        itemTemplate = entity.getItemTemplate()
        assert itemTemplate.deleted_at is not None

    def test_getSharelink(self):
        sharelink = entity.getSharelink()
        assert sharelink is not None
