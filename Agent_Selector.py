import random
class agent:
    def __init__(self, name, is_available, available_since, roles):
        self.name=name
        self.is_available = is_available
        self.available_since = available_since 
        self.roles = roles
 
class isuue:
    def __init__(self,role):
        self.role=role
 
    def selector(self, obj_list, Mode):
        agent = []
        max1 = 0
        rol = []
        available_agent = [ i for i in obj_list if i.is_available == True]
        matched_agent = []
        for i in available_agent:
            flag = True
            for j in self.role:
                if j not in i.roles:
                    flag = False
            if flag:
                matched_agent.append(i)
 
        if  Mode=="All available":
            agent.extend(matched_agent)
        elif Mode=="Least Busy":
            temp = None
            for j in matched_agent:
                max1 = max(j.available_since,max1)
                temp = j
                # can check if more than 1 agent have same maximum value
            if temp:
                agent.append(temp)
        else:
            agent.append(random.choice(matched_agent))
 
        for i in agent:
            print(i.name,end = ", ")
        print("")
 
 
## Will create many objects and combile them in one list and pass it to the selector funt
 
listAgent = []
listAgent.append(agent('A1', True, 4, ['R1', 'R2', 'R3']))
listAgent.append(agent('A2', False, 0, ['R2', 'R3']))
listAgent.append(agent('A3', True, 2, ['R1', 'R3']))
listAgent.append(agent('A4', True, 4, [ 'R3']))
 
issues1 = isuue(['R1'])
issues1.selector(listAgent, "All available")
issues2 = isuue(['R3'])
issues2.selector(listAgent, "Least Busy")
issues3 = isuue(['R3'])
issues3.selector(listAgent, "Random")
