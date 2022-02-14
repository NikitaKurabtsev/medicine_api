from dataclasses import field

from rest_framework import serializers

from medicine.models import Company, Medicine


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    medicines = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        name='medicine-detail', #configure with router
    )

    class Meta:
        model = Company
        fields = (
            'url', 
            'pk', 
            'name', 
            'created',
            'medicines'
        )

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.SlugRelatedField(
        queryset=Company.objects.all(), 
        slug_field='slug'
    )

    class Meta:
        model = Medicine
        fields = (
            'name',
            'medicine_category',
            'company',
            'description',
            'release_date',
            'expiration_date',
        )
