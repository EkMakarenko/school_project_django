def def_serializer():

    def get_subject(self, obj):
        return str(obj.subject.get_subject)

    def get_pupil(self, obj):
        return str(obj.pupil.get_pupil)

    def get_group(self, obj):
        return obj.grade.get_grade

    def get_score_status(self, obj):
        return obj.subject.get_score_status

    def get_group(self, obj):
        return obj.grade.get_grade