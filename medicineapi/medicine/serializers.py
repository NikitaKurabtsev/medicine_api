from rest_framework import serializers

from medicine.models import Company, Medicine


class CompanySerializer(serializers.ModelSerializer):
    medicines = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="medicine-detail",
    )
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Company
        fields = (
            "url",
            "pk",
            "name",
            "owner",
            "created",
            "medicines",
        )


class MedicineSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        queryset=Company.objects.all(), 
        slug_field="slug",
    )
    release_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d", "iso-8601"])
    expiration_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d", "iso-8601"])

    class Meta:
        model = Medicine
        fields = (
            "url",
            "pk",
            "name",
            "medicine_category",
            "company",
            "description",
            "release_date",
            "expiration_date",
        )

    def validate_company(self, value):
        """
        Check that request user choose the company that he own.
        """
        if value.owner != self.context["request"].user:
            raise serializers.ValidationError(
                "You have to set up your company to add medicines."
            )

        return value

    def validate_description(self, value):
        """
        Check that description is unique and
        length bigger than 50 characters.
        """
        medicines = Medicine.objects.filter(description=value)

        if medicines.exists():
            raise serializers.ValidationError(
                "Description already exists"
            )
        if len(value) < 50:
            raise serializers.ValidationError(
                "Description must be bigger than 50 characters"
            )

        return value

    def validate(self, data):
        """
        Check that expiration date bigger then release date.
        """
        if data["release_date"] >= data["expiration_date"]:
            raise serializers.ValidationError(
                {"release_date": "Release date must be less then expiration date"}
            )
        if data["expiration_date"] <= data["release_date"]:
            raise serializers.ValidationError(
                {"expiration_date": "Expiration date must be bigger then release date"}
            )

        return data
