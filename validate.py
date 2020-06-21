from pydantic import BaseModel, ValidationError, PositiveFloat, PositiveInt, Field, constr, StrictInt

class Marke(BaseModel):
    MichNr : PositiveInt
    Satz : str
    Jahrgang : PositiveInt
    Gebiet : str = Field(min_length=1)
    Entwertung : str = Field(..., regex='^postfrisch|falz$')
    Anzahl : StrictInt
    Preis : PositiveFloat 

checks = list(Marke.__fields__.keys())
check_result = []

def CheckMarke(d1):
    try:
        print('Checked Marke : ', Marke(**d1))
        check_result.append("Entry valid")
    except ValidationError as e:
        errorlist = [x['loc'][0] + ": " + x['msg'] for x in e.errors()]
        check_result.append("; ".join(errorlist))
    finally:
        return check_result

def validate_df(dta):
    dta.fillna("", inplace=True)
    
    for i in dta.index:
        zeile = dict(zip(checks, dta.iloc[i]))
        CheckMarke(d1=zeile)
    

    dta['Fehler'] = check_result
    return dta


