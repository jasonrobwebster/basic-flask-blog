import uuid
import datetime
from src.models.post import Post
from src.common.database import Database


class Blog(object):

    def __init__(self, title, description, _id=None):
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, abstract, content, created_date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id, title=title, abstract=abstract, content=content, created_date=created_date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def get_post(self, post_id):
        data = Database.find_one(collection='posts', query={"_id": post_id, "blog_id": self._id})
        return Post(**data)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description
        }

    @classmethod
    def from_mongo(cls, id):
        data = Database.find_one(collection='blogs', query={"_id": id})
        return cls(**data)

    @classmethod
    def get_blogs(cls):
        blogs = Database.find(collection='blogs', query={})
        return [cls(**blog) for blog in blogs]
