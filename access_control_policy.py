access_control_matrix = {
    "client": {
        "client info": ["view", "modify"],
        "balance": ["view"],
        "investment portfolio": ["view"],
        "financial advisor info": ["view"],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
    },
    "premium_client": {
        "client info": ["view", "modify"],
        "balance": ["view"],
        "investment portfolio": ["view", "modify"],
        "financial advisor info": ["view"],
        "financial planner info": ["view"],
        "investment analyst info": ["view"],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
    },
    "financial_planner": {
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view", "modify"],
        "financial advisor info": [],
        "financial planner info": ["view", "modify"],
        "investment analyst info": [],
        "money market instruments": ["view"],
        "private consumer instruments": ["view"],
        "derivatives trading": [],
        "interest instruments": []
    },
    "financial_advisor": {
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view", "modify"],
        "financial advisor info": ["view", "modify"],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": ["view"],
        "derivatives trading": [],
        "interest instruments": []
    },
    "investment_analyst": {
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view", "modify"],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": ["view", "modify"],
        "money market instruments": ["view"],
        "private consumer instruments": ["view"],
        "derivatives trading": ["view"],
        "interest instruments": ["view"]
    },
     "tech_support": {
        "client info": ["view"],
        "balance": [],
        "investment portfolio": [],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
    },
     "teller": {
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view"],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
    },
     "compliance_officer": {
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view", "validate"],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
    }
}