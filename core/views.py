from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee


class UserInformation(APIView):

    def get(self, request, format=None, **kwargs):
        name = kwargs.get('name')
        try:
            employee = Employee.objects.get(name=name)
            data = {'information': employee.information}
        except:
            data = {'information': "User Does not exists"}

        return Response(data)
