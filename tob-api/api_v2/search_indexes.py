# TODO: Figure out how to configure haystack to register indices in
#       ./indices/<IndexName> instead of this default file...

from haystack import indexes
from django.utils import timezone

from api_v2.models.Topic import Topic as TopicModel


class TopicIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    autocomplete = indexes.EdgeNgramField()

    name = indexes.CharField()
    location = indexes.CharField()
    # historical = indexes.BooleanField()

    @staticmethod
    def prepare_name(obj):
        names = []
        for credential in obj.credentials.filter(end_date=None):
            for name in credential.names.all():
                names.append(name.text)

        return " ".join((names))

    @staticmethod
    def prepare_location(obj):
        locations = []
        for credential in obj.credentials.filter(end_date=None):
            for address in credential.addresses.all():
                locations.append(address.addressee)
                locations.append(address.civic_address)
                locations.append(address.city)
                locations.append(address.province)
                locations.append(address.postal_code)
                locations.append(address.country)

        return " ".join((locations))

    # @staticmethod
    # def prepare_historical(obj):
    #     return " ".join((obj.source_id))

    def get_model(self):
        return TopicModel

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            create_timestamp__lte=timezone.now()
        )