from sqlalchemy import Column, Integer, Text, SmallInteger, ForeignKey, String
from sqlalchemy.orm import reconstructor, relationship

from app.models.base import Base


class Classic(Base):
    """


    """
    id = Column(Integer, primary_key=True,
                comment='期刊在数据中序号，供点赞使用')
    content = Column(Text, default='', comment='期刊内容')
    # image = relationship(Image)
    img_id = Column(Integer, ForeignKey('image.id'))
    index = Column(SmallInteger, comment='期号')
    title = Column(String(100), default='', comment='期刊题目')
    author = Column(String(100), default='', comment='作者')
    type = Column(
        SmallInteger, default=100,
        comment='期刊类型,这里的类型分为:100 电影 200 音乐 300 句子')
    url = Column(String(100), default='', nullable=True,
                 comment='当type为300时，此字段为音乐url')

    @reconstructor
    def __init__(self):
        self.fields = [
            'content', 'id', 'image_url',
            'fav_nums', 'like_status',
            'index', 'create_datetime',
            'title', 'author',
            'type', 'url']

    def keys(self):
        return self.fields


    @property
    def latest(self):
        res = Classic.query.filter_by().order_by(
            Classic.id.desc()
        ).first_or_404()
        return res

    @property
    def image_url(self):
        return self.image.image

    # @property
    # def fav_nums(self):
    #     count = Like.query.filter_by(cid=self.id).count()
    #     return count

    def next(self, index):
        res = self.query.filter_by().filter(
            Classic.id < index
        ).order_by(
            Classic.id.desc()
        ).limit(1).first_or_404()
        return res

    def previous(self, index):
        return self.query.filter_by().filter(
            Classic.id < index
        ).order_by(
            Classic.id.desc()
        ).limit(1).first_or_404()

    def detail(self, type, id):
        return self.query.filter_by(
            type=type, id=id
        ).first_or_404()
