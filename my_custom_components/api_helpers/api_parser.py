from langflow import CustomComponent
from langflow.field_typing import Text, Dict, Data

class ApiInputParser(CustomComponent):
    display_name: str = "API Request Parser"
    description: str = "Parses a JSON payload from an API request (e.g., from AWS Lambda)."
    icon: str = "zap"

    def build_config(self):
        return {
            "api_payload": {
                "display_name": "API Payload",
                "info": "Receives the `input_value` from the flow's API call."
            }
        }

    def build(self) -> (Text, Text, Text, Text, Dict):
        payload = self.api_payload or {}
        text_output, channel_output, user_name_output, user_id_output = "", "", "", ""

        if isinstance(payload, dict):
            text_output = payload.get("text", "")
            channel_output = payload.get("channel", "")
            user_name_output = payload.get("user_name", "")
            user_id_output = payload.get("user_id", "")

        self.status = { "Parsed Text": text_output, "User": user_name_output }
        return (text_output, channel_output, user_name_output, user_id_output, payload)

    def get_output_schema(self, build_config):
        return {
            "text": Text, "channel": Text, "user_name": Text,
            "user_id": Text, "full_payload": Dict
        }