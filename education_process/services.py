def def_serializer() -> None:
    """
    Define a serializer with custom methods to retrieve specific fields from related objects.
    This function defines a serializer with custom methods to retrieve specific fields from related objects.

    Methods:
    - get_subject(self, obj): Retrieve the subject of the object.
    - get_pupil(self, obj): Retrieve the pupil of the object.
    - get_group(self, obj): Retrieve the group of the object.
    - get_score_status(self, obj): Retrieve the score status of the object.

    :return: None
    """

    def get_subject(self, obj):
        return str(obj.subject.get_subject)

    def get_pupil(self, obj):
        return str(obj.pupil.get_pupil)

    def get_group(self, obj):
        return obj.grade.get_grade

    def get_score_status(self, obj):
        return obj.subject.get_score_status
