from django.conf.urls import url, include
from django.conf import settings

urlpatterns = [
    url(r'^api/v1/todo/', include('app.todo.urls')),
]

# ENABLE SWAGGER
if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="To-do API",
            default_version='v1',
            description="",
        ),
        validators=['flex', 'ssv'],
        public=True,
    )
    urlpatterns.extend(
        [
            url(r'^docs(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
            url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
        ]
    )
