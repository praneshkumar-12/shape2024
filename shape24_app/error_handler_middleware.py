import logging
from django.shortcuts import render
import traceback

logger = logging.getLogger(__name__)


class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.exception(exception)
        logging.basicConfig(filename="error.log", level=logging.ERROR)
        logging.error("=================================")
        logging.error(str(exception), exc_info=True)
        logging.error("=================================")

        return render(
            request,
            "error.html",
            {
                "error_title": "Well... Sorry, Something unexpected happened! :(",
                "error_message": "Don't worry, we'll take care of this!",
                "exception": str(exception)
                + " || "
                + "".join(traceback.format_tb(exception.__traceback__)),
            },
        )
