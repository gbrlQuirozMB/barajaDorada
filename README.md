# Baraja Dorada Backend

**----------------------------------------------------------SORTEOS ** 
http://127.0.0.1:8000/api/sorteos/create/  
http://127.0.0.1:8000/api/sorteos/list/  
http://127.0.0.1:8000/api/sorteos/list/?activo=true  
http://127.0.0.1:8000/api/sorteos/detail/3/  
http://127.0.0.1:8000/api/sorteos/delete/2/  
http://127.0.0.1:8000/api/sorteos/update/2/  
  
LISTA  
[  
  {  
    "id": 1,  
    "titulo": "CENA AL ATARDECER",  
    "descripcion": "lorem ipsum",  
    "detalles": "lorem ipsum",  
    "imagen": "img/img.img",  
    "activo": true,  
    "fechaHoraSorteo": "dd/mm/yyyy"  
  },  
  {  
    "id": 1,  
    "titulo": "CENA AL ATARDECER",  
    "descripcion": "lorem ipsum",  
    "detalles": "lorem ipsum",  
    "imagen": "img/img.img",  
    "activo": true,  
    "fechaHoraSorteo": "dd/mm/yyyy"  
  },  
  {  
    "id": 1,  
    "titulo": "CENA AL ATARDECER",  
    "descripcion": "lorem ipsum",  
    "detalles": "lorem ipsum",  
    "imagen": "img/img.img",  
    "activo" : true,  
    "fechaHoraSorteo": "dd/mm/yyyy"  
  }  
]  
  
DETALLE  
{  
    "id": 1,  
    "titulo": "lorem ipsum",  
    "descripcion": "lorem ipsum",  
    "detalles": "lorem ipsum",  
    "activo": true,  
    "fechaHoraSorteo": "2020-11-01T09:09:00-06:00",  
    "imagenes": [  
        {  
            "id": 1,  
            "imagen": "http://127.0.0.1:8000/api/sorteos/detail/1/static/img/blusbo_sPAqqWD.png",  
            "principal": true,  
            "sorteo": 1  
        },  
        {  
            "id": 2,  
            "imagen": "http://127.0.0.1:8000/api/sorteos/detail/1/static/img/mayol_kYsgs9E.png",  
            "principal": false,  
            "sorteo": 1  
        }  
    ]  
}  
  
  
  
**----------------------------------------------------------CARTAS ** 
http://127.0.0.1:8000/api/cartas/create/  
http://127.0.0.1:8000/api/cartas/list/  
http://127.0.0.1:8000/api/cartas/detail/2/  
http://127.0.0.1:8000/api/cartas/delete/2/  
http://127.0.0.1:8000/api/cartas/update/2/  
  
LISTA  
[  
  {  
    "id": 3,  
    "nombre": "3 de corazones",  
    "imagen": "http://127.0.0.1:8000/api/cartas/list/static/img/blusbo.png"  
  },  
  {  
    "id": 45,  
    "nombre": "6 de treboles",  
    "imagen": "http://127.0.0.1:8000/api/cartas/list/static/img/blusbo.png"  
  },  
  {  
    "id": 22,  
    "nombre": "9 de espadas",  
    "imagen": "http://127.0.0.1:8000/api/cartas/list/static/img/blusbo.png"  
  }  
]  
  
DETALLE  
{  
    "id": 1,  
    "nombre": "ninguno",  
    "imagen": "http://127.0.0.1:8000/api/cartas/detail/1/static/img/blusbo.png"  
}  
  
  
  
**----------------------------------------------------------IMAGENES**  
http://127.0.0.1:8000/api/imagenes/create/  
http://127.0.0.1:8000/api/imagenes/list/  
http://127.0.0.1:8000/api/imagenes/detail/2/  
http://127.0.0.1:8000/api/imagenes/delete/2/  
http://127.0.0.1:8000/api/imagenes/update/2/  
  
LISTA  
[  
    {  
        "id": 1,  
        "imagen": "http://127.0.0.1:8000/api/imagenes/list/static/img/blusbo_sPAqqWD.png",  
        "principal": true,  
        "sorteo": 1  
    },  
    {  
        "id": 2,  
        "imagen": "http://127.0.0.1:8000/api/imagenes/list/static/img/mayol_kYsgs9E.png",  
        "principal": false,  
        "sorteo": 1  
    }  
]  
  
DETALLE  
{  
    "id": 1,  
    "imagen": "http://127.0.0.1:8000/api/imagenes/detail/1/static/img/blusbo_sPAqqWD.png",  
    "principal": true,  
    "sorteo": 1  
}
