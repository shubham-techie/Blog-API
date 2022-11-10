# Blog-API
## A RESTFUL API for Blog designed using Django-Rest-Framework while learning.
<br>

### Concepts learnt :

### [Serializers](https://github.com/shubham-techie/Blog-API/blob/master/app/serializers.py) : 
1. Serializers creation from scratch by directly inheriting Serializer class
2. Serializer creation by inheriting ModelSerializer class \
  *(**Note** : ModelSerializer is built on-top of Serializer class)*
  <br>
  
### [Views](https://github.com/shubham-techie/Blog-API/blob/master/app/views.py) :
Views can be creating in different ways, depending on the requirement and usage. Following are only 8 ways :

### Function-based views -
1. without using api_view() decorator
2. using api_view() decorator

### Class-based views -
3. APIView \
   *(**Note** : Here, define HTTP handler methods)*
4. GenericAPIView and ModelMixins \
   *(**Note** : Here, actions methods are being defined in ModelMixins and we define HTTP handler methods and return corresponding action methods)*
5. Concrete GenericAPIViews \
   *(**Note** : These are pre-defined implementation of GenericAPIView and ModelMixins)*

### Class-based Viewsets -
(Viewsets are nothing but APIViews, but here ***action methods are mapped to HTTP handler methods*** in urls.py) \
(Viewsets ***overrides as_view() method*** to mapping HTTP handler methods and action methods via key-value pair) \
(And then here comes the role of ***routers, as it has predefined mapped handler methods***) 

6. ViewSet \
   *(**Note** : It is built by inheriting APIView and ViewSetMixin)* 
7. GenericViewSet \
   *(**Note** : It is built by inheriting GenericAPIView and ViewSetMixin)* 
8. Concrete GenericViewSets \
   *(**Note** : These are pre-defined implementation of GenericViewSet and ModelMixins)* 
   
   
## [MY_DRF_Handwritten_Notes](https://drive.google.com/file/d/1b3Icw5JfjeXxsYSUloKlLd48GG2EL-YM/view?usp=sharing)
