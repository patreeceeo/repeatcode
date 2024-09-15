from tag import Tag
from difficulty import Difficulty


class Problem:
    def __init__(self, id: int, slug: str, difficulty: Difficulty):
        self.id = id
        self.slug = slug
        self.difficulty = difficulty
        self._tags = set()

    def add_tags(self, tags: set[Tag]):
        for tag in tags:
            self._tags.add(tag)
            tag.add_problem(self)
