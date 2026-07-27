from labstep.generic.entity.model import Entity


class ActivityLog(Entity):
    """
    Represents an Activity Log on Labstep.
    """

    __entityName__ = "log"
    __unSearchable__ = True


    @property
    def printMessage(self):
        parents = self.loggable_parents or []
        breadcrumb = " - ".join((p["display_name"] or f"{p['entity_class']} {p['id']}" for p in parents))
        message = self.message
        author = self.author or {}
        return f"{breadcrumb} - {author['username']} - {message}" if breadcrumb else message