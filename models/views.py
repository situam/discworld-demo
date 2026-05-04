from dataclasses import dataclass
from models.discworld import (
    PaginatedPersonlistModelList,
    PersondetailModel,
    ProfessionlistModel,
)
from utils.url_to_query_string import url_to_query_string


@dataclass
class ExpandedPersonListView:
    person_list: PaginatedPersonlistModelList
    professions: dict[str, ProfessionlistModel | None]

    # pagination links: extract just the query string from the prev/next urls
    @property
    def link_to_prev_page(self):
        return (
            None
            if self.person_list.previous is None
            else url_to_query_string(self.person_list.previous)
        )

    @property
    def link_to_next_page(self):
        return (
            None
            if self.person_list.next is None
            else url_to_query_string(self.person_list.next)
        )


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
