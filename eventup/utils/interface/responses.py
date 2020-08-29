""""Utils Response"""

# Rest Library
from rest_framework.response import Response


class CustomActions():
    def custom_response(self, status_code, status, message, data=None):
        response = {
            "status": status,
            # "data": data.data,
            "message": message
        }
        if data:
            response.update({'data': data})
        return Response(response, status=status_code)
