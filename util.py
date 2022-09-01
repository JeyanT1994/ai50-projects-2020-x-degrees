class Actor():
    def __init__(self, person_id, parent_id, movie):
        self.person_id = person_id  # state
        self.parent_id = parent_id
        self.movie = movie  # action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, actor):
        self.frontier.append(actor)

    def contains_state(self, person_id):
        return any(actor.person_id == person_id for actor in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            actor = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return actor


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            actor = self.frontier[0]
            self.frontier = self.frontier[1:]
            return actor
