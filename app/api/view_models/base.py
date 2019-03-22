class BaseViewModel:

    def keys(self):
        return []

    def __getitem__(self, item):
        return getattr(self, item)
