from dataclasses import dataclass, field
from typing import List
from dataclass_wizard import JSONWizard



@dataclass()
class User(JSONWizard): 
    name: str
    email: str
    password: str
    followers: List[str] = field(default_factory=list) 

