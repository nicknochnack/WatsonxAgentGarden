# from langflow.field_typing import Data
from langflow.custom.custom_component.component import Component
from langflow.io import MessageTextInput, Output, FloatInput, StrInput
from langflow.schema.data import Data
import requests


class AIAPolicyTool(Component):
    display_name = "Submit New Policy"
    description = "Submit a new insurance policy confirmation from a quote."
    documentation: str = "https://docs.langflow.org/components-custom-components"
    icon = "code"
    name = "CustomComponent"

    inputs = [
        StrInput(
            name="user_name",
            display_name="Policy users name.",
            info="This is a custom component Input",
            value=None,
            tool_mode=True,
        ),
        StrInput(
            name="dob",
            display_name="Date of birth!",
            info="This is a custom component Input",
            value=None,
            tool_mode=True,
        ),
        FloatInput(           
            name="quote_price",
            display_name="The premium for the policy of birth!",
            info="This is a custom component Input",
            value=None,
            tool_mode=True,
        )
        
    ]

    outputs = [
        Output(display_name="Output", name="output", method="submit_quote"),
    ]

    def submit_quote(self) -> Data:
        
        res = requests.post('http://localhost:8000', json={'quote_price':self.quote_price, 'name':self.user_name, 'dob':self.dob})
        
        data = Data(value=res.json())
        self.status = data
        return data
