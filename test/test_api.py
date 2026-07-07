import requests
import pytest
from faker import Faker
from conftest import historial

# Configuración
BASE_URL = "https://jsonplaceholder.typicode.com" 
fake = Faker()


class TestJSONPlaceholder:

    # TEST 1: GET - obtener todos los posts (Éxito)
    def test_get_posts_success(self):
        historial("\n=== TEST 1: GET Posts ===")

        # Hacer petición GET
        response = requests.get(f"{BASE_URL}/posts")

        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
        historial("Codigo de estado 200 - correcto")
   

        # Convertir respuesta a JSON
        data = response.json()

        # Validar estructura del JSON
        assert isinstance(data, list), "La respuesta deberia ser una lista"
        assert len(data) > 0, "La lista no deberia estar vacia"
        historial("Estructura JSON correcta")

        # Validar estructura del primer post

        first_post = data[0]
        required_fields = ["userId", "id", "title", "body"]
        for field in required_fields:
            assert field in first_post, f"Falta el campo '{field}' en el post"
        historial("Estructura del post correcta")

        # Validar tipos de datos
        assert isinstance(first_post["id"], int)
        assert isinstance(first_post["title"], str)
        assert isinstance(first_post["body"], str)
        historial("Tipos de datos correctos")

        historial("Test GET Posts completado exitosamente!")

    # TEST 2: POST - Crear un nuevo post (Éxito)

    def test_create_post_success(self):
        """POST /posts - Crear un nuevo post exitosamente"""
        historial("\n=== TEST 2: POST Create Post ===")

        # Datos para el nuevo post
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }

        # Hacer petición POST
        response = requests.post(f"{BASE_URL}/posts", json=post_data)

        # Validar código de estado
        assert response.status_code == 201, f"Esperado 201, obtenido {response.status_code}"

        # Convertir respuesta a JSON
        data = response.json()

        # Validar estructura de respuesta
        exptected_fields = ["id", "title", "body", "userId"]
        for field in exptected_fields:
            assert field in data, f"Falta el campo '{field}' en la respuesta"
        historial("Estructura de respuesta correcta")

        # Validar que los datos se guardaron correctamente
        assert data["title"] == post_data["title"]
        assert data["body"] == post_data["body"]
        assert data["userId"] == post_data["userId"]
        historial("Datos guardados correctamente")

        # Validar que se asignó un ID (simulado por JSONPlaceholder)
        assert data["id"] == 101, f"Expected ID 101, obtenido {data['id']}"
        historial("ID asignado correctamente")
       
        historial("Test CREATE Post completado exitosamente!")

    # TEST 3: DELETE - Eliminar un post (Éxito)

    def test_delete_post_success(self):
        """DELETE /posts/{id} - Eliminar un post exitosamente"""
        historial("\n=== TEST 3: DELETE Post ===")

        # ID del post a eliminar (usamos uno que sabemos que existe))
        post_id = 1

        # Hacer petición DELETE
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")

        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
        historial("Codigo de estado 200 - correcto")

        # JSONPlaceholder devuelve un objeto vacío para Delete exitoso
        data = response.json()
        assert data == {}, f"Esperado un diccionar vacío, obtenido {data}"
        historial("Respuesta DELETE correcta")

        historial("Test DELETE Post completado exitosamente!")

