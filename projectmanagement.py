from datetime import date


class Project:
    def __init__(self,name,startDate,endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []

    def addTask(self,task):
        self.tasks.append(task)

class Task:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def addResource(self,resource):
        self.resources.append(resource)


class Resource:
    def __init__(self,name,skill):
        self.name = name
        self.skill = skill

Project = Project("AI",date(2021,2,3),date(2021,9,30))
task = Task('Create Bot',90)
resource = Resource("John","Python")
task.addResource(resource)
Project.addTask(task)

for eachTask in Project.tasks:
    print(eachTask.name)
    for eachResource in eachTask.resources:
        print(eachResource.name)
        print(eachResource.skill)
