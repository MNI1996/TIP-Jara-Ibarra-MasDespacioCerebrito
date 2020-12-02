from backend.src.api.authentication import LoginApi, RegisterApi
from backend.src.api.ranking import RankingApi
from backend.src.api.room import RoomsApi, RoomApi, RoomsUpdateApi
from backend.src.api.player import PlayerApi
from backend.src.api.questions import QuestionApi, AnswerQuestionApi


def create_routes(api):
    api.add_resource(QuestionApi, '/questions/')
    api.add_resource(AnswerQuestionApi, '/question/<id>/')
    api.add_resource(PlayerApi, '/players/')
    api.add_resource(RoomsApi, '/rooms/')
    api.add_resource(RoomApi, '/rooms/<room_id>/')
    api.add_resource(RankingApi, '/ranking/players/')
    api.add_resource(LoginApi, '/login/')
    api.add_resource(RegisterApi, '/register/')
    api.add_resource(RoomsUpdateApi, '/rooms/<room_id>/update/')
