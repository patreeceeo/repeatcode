from topic import Topic
from difficulty import Difficulty


class Problem:
    def __init__(self, id: int, slug: str, difficulty: Difficulty):
        self.id = id
        self.slug = slug
        self.difficulty = difficulty
        self._topics = set()

    def add_topics(self, topics: set[Topic]):
        for topic in topics:
            self._topics.add(topic)
            topic.add_problem(self)
