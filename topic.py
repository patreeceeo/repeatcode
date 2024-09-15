from problem import Problem


class Topic:
    def __init__(self, name: str):
        self.name = name
        self._problems = set()

    def add_problem(self, problem: Problem):
        self._problems.add(problem)
