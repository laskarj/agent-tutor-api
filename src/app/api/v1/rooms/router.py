from fastapi import APIRouter, Depends

from app.api.dependencies.stub import Stub
from app.api.v1.rooms.schemas import RoomAccessToken, RoomCreateRequest, RoomListSchema, RoomSchema
from app.shared.logger import get_logger
from app.shared.services.livekit.api_adapter import LivekitAPIAdapter

router = APIRouter(prefix="/rooms")

logger = get_logger(f"rooms:{__name__}")


@router.post("/", response_model=RoomSchema)
async def create_room(
    room_request: RoomCreateRequest, livekit_adapter: LivekitAPIAdapter = Depends(Stub(LivekitAPIAdapter))
):
    """Create a new LiveKit room"""
    room_info = await livekit_adapter.create_room(
        name=room_request.name,
        empty_timeout=room_request.empty_timeout,
        max_participants=room_request.max_participants,
        metadata=room_request.metadata,
    )

    return RoomSchema(
        name=room_info.name,
        sid=room_info.sid,
        creation_time=room_info.creation_time,
        num_participants=room_info.num_participants,
        metadata=room_info.metadata,
    )


@router.get("/")
async def list_rooms(livekit_adapter: LivekitAPIAdapter = Depends(Stub(LivekitAPIAdapter))):
    """List all active rooms"""
    response = await livekit_adapter.list_rooms()
    parsed_rooms = [
        RoomSchema(
            sid=room.sid,
            name=room.name,
            metadata=room.metadata,
            creation_time=room.creation_time,
            num_participants=room.num_participants,
        )
        for room in response.rooms
    ]
    return RoomListSchema(rooms=parsed_rooms)


@router.get("/{room_name}")
async def get_room(room_name: str, livekit_adapter: LivekitAPIAdapter = Depends(Stub(LivekitAPIAdapter))):
    room = await livekit_adapter.get_room(room_name)
    return RoomSchema(
        name=room.name,
        sid=room.sid,
        creation_time=room.creation_time,
        metadata=room.metadata,
        num_participants=room.num_participants,
    )


@router.delete("/{room_name}")
async def delete_room(room_name: str, livekit_adapter: LivekitAPIAdapter = Depends(Stub(LivekitAPIAdapter))):
    """Delete a room"""
    await livekit_adapter.delete_room(room_name)
    return {"message": f"Room {room_name} deleted successfully"}


@router.post("/{room_name}/tokens")
async def generate_access_token(
    room_name: str, identity: str, livekit_adapter: LivekitAPIAdapter = Depends(Stub(LivekitAPIAdapter))
):
    """Generate access token for a participant to join a room"""
    jwt_token = await livekit_adapter.create_token(identity=identity, room_name=room_name)
    return RoomAccessToken(token=jwt_token, room_name=room_name, identity=identity, livekit_url=livekit_adapter.ws_url)
