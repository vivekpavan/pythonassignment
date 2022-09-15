from distutils.log import error
from pickletools import int4
from rest_framework import serializers
from .models import apiModel
from django.http import Http404

class apiSerializer(serializers.ModelSerializer):
    mystring = serializers.SerializerMethodField()
    def get_mystring(self,apiModel):
        alpha = apiModel.string[:4]
        a = (apiModel.string[4:])
        b = a.replace('.', '')
        try:
            c = [int(numeric_string) for numeric_string in b]
        except ValueError:
            raise Http404
            
        A = []
        while c:
            max = 0
            for i in c:
                if i > max:
                    max = i
            s = "%s" % max
            count = (b.count(s))
            for i in range(0, count):
                A.append(max)
                c.remove(max)
            A.append('.')

        B = ''.join([str(x) for x in A])
        return alpha + B
        

    class Meta:
        model = apiModel
        fields = ['string','mystring']