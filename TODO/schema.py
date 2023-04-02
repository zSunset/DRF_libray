import graphene
from graphene_django import DjangoObjectType
from TODO.models import ToDo_notes, Project
from authors.models import CustomUser

class ToDo_notesType(DjangoObjectType):
    class Meta:
        model = ToDo_notes
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'

class Query(graphene.ObjectType):
    todo_notes = graphene.List(ToDo_notesType)
    project = graphene.List(ProjectType)
    custom_user = graphene.List(CustomUserType)
    
    def resolve_todo_notes(root, info):
        return ToDo_notes.objects.all()
    
    def resolve_project(root, info):
        return Project.objects.all()
    
    def resolve_custom_user(root, info):
        return CustomUser.objects.all()



schema = graphene.Schema(query=Query)


"""query{project{
  name
  userSet{
    username
  }
}}"""


"""{
  "data": {
    "project": [
      {
        "name": "Python",
        "userSet": []
      },
      {
        "name": "JS",
        "userSet": [
          {
            "username": "admin"
          },
          {
            "username": "sunset"
          },
          {
            "username": "zsunset"
          }
        ]
      },
      {
        "name": "JS",
        "userSet": [
          {
            "username": "admin"
          },
          {
            "username": "locust"
          }
        ]
      }
    ]
  }
}"""