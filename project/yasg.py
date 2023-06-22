from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="LMS for ASTANA HUB",
      default_version='v1.4.2',
      description="""
         This is an LMS for Astana HUB. Developed on the basis of the LMS Case Cup competition.

         Team: Astronauts
         ---Yerlan Ayapov | Backend developer
         ---Erzat Pazylkhanov | Frontend developer
         ---Zhansaya Nurlybekova | UI/UX designer (she left at 4 weeks)
      """,
      license=openapi.License(name="No license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swaggers-yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]