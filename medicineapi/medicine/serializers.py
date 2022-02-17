from rest_framework import serializers

from medicine.models import Company, Medicine


class CompanySerializer(serializers.ModelSerializer):
    medicines = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='medicine-detail', #configure with router
    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Company
        fields = (
            'url',
            'pk',
            'name',
            'owner',
            'created',
            'medicines',
        )


class MedicineSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        queryset=Company.objects.all(), 
        slug_field='slug',
    )

    class Meta:
        model = Medicine
        fields = (
            'url',
            'pk',
            'name',
            'medicine_category',
            'company',
            'description',
            'release_date',
            'expiration_date',
        )

    def validate_company(self, value):
        '''
        Check that request user choose the company that he own.
        '''
        if value.owner != self.context['request'].user:
            raise serializers.ValidationError(
                'You have to set up a company to add medicines.'
            )
        return value
