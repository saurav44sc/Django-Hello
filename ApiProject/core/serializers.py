from rest_framework import serializers
from .models import Post

# from django import forms

# class PostForm(forms.ModelForm):
#   class Meta:
#     model = Post
#     fields = (
#       'title', 'description'
#     )

# serializers convert the model into the Json format

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = (
      'title', 'description', 'owner'
    )