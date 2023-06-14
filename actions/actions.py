from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSaludaryAyuda(Action):

     def name(self) -> Text:
         return "action_saludar_y_ayuda"

     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         print(format(tracker.get_slot('nombre')))   
         dispatcher.utter_message(text="Gracias "+format(tracker.get_slot('nombre'))+". ¿En qué te puedo ayudar?")

         return []

class ActionProporcionarDocumento(Action):

     def name(self) -> Text:
         return "action_proporcionar_documento"

     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         # url = tracker.get_slot('documento') para consulta a BBDD
         
         url = "https://cualquierservidor/certificado_empadronamiento.pdf"  
         dispatcher.utter_message(text="Puedes descargar el documento en "+url)

         return []
