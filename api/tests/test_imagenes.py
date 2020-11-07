from datetime import datetime
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Sorteo, Imagen
from api.serializers import ImagenSerializer

nl = '\n'


class Post200Test(APITestCase):
    def setUp(self):
        sorteo = Sorteo.objects.create(id=1, titulo='titulo', descripcion='descripcion', detalles='detalles', activo=True, fechaHoraSorteo=datetime.now(), costoCarta=999)
        Imagen.objects.create(id=1, principal=True, sorteo=sorteo)
        Imagen.objects.create(id=2, principal=False, sorteo=sorteo)

        stream = BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(stream, format='jpeg')

        uploaded_file = SimpleUploadedFile('./uploads/noCircula.jpg', stream.getvalue(), content_type='image/jpg')

        self.json = {
            "imagen": uploaded_file,
            "principal": True,
            "sorteo": 1
        }

    def test(self):
        response = self.client.post('/api/imagenes/create/', data=self.json, format='multipart')
        print(f'response JSON ===>>> {nl} {response.data} {nl} ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        queryset = Imagen.objects.all()
        serializer = ImagenSerializer(queryset, many=True)
        print(serializer.data)

        for dato in queryset:
            print(f'id: {dato.id}   principal: {dato.principal}   sorteo: {dato.sorteo}   imagen: {dato.imagen}  ')
