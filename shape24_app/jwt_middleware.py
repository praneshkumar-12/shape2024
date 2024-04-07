from jwt import decode, InvalidTokenError
from django.conf import settings
from django.shortcuts import redirect
from shape24_app.models import Users
import hashlib


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.path in settings.JWT_MIDDLEWARE_EXCLUDED_PATHS
            or "/checkavail" in request.path
        ):
            return self.get_response(request)

        jwt_token = request.session.get("jwt-token", None)
        _id = request.session.get("_id")

        if jwt_token and _id:
            try:
                decoded_jwt = decode(
                    jwt_token, settings.SECRET_KEY, algorithms=["HS256"]
                )

                if not check_jwt(decoded_jwt, _id):
                    del request.session["jwt-token"]
                    return redirect("/login/")

                request.jwt_token = decoded_jwt

                response = self.get_response(request)
                return response

            except InvalidTokenError:
                del request.session["jwt-token"]
                return redirect("/login/")

        if request.session.get("jwt-token", None):
            del request.session["jwt-token"]

        return redirect("/login/")


def check_jwt(decoded_jwt, _id):
    email = decoded_jwt.get("email")

    user_object = Users.objects.filter(user_id=_id)

    if not user_object:
        return False

    user_object = user_object[0]

    user_email = user_object.email

    if not user_email:
        return False

    hashed_email = str(hashlib.sha256(user_email.encode("utf-8")).hexdigest())

    if hashed_email == email:
        return True

    return False
