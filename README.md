# Microsserviços com Docker e API Gateway

Este repositório contém um exemplo simples com 3 serviços:

- `users_service` — fornece dados de usuários (lista fixa)
- `orders_service` — retorna pedidos por usuário; consulta o `users_service` internamente para validar usuário
- `gateway_service` — API Gateway que expõe endpoints públicos em `:8080` e encaminha para os serviços

Como rodar

No PowerShell (Windows):

```powershell
# Build e subir todos os serviços:
docker-compose up --build

# Testar endpoints (em outra janela):
curl http://localhost:8080/api/users
curl http://localhost:8080/api/orders/1
```

