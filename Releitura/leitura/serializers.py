from rest_framework import serializers
from leitura.models import Loja,Livro

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'
        
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome']
        depth = 1