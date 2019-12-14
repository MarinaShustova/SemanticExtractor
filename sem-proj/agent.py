import pickle


class Model:
    def __init__(self, name, descr):
        self.arguments = []
        self.conflict = descr.get('conflict')
        self.decisions = descr.get('previous decisions')
        self.agents = descr.get('agents')
        self.name = name

    def create(self, descr):
        pass

    def createfromcase(self, case):
        descr = {case.get('Model'): {'agents': [case.get('agent'), case.get('opponent')], 'conflict': '', 'previous decisions': [],
                 'possible agent1 arguments': [], 'possible agent2 arguments': []}}
        return descr


class Agent:
    intentions = []
    missingresources = []
    current_case = {}
    database = {}

    def __init__(self):
        with open('case.pkl', 'rb') as f1:
            self.current_case = pickle.load(f1)
        f1.close()
        with open('Models.pkl', 'rb') as f2:
            self.database = pickle.load(f2)
        f2.close()

        if self.current_case.get('Model') not in self.database:
            self.database.update(self.model.createfromcase(self.current_case))

        self.model = Model(self.current_case.get('Model'), self.database.get(self.current_case.get('Model')))

        self.intentions.append(self.current_case.get('goal'))

        for i in self.current_case.get('missing'):
            self.missingresources.append(i)

        if self.model.agents[0] == self.current_case.get('agent'):
            self.model.arguments = (self.database.get(self.model.name)).get('possible agent1 arguments')
        else:
            self.model.arguments = (self.database.get(self.model.name)).get('possible agent2 arguments')

    def convince(self):
        while self.intentions:
            self.makesuggestion()

    def makesuggestion(self):
        for i in self.missingresources:
            print("What I need is", i)
        self.waitfordecision()

    def waitfordecision(self):
        for i in self.missingresources:
            answer = input(i + " : ")
            if answer is 'Yes':
                self.satisfy(i)
            else:
                self.reject()


    def satisfy(self, resource):
        self.missingresources.remove(resource)
        if not self.missingresources:
            self.intentions.clear()

    def reject(self):
        print("No, it is not satisfying")
        if self.model.arguments:
            print(self.model.arguments.pop())
        else:
            print("I ran out of arguments")


def main():
    agent = Agent()
    agent.convince()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
