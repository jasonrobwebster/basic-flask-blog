import uuid
import datetime
from src.common.database import Database


class Post(object):

    def __init__(self, blog_id, title, content, abstract, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.abstract = abstract
        self.content = content
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'abstract': self.abstract,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]