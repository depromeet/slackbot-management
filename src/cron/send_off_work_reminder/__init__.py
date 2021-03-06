from src.utils.http import LambdaResponse, ExceptionHandler
from src.utils.logging import Logger
from src.utils.slack import SlackMessageWriter


@LambdaResponse
@ExceptionHandler
@Logger
@SlackMessageWriter
def handler(event, context):
    return {
        'channel': 'general',
        'text': '삐빅. 퇴근시간입니다.'
    }
