
from rest_framework import serializers
from api.v1.models import Student

# ModelSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'city']
        # fields='__all__'
        # exclude=['roll_no']


# Normal Serialier

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     roll_no = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll_no = validated_data.get('roll_no', instance.roll_no)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
