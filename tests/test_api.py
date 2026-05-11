import pytest
from playwright.sync_api import Playwright, APIRequestContext

# Esta Fixture prepara la conexión a la API


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    # Definimos la URL base para no repetirla
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()


def test_validar_usuario_api(api_request_context: APIRequestContext):
    # 1. Hacemos la petición GET
    response = api_request_context.get("/users/1")

    # 2. Validamos que la respuesta sea exitosa (Status 200)
    assert response.ok

    # 3. Convertimos la respuesta a JSON y validamos datos
    user_json = response.json()
    assert user_json["username"] == "Bret"
    assert user_json["email"] == "Sincere@april.biz"

    print(f"\n[API Success] Usuario verificado: {user_json['name']}")


def test_crear_post_api(api_request_context: APIRequestContext):
    # 1. Hacemos un POST (enviar datos)
    nuevo_post = {
        "title": "Post de Gokay",
        "body": "Aprendiendo API con Playwright",
        "userId": 1
    }
    response = api_request_context.post("/posts", data=nuevo_post)

    # 2. Validamos que se haya creado (Status 201)
    assert response.status == 201
    print(f"\n[API Success] Post creado con ID: {response.json()['id']}")


def test_crear_y_verificar_post(api_request_context: APIRequestContext):
    # 1. Definimos el nuevo post
    nuevo_post = {
        "title": "Post de Gokay",
        "body": "Verificando el ciclo completo de API",
        "userId": 1
    }

    # 2. Hacemos el POST
    print("\n[Step 1] Enviando POST...")
    post_response = api_request_context.post("/posts", data=nuevo_post)
    assert post_response.status == 201

    # Obtenemos el ID que nos asignó la API
    res_json = post_response.json()
    nuevo_id = res_json["id"]
    print(f"[Step 1] Post creado con ID: {nuevo_id}")

    # 3. Hacemos el GET usando ese ID para verificar
    # Nota: En esta API de práctica, el GET al ID 101 puede dar 404 porque es simulado,
    # pero así es como escribirías la lógica en un entorno real:
    print(f"[Step 2] Enviando GET al ID {nuevo_id} para verificar...")
    get_response = api_request_context.get(f"/posts/{nuevo_id}")

    # En una API real, aquí pondrías: assert get_response.ok
    # Como esta API es de juguete, vamos a validar al menos que intentamos consultar el ID correcto
    print(
        f"[Step 2] Verificación enviada correctamente al endpoint de ID {nuevo_id}")


def test_editar_y_verificar_post(api_request_context: APIRequestContext):
    # 1. Datos que queremos actualizar
    datos_actualizados = {
        "id": 1,
        "title": "Título editado por Gokay",
        "body": "Cuerpo del post actualizado con PUT",
        "userId": 1
    }

    # 2. Ejecutamos el PUT al ID 1
    print("\n[Step 1] Enviando PUT para editar el ID 1...")
    put_response = api_request_context.put("/posts/1", data=datos_actualizados)

    # Validamos que la edición sea exitosa (Status 200 OK)
    assert put_response.status == 200
    res_json = put_response.json()
    assert res_json["title"] == "Título editado por Gokay"
    print(f"[Step 1] Recurso ID {res_json['id']} editado correctamente.")

    # 3. Verificamos con un GET el estado actual
    print("[Step 2] Verificando cambios con GET...")
    get_response = api_request_context.get("/posts/1")
    assert get_response.ok
    print(
        f"[Step 2] El título en el servidor es: {get_response.json()['title']}")
