from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee


class EmployeeView(APIView):

    def get(self, request):
        employee = Employee.objects.all()
        data = []
        for i in range(len(employee)):
            if employee[i].manager != None:
                e = {"emp_id": employee[i].id,
                     "emp_name": employee[i].name,
                     "manager": employee[i].manager.name
                     }
            else:
                e = {"emp_id": employee[i].id,
                     "emp_name": employee[i].name,
                     "manager": None
                     }
            data.append(e)

        return Response(data)
