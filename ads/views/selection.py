from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsSelectionOwner
from ads.serializers import SelectionSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer

    default_permission = [AllowAny(), ]
    permission_list = {
        "create": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsSelectionOwner()],
        "partial_update": [IsAuthenticated(), IsSelectionOwner()],
        "destroy": [IsAuthenticated(), IsSelectionOwner()]
    }

    def get_permissions(self):
        return self.permission_list.get(self.action, self.default_permission)
