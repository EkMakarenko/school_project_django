class TeacherService:
    @staticmethod
    def update_image(serializer, instance, request) -> None:
        """
        Update the image of a specific instance. This function validates the serializer and, if valid, deletes the
        existing image associated with the instance and updates it with the new image provided in the request data.

        :param serializer: An instance of a serializer used to validate the data
        :param instance: The specific instance for which the image needs to be updated
        :param request: The request object containing the new image data
        :return: None
        """

        if serializer.is_valid(raise_exception=True):
            instance.image.delete(save=True)
            instance.image = request.data['image']
