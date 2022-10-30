from .models import Article
from . serializers import ArticleSerializer


"""
# Way1 ==> function based views without api_view() decorator

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def article_list(request, format=None):
    '''
    fetch all objects & create object
    '''

    # GET all objects
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    # POST/ create object
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data) 

        if serializer.is_valid():
            serializer.save()               # serializer.save() calls serializer.create() or serializer.update() depending on number of parameters passes to Serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)  


@csrf_exempt
def article_detail(request, pk, format=None):
    '''
    fetch detail, update and delete single object
    '''

    # extract instance from id
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    # GET details
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)

    # UPDATE details
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) 

    # DELETE object
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
"""




"""
# Way2 ==> function based views with api_view() decorator

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def article_list(request, format=None):
    '''
    fetch all objects & create object
    '''

    # GET all objects
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    # POST/ create object
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk, format=None):
    '''
    fetch detail, update and delete single object
    '''

    # extract instance from id
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET details
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # UPDATE details
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    # DELETE object
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
"""




"""
# Way3 ==> Class based views using APIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticleAPIView(APIView):
    
    # GET all objects
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    # POST/ create object
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ArticleDetails(APIView):

    # extract instance from id
    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

     # GET details
    def get(self, request, id, format=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # UPDATE details
    def put(self, request, id, format=None):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    # DELETE object
    def delete(self, request, id, format=None):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
"""




"""
# Way4 ==> Class-based GenericAPIViews and mixins

from rest_framework import mixins, generics


class ListCreateRetrieveUpdateDestroyGenericAPIView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
        ):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    lookup_field = 'id'      # default is pk

    def get(self, request, id=None, format=None):
        if not id:
            return self.list(request)
        return self.retrieve(request, id)

    def post(self, request, id=None, format=None):
        return self.create(request)

    def put(self, request, id, format=None):
        return self.update(request, id)

    def delete(self, request, id, format=None):
        return self.destroy(request, id)
"""




"""
# Way5 ==> Class-based Concrete Generic Views

from rest_framework import generics


class ListCreateGenericConcreteView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class RetrieveUpdateDestroyGenericConcreteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'
"""



"""
# Way6 ==> class-based viewsets inheriting APIView

# ViewSet class are same as APIView class and just defined methods are mapped to corresponding HTTP handler methods in urls.py

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


# Both these classes have same methods as above APIView defined classes
# And only defined methods are mapped to corresponding HTTP handler methods in urls.py

# In ViewSet inheriting classes, name of methods can be named anything and just map it properly in urls.py
# Eg - list() can be display(), create() can be create_new(),...

class ListCreateViewSet(ViewSet):   # equivalent to inheriting ViewSetMixin & APIView
    def list(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = ArticleSerializer(data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class RetrieveUpdateDestroyViewSet(ViewSet):
    queryset = Article.objects.all()
    lookup_field = 'id'  # for using router

    def retrieve(self, request, id, format=None): 
        # queryset = Article.objects.all()
        article = get_object_or_404(self.queryset, id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, id, format=None):
        # queryset = Article.objects.all()
        article = get_object_or_404(self.queryset, id=id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def destroy(self, request, id, format=None):
        # queryset = Article.objects.all()
        article = get_object_or_404(self.queryset, id=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
"""



"""
# Way7 ==> class-based GenericViewSet inheriting GenericAPIView 
# And then using this by inheriting GenericViewSet and ModelMixins

# GenericViewSet are same as using GenericAPIViews along with inheriting ModelMixins
# For GenericAPIView class, we define HTTP handler methods and then call corresponding actions methods from ModelMixins
# But for GenericViewSet class, we map actions methods from ModelMixins to HTTP handler methods in urls.py

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class ListCreateRetrieveUpdateDestroyGenericViewSet(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
        ):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    lookup_field = 'id'      # default is pk
"""




# Way8 ==> Class-based concrete GenericViewSet inheriting GenericAPIView and ModelMixins

from rest_framework import viewsets
from rest_framework.decorators import action

# Authentication 
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ListRetrieveGenericViewSet(viewsets.ReadOnlyModelViewSet): # equivalent to inheriting GenericViewSet, ListModelMixin & RetrieveModelMixin
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class GenericModelViewSet(viewsets.ModelViewSet):  # equivalent to inheriting GenericViewSet & all of ModelMixins
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    authentication_classes = [ SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # for adding extra actions, use action decorator
    # @action(detail=True, method=['put'], name='Change Password')
    # def change_password(self, request, pk=None):
    #     pass
