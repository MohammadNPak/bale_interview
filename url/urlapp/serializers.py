from rest_framework import serializers
from .models import UrlModel
from django.utils.http import urlsafe_base64_encode


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = ["url","short_url"]
        extra_kwargs = {'short_url': {'required':False}}

    # def validate(self, data):
    #     # context = getattr(self, "context", None)

    #     # if context is None:
    #     #     return data

    #     # url = context.get("short_url")
    #     data["short_url"] = urlsafe_base64_encode(str(data["url"]).encode("utf-8"))
    #     # super.validate()
    #     return data
    