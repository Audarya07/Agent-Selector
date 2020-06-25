from data import *
import random

class SelectAgent:

    def all_available(self, agent_list, issue):
        selected_agents = []
        for agent in agent_list:
            if agent.is_available:
                if all(role in agent.roles for role in issue):
                    selected_agents.append(agent.agent_name)
        
        if selected_agents:
            return selected_agents
        else:
            return "Agents not available !!"

    def select_random(self, agent_list, issue):
        selected_agents = []
        for agent in agent_list:
            if agent.is_available:
                if all(role in agent.roles for role in issue):
                    selected_agents.append(agent.agent_name)
        
        if selected_agents:
            assigned_agent = random.choice(selected_agents)
            return assigned_agent
        else:
            return "Agents not available !!"

    def least_busy(self, agent_list, issue):
        selected_agents = []
        for agent in agent_list:
            if agent.is_available:
                if all(role in agent.roles for role in issue):
                    selected_agents.append((agent.agent_name, agent.available_since))
        
        if selected_agents:
            selected_agents.sort(key=lambda x: -x[1])
            assigned_agent = selected_agents[0]
            return assigned_agent
        else:
            return "Agents not available !!"

if __name__ == "__main__":
    print("Please write issues from the following list:\n1.sales\n2.support\n3.speaker")
    issue = input("Enter issues separated by spaces : ").split()

    for val in issue:
        if val not in ["sales", "support", "speaker"]:
            print("invalid issue '{}'".format(val))
            exit()

    print("-------SELECT MODE NUMBER--------\n1.All available\n2.Least Busy\n3.Random Select")
    mode = int(input("Enter mode = "))

    select_agent = SelectAgent()

    if mode == 1:
        print(select_agent.all_available(agents, issue))
    elif mode == 2:
        print(select_agent.least_busy(agents, issue))
    elif mode == 3:
        print(select_agent.select_random(agents, issue))
    else:
        print("Invalid Input !!")