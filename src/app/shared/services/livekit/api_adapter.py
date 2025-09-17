from livekit.api import AccessToken, LiveKitAPI, VideoGrants
from livekit.protocol.models import Room
from livekit.protocol.room import (
    CreateRoomRequest,
    DeleteRoomRequest,
    ListRoomsRequest,
    ListRoomsResponse,
)

from app.shared.config.providers import LivekitConfig
from app.shared.logger import get_logger
from app.shared.services.livekit.exceptions import RoomNotFoundError

logger = get_logger("livekit.api:adapter")


class LivekitAPIAdapter:
    def __init__(self, config: LivekitConfig) -> None:
        self._config = config
        self._api_client = LiveKitAPI(url=config.ws_url, api_key=config.api_key, api_secret=config.secret_key)

    async def close(self) -> None:
        """Close the API client session."""
        await self._api_client._session.close()

    async def create_room(
        self,
        name: str,
        empty_timeout: int | None = None,
        max_participants: int | None = None,
        metadata: str | None = None,
    ) -> Room:
        request = CreateRoomRequest(
            name=name,
            empty_timeout=empty_timeout,
            max_participants=max_participants,
            metadata=metadata,
        )
        room: Room = await self._api_client.room.create_room(request)
        return room

    async def list_rooms(self) -> ListRoomsResponse:
        request = ListRoomsRequest()
        response = await self._api_client.room.list_rooms(request)
        logger.info(response)
        return response

    async def get_room(self, name: str) -> Room:
        request = ListRoomsRequest(names=[name])
        response = await self._api_client.room.list_rooms(request)
        if not response.rooms:
            raise RoomNotFoundError("Room not found")
        return response.rooms[0]

    async def delete_room(self, room_name: str):
        request = DeleteRoomRequest(room=room_name)
        await self._api_client.room.delete_room(request)

    async def create_token(self, room_name: str, identity: str) -> str:
        token = AccessToken(self._config.api_key, self._config.secret_key)
        grant = VideoGrants(
            room_join=True,
            room=room_name,
            can_publish=True,
            can_subscribe=True,
        )

        token = token.with_identity(identity).with_name(identity).with_grants(grant)
        jwt_token = token.to_jwt()
        return jwt_token

    @property
    def ws_url(self) -> str:
        return self._config.ws_url
