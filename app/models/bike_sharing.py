from pydantic import BaseModel, Field, field_validator

class BikeSharingRequest(BaseModel):
    season: str = Field(..., description="Season (Winter/Spring/Summer/Fall)")
    mnth: str = Field(..., description="Month name (January, etc.)")
    hr: int = Field(..., ge=0, le=23, description="Hour of the day")
    holiday: str = Field(..., description="Yes/No if holiday")
    weekday: str = Field(..., description="Name of the weekday (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday)")
    workingday: str = Field(..., description="Yes/No if working day")
    weathersit: int = Field(..., description="Weather code")
    temp: float = Field(..., ge=0, le=1, description="Normalized temperature")
    atemp: float = Field(..., ge=0, le=1, description="Normalized feeling temperature")
    hum: float = Field(..., ge=0, le=1, description="Normalized humidity")
    windspeed: float = Field(..., ge=0, le=1, description="Normalized wind speed")

    @field_validator("season")
    def validate_season(cls, v):
        allowed = {"Winter", "Spring", "Summer", "Fall"}
        if v not in allowed:
            raise ValueError(f"season must be one of {allowed}")
        return v

    @field_validator("mnth")
    def validate_mnth(cls, v):
        allowed = {
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        }
        if v not in allowed:
            raise ValueError(f"mnth must be one of {allowed}")
        return v

    @field_validator("holiday", "workingday")
    def validate_binary_strings(cls, v):
        allowed = {"Yes", "No"}
        if v not in allowed:
            raise ValueError(f"Must be one of {allowed}")
        return v

    @field_validator("weekday")
    def validate_weekday(cls, v):
        allowed = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
        if v not in allowed:
            raise ValueError(f"weekday must be one of {allowed}")
        return v

    @field_validator("weathersit")
    def validate_weathersit(cls, v):
        allowed = {1, 2, 3, 4}
        if v not in allowed:
            raise ValueError(f"weathersit must be one of {allowed}")
        return v

