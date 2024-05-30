from pydantic import BaseModel, constr


class PressRelease(BaseModel):
    text: str = constr(min_length=100)


class ModifiedPressRelease(BaseModel):
    text: str


class ModifiedPressReleaseGet(ModifiedPressRelease):
    id: int

    class Config:
        from_attributes = True


class CreditAgencySummaries(BaseModel):
    rating: str
    summary: str


class CreditAgencySummariesGet(CreditAgencySummaries):
    id: int

    class Config:
        from_attributes = True
