from typing import Type, Generic, TypeVar, List, Iterator
from modules.epiUtils.epiObject import EpiObject
import pandas as pd

EpiObjectTypeVar = TypeVar('EpiObjectTypeVar', bound=EpiObject)

class EpiList(Generic[EpiObjectTypeVar], list):
    def __init__(self, items: List[EpiObjectTypeVar] = None):
        if items is not None:
            super().__init__(items)
        else:
            super().__init__()

    def __iter__(self) -> Iterator[EpiObjectTypeVar]:
        return super().__iter__()

    @classmethod
    def fromDataframe(cls, dataframe: pd.DataFrame, epiObjectType: Type[EpiObjectTypeVar]) -> 'EpiList[EpiObjectTypeVar]':
        epiObjectList = []

        for row in dataframe.to_dict('records'):
            # try to parse object as epi object
            instance = epiObjectType.parse_obj(row)
            epiObjectList.append(instance)

        return cls(epiObjectList)

    def toDataframe(self) -> pd.DataFrame:
        epiObjDictionaries = [obj.dict() for obj in self]
        return pd.DataFrame(epiObjDictionaries)

    def toListOfDicts(self) -> List[dict]:
        return [obj.dict() for obj in self]
