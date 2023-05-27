import re
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_form"
    
    def validate_name(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker, domain: DomainDict,) -> Dict[Text, Any]:
        if slot_value.replace(" ", "").isalpha():
            return {'name':slot_value}
        else:
            dispatcher.utter_message("Invalid Input.")
            return {'name': None}