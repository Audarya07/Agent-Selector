class CreateAgent:

    def __init__(self, agent_name, is_available, available_since, roles):
        self.agent_name = agent_name
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles

#Creating Data

agents = [
    CreateAgent('Richard', True, 2, ["sales", "support"]),
    CreateAgent('John', False, 1, ["sales", "support"]),
    CreateAgent('Smith', False, 3, ["speaker", "support"]),
    CreateAgent('Buck', True, 3, ["support", "sales"]),
    CreateAgent('Larry', True, 4, ["speaker", "support", "sales"]),
    CreateAgent('Andrew', True, 9, ["speaker", "sales", "support"]),
    CreateAgent('Paige', False, 7, ["speaker", "support"]),
    CreateAgent('Hudson', True, 8, ["sales", "support"]),
    CreateAgent('Bill', True, 8, ["sales", "support"])
]