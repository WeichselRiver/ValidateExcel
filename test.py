import pandas as pd
from pydantic import BaseModel, ValidationError


class Marke(BaseModel):
    MichNr : int
    name : str

dta = pd.read_excel(r'D:\Programming\html\Bilder\test.xlsx')

for i in list(range(dta.shape[0])):
    try:
        Marke(MichNr=dta[MichNr][i], name = "Hallo")
    except ValidationError as e:
        print(e)

