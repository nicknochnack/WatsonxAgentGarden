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
            display_name="Applicant's Full Name",
            info="The full name of the applicant.",
            value=None,
            tool_mode=True,
        ),
        StrInput(
            name="dob",
            display_name="Applicant Date of Birth.",
            info="The applican't date of birth.",
            value=None,
            tool_mode=True,
        ),
        FloatInput(           
            name="quote_price",
            display_name="Quote Price",
            info="The quoted premium price for the policy!",
            value=None,
            tool_mode=True,
        ), 
        StrInput(           
            name="url",
            display_name="Api URL!",
            info="The url for the policy submission endpoint.",
            value='http://localhost:8000',
            tool_mode=False,
        )

        
    ]

    outputs = [
        Output(display_name="Output", name="output", method="submit_quote"),
    ]

    def submit_quote(self) -> Data:
        
        res = requests.post(self.url, json={'quote_price':self.quote_price, 'name':self.user_name, 'dob':self.dob})
        
        data = Data(value=res.json())
        self.status = data
        return data
