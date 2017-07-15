from cornice.resource import resource, view

from ode.models import Source
from ode.resources.base import ResourceMixin, set_content_type
from ode.resources.base import COLLECTION_JSON_MIMETYPE
from ode.validation.schema import SourceCollectionSchema
from ode.validation.validators import has_provider_id
from ode.validation.validators import validate_querystring


@resource(collection_path='/v1/sources', path='/v1/sources/{id}',
          filters=set_content_type)
class SourceResource(ResourceMixin):

    model = Source

    @view(validators=[has_provider_id], schema=SourceCollectionSchema,
          content_type=COLLECTION_JSON_MIMETYPE)
    def collection_post(self):
        return ResourceMixin.collection_post(self)

    @view(validators=[has_provider_id], schema=SourceCollectionSchema,
          content_type=COLLECTION_JSON_MIMETYPE)
    def put(self):
        return ResourceMixin.put(self)

    @view(validators=[validate_querystring])
    def collection_get(self):
        return ResourceMixin.collection_get(self)
