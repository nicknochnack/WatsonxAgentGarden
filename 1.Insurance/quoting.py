from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool(name='life_insurance_quote', description='This tool provides a quick life insurance quote based on high level parameters. When using this tool ensure that you know the members age, whether they smoke, drink alcohol and determine if they have heart problems now or in the past.', permission=ToolPermission.ADMIN)
def quote(age:int, smoker:bool, alcohol: bool, heart_problems:bool): 
    base_rate = 200
    age_factor = age / 30 
    smoker_factor = 1.2 if smoker else 1.0 
    alcohol_factor = 1.2 if alcohol else 1.0 
    heart_factor = 1.2 if heart_problems else 1.0 

    return base_rate * age_factor * smoker_factor * alcohol_factor * heart_factor 

if __name__ == '__main__': 
    print(quote(30, True, False, True)) 

