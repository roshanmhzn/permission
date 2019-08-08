from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import redirect


class HasPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        obj = self.get_object()
        # import ipdb
        # ipdb.set_trace()
        if self.request.user.is_superuser:
            return True

        if obj.user == self.request.user:
            return True

        return super().has_permission()
