from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


"""
# For Way6
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='', viewset= views.ListCreateViewSet, basename='article')
router.register(prefix='', viewset=views.RetrieveUpdateDestroyViewSet, basename='article')

urlpatterns = [ 
    path('', include(router.urls))
]

# Imp points ==> 1. router automatically adds suffix_patterns
            #    2. router automatically determines whether to include 'pk' in url or not by looking into detail parameter of action decorator
            #    3. router include custom_action name in url
"""



urlpatterns = [
    
    # Way1, Way2 ==> urls patterns for function-based views as well as with apiview decorator
    # path('', views.article_list),
    # path('<int:pk>/', views.article_detail)
    

    # Way3 ==> urls patterns for class-based APIViews
    # path('', views.ArticleAPIView.as_view()),
    # path('<int:id>/', views.ArticleDetails.as_view())


    # Way4 ==> urls patterns for generic class-based APIViews
    # path('', views.ListCreateRetrieveUpdateDestroyGenericAPIView.as_view()),
    # path('<int:id>/', views.ListCreateRetrieveUpdateDestroyGenericAPIView.as_view())


    # Way5 ==> urls patterns for class-based Concrete Generic Views
    # path('', views.ListCreateGenericConcreteView.as_view()),
    # path('<int:id>/', views.RetrieveUpdateDestroyGenericConcreteView.as_view())


    # Way6 ==> urls patterns using ViewSet, which is inheriting APIView classes
    # path('', views.ListCreateViewSet.as_view({
    #     'get': 'list',
    #     'post':'create'
    #     })),
    # path('<int:id>/', views.RetrieveUpdateDestroyViewSet.as_view({
    #     'get': 'retrieve', 
    #     'put': 'update', 
    #     'delete': 'destroy'
    #     }))
    # path('', include(router.urls))

    
    # Way7 ==> urls patterns using GenericViewSet, which is inheriting GenericAPIView class
    # path('', views.ListCreateRetrieveUpdateDestroyGenericViewSet.as_view({
    #     'get': 'list',
    #     'post':'create'
    #     })),
    # path('<int:id>/', views.ListCreateRetrieveUpdateDestroyGenericViewSet.as_view({
    #     'get': 'retrieve', 
    #     'put': 'update', 
    #     'delete': 'destroy'
    #     }))



    # Way8 ==> urls patterns using GenericViewSet, which is inheriting GenericAPIView class
    # path('', views.ListRetrieveGenericViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', views.ListRetrieveGenericViewSet.as_view({'get': 'retrieve'})),

    path('', views.GenericModelViewSet.as_view({
        'get': 'list',
        'post':'create'
        })),
    path('<int:pk>/', views.GenericModelViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        # 'patch': 'partial_update',
        'delete': 'destroy'
        }))

    # for custom-actions
    # path('<int:pk>/changepassword/', views.views.GenericModelViewSet.as_view({'put': 'change_password'}))
]

urlpatterns = format_suffix_patterns(urlpatterns)