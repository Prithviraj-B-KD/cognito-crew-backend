from langflow.custom import Component
from langflow.io import DataInput, Output
from langflow.schema import Data
from typing import Dict, Text

class ApiInputParser(Component):
    display_name: str = "API Request Parser"
    description: str = "Parses a JSON payload from an API request (e.g., from AWS Lambda)."
    icon: str = "zap"

    # Define all inputs as a class-level list
    inputs = [
        DataInput(
            name="api_payload",
            display_name="API Payload",
            info="This field receives the `input_value` from the flow's API call.",
            required=True
        )
    ]

    # Define all outputs as a class-level list, each with a corresponding method
    outputs = [
        Output(display_name="Text", name="text", method="get_text"),
        Output(display_name="Channel", name="channel", method="get_channel"),
        Output(display_name="User Name", name="user_name", method="get_user_name"),
        Output(display_name="User ID", name="user_id", method="get_user_id"),
        Output(display_name="Full Payload", name="full_payload", method="get_full_payload"),
    ]

    def _pre_run_setup(self):
        """
        A lifecycle hook to process the data once before any output method is called.
        """
        # Get the input payload. It's available as `self.<input_name>`
        payload = self.api_payload.data if self.api_payload else {}

        # Safely parse the payload and store the results as instance variables
        if isinstance(payload, dict):
            self.parsed_text = payload.get("text", "")
            self.parsed_channel = payload.get("channel", "")
            self.parsed_user_name = payload.get("user_name", "")
            self.parsed_user_id = payload.get("user_id", "")
            self.parsed_payload = payload
        else:
            # Handle cases where the input is not a dictionary
            self.parsed_text = ""
            self.parsed_channel = ""
            self.parsed_user_name = ""
            self.parsed_user_id = ""
            self.parsed_payload = {}
        
        # Set a status message for the UI
        self.status = {
            "Parsed Text": self.parsed_text,
            "User": self.parsed_user_name
        }

    # Create a separate method for each output defined above
    def get_text(self) -> Text:
        """Returns the parsed text from the payload."""
        return self.parsed_text

    def get_channel(self) -> Text:
        """Returns the parsed channel name."""
        return self.parsed_channel

    def get_user_name(self) -> Text:
        """Returns the parsed user name."""
        return self.parsed_user_name

    def get_user_id(self) -> Text:
        """Returns the parsed user ID."""
        return self.parsed_user_id

    def get_full_payload(self) -> Dict:
        """Returns the entire original payload as a dictionary."""
        return self.parsed_payload