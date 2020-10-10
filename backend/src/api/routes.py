from backend.src.api.room import RoomsApi, RoomApi
from backend.src.api.player import PlayerApi
from backend.src.api.questions import QuestionApi, AnswerQuestionApi


def create_routes(api):
    api.add_resource(QuestionApi, '/questions/')
    api.add_resource(AnswerQuestionApi, '/question/<id>/')
    api.add_resource(PlayerApi, '/players/')
    api.add_resource(RoomsApi, '/rooms/')
    api.add_resource(RoomApi, '/rooms/<room_id>/')
