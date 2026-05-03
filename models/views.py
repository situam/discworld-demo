from dataclasses import dataclass
from models.discworld import PersondetailModel, ProfessionlistModel

@dataclass
class ExpandedPersonView:
    person: PersondetailModel
    professions: dict[str, ProfessionlistModel | None]

    @property
    def fullname(self):
        return f"{self.person.forename} {self.person.surname}"
    
    def to_dict(self):
        return {
        **self.person.model_dump(),
        "profession": [
            self.professions[str(url)].name
            for url in (self.person.profession or [])
            if str(url) in self.professions
        ],
    }