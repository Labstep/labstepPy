class EntityList(list):
    def __init__(self, items, entityClass, user):
        super().__init__(map(lambda x: entityClass(x, user), items))
        self.__searchKey__ = getattr(entityClass, '__searchKey__', 'name')

    def get(self, key):
        hits = [entity for entity in self if getattr(
            entity, self.__searchKey__) == key]

        if len(hits) == 0:
            return None

        if len(hits) == 1:
            return hits[0]

        if len(hits) > 1:
            print(f'Warning: multiple matches found for "{key}"')

            return hits[0]
