from rest_framework import serializers


class StudentSerializer(serializers.Serializer):

    student_name = serializers.CharField(max_length=100)

    age = serializers.IntegerField(min_value=3, max_value=18)

    email = serializers.EmailField()

    guardian_name = serializers.CharField(max_length=100)

    phone = serializers.RegexField(regex=r"^\d{10}$")

    learning_difficulty = serializers.BooleanField()

    def validate_student_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Student name must contain at least 3 characters."
            )
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain digits only.")
        return value
