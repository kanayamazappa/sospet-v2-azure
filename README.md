# SOSPetV2

### Reestruturação para uma arquitetura horizontal.

Banco de dados Mysql - hospedado no azure (Servidor flexível do Banco de Dados do Azure para MySQL);

API's - 2 instancias hospedadas no azure (Instâncias de contêiner) - imagem [b7d9bda0c3de/sospetv2azure_api:latest](https://hub.docker.com/repository/docker/b7d9bda0c3de/sospetv2azure_api), criada com Python 3, Django, Django Rest Framework.

FRONT's - 2 instancias hospedadas no azure (Instâncias de contêiner) - imagem [b7d9bda0c3de/sospetv2azure_web:latest](https://hub.docker.com/repository/docker/b7d9bda0c3de/sospetv2azure_web), criada com Python 3, Django

LOAD BALANCER API - 1 instancias hospedadas no azure (Instâncias de contêiner) - imagem [nginx:latest](https://hub.docker.com/_/nginx)
LOAD BALANCER WEB - 1 instancias hospedadas no azure (Instâncias de contêiner) - imagem [nginx:latest](https://hub.docker.com/_/nginx)

### Caminhos

Os caminhos são:

- MYSQL: sospetv2.mysql.database.azure.com
- API 1: http://sospet-api1.eastus.azurecontainer.io
- API 2: http://sospet-api2.eastus.azurecontainer.io
- BALANCER API: http://sospet-api.eastus.azurecontainer.io
- FRONT 1: http://sospet-web1.eastus.azurecontainer.io
- FRONT 2: http://sospet-web2.eastus.azurecontainer.io
- BALANCER FRONT: http://sospet-web.eastus.azurecontainer.io

### Backup do Mysql

O arquivo se encontra aqui na raiz do projeto: sospet.sql
