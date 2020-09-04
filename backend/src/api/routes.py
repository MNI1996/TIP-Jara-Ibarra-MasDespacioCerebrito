from backend.src.api.questions import QuestionApi


def create_routes(api):
    api.add_resource(QuestionApi, '/questions/')
