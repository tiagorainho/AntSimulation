class State:
    def __init__(self, name) -> None:
        self.name = name

    def enter(self):
        # print(f"Entering {self.name}")
        pass

    def update(self, object: any):
        pass

    def exit(self):
        pass

class Transition:
    def __init__(self, _from, _to) -> None:
        self._from = _from
        self._to = _to

class FSM:
    def __init__(self, states: list[State], transitions: dict[Transition]) -> None:
        self._states = states
        self._transitions = transitions

        self.current: State = self._states[0]
        self.end: State = self._states[-1]

    def event(self, event, object):
        if event:
            trans = self._transitions.get(event)
            if trans and trans._from == self.current:
                self.current.exit()
                self.current = trans._to
                self.current.enter()
        self.current.update(object)

        if self.current == self.end:
            self.current.exit()
            return False
        return True