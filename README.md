# Agent Selector  

A script that returns a list of agents or agent depending upon the selection mode.  

## Question  

You are given the following data for agents 
1. agent  
2. is-available  
3. available-since (the time since the agent is available)  
4. roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.)  

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest. In random mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

Please write a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.  

### Repo details  

1. _Answers.txt_ has answers to questions asked.  
2. _data.py_ has the data of agents. More data can be added.  
3. _solver.py_ has the code to select agents.   