

class AbstractDAO(object):

    def create(self, entity) -> bool:
        raise NotImplementedError("Class %s doesn't implement create()"
                                  % (self.__class__.__name__))

    def read(self, entityID) -> list:
        raise NotImplementedError("Class %s doesn't implement read()"
                                  % (self.__class__.__name__))

    def update(self, entity, entityID) -> bool:
        raise NotImplementedError("Class %s doesn't implement update()"
                                  % (self.__class__.__name__))

    def delete(self, entityID) -> bool:
        raise NotImplementedError("Class %s doesn't implement delete()"
                                  % (self.__class__.__name__))