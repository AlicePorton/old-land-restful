from app.api.view_models.base import BaseViewModel


class ClassicViewModel(BaseViewModel):
    """
    TODO: 这里是对Model做一个筛选，但是这种筛选是不是有些过于复杂，能不能用更加简便的方法：
        `反射`
    """
    def __init__(self, classic):
        self.content = classic['content']
        self.fav_nums = classic['fav_nums']
        self.id = classic['id']
        self.image = classic['image_url']
        self.index = classic['index']
        self.like_status = classic['like_status']
        self.pubdate = classic['create_datetime']
        self.title = self.mark_title(classic['title'], classic['author']) or '未名'
        self.type = classic['type']
        self.url = classic.url or ''

    def keys(self):
        keys = ['content', 'fav_nums', 'id', 'image', 'index',
                'like_status', 'pubdate', 'title', 'type']

        if self.url:
            keys.append('url')
        return keys

    @staticmethod
    def mark_title(title, author):
        return '' if title is None or author is None else author + '<{}>' . format(title)


class ClassicCollection:
    def __init__(self):
        self.classic = []

    def fill_single(self, data):
        self.classic = ClassicViewModel(data)
        return self.classic

    def fill(self, data):
        self.classic = [ClassicViewModel(single) for single in data]
        return self.classic
