from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button = [{
            'title':'yes',
            'payload':'/affirm'
        },
        {
            'title': 'no',
            'payload': '/deny'
        }
        ]
        dispatcher.utter_message(text="Please Select Yes or no.",buttons=button)
        return []