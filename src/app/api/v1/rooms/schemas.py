from pydantic import BaseModel, ConfigDict


class RoomCreateRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    empty_timeout: int | None = None
    max_participants: int | None = None
    metadata: str | None = None


class RoomSchema(BaseModel):
    name: str
    sid: str
    creation_time: int
    num_participants: int
    metadata: str


class RoomListSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    rooms: list[RoomSchema]


class RoomAccessToken(BaseModel):
    token: str
    room_name: str
    identity: str
    livekit_url: str
