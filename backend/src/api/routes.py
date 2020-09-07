from backend.src.api.room import RoomApi
from backend.src.api.player import PlayerApi
from backend.src.api.questions import QuestionApi


def create_routes(api):
    api.add_resource(QuestionApi, '/questions/')
    api.add_resource(PlayerApi,'/players/')
    api.add_resource(RoomApi,'/rooms/')
