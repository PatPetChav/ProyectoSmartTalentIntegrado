from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('cards-home/',views.ConvocatoriaView.as_view()),
    # path('form-postulante',views.PostulanteView.as_view()),
    # path('form-academico',views.AcademicoView.as_view()),
    # path('form-laboral',views.LaboralView.as_view()),
    # path('form-psicologico',views.PsicologicoView.as_view()),
    # path('sign-in',views.UsuarioView.as_view()),
    # path('dashboard/<str:name>',views.DashboardView.as_view()),
    # path('tables/<str:name>',views.TablesView.as_view()),
    # path('detalle-postulante/<str:name>',views.DetalleView.as_view()),
]