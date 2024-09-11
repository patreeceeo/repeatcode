# Required in Python < 3.11 for automatic forward references
from __future__ import annotations


class Problem:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    _tags = set()

    def add_tags(self, tags: set[Tag]):
        for tag in tags:
            self._tags.add(tag)
            tag.add_problem(self)


class Tag:
    def __init__(self, name: str):
        self.name = name

    _problems = set()

    def add_problem(self, problem: Problem):
        self._problems.add(problem)
