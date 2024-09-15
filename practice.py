from enum import Enum
from topic import Topic
from problem import Problem


class PracticeState(Enum):
    NEW = 0
    LEARNING = 1
    MATURE = 2


class TopicPractice:
    def __init__(self, topic: Topic):
        self._topic = topic
        self.state = PracticeState.NEW
        self.last_time = 0
        self.wait_time = 1


class ProblemPractice:
    def __init__(self, problem: Problem):
        self._problem = problem
        self.state = PracticeState.NEW
        self.last_time = 0
        self.wait_time = 1
