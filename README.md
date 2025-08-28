# das-2-2025-2
AWS Cloud Architecting

RODAR PYHTHON 

cd s3
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# AULA 30/07

- AWS Well-Architected framework
Documento de boas práticas para AWS

Security Pilar

Pilar performance
Serverless
S3 - Hospedando aplicação web (SPA) - React, Angular, Vue

Cost optimization Pilar

Sustainability Pilar
Dont waste

AWS Well-Architected Tool
- Helps to understand if your app infra is right for the cloud.

Implementar escalabilidade

Amazon EC2 Auto scaling
- Scale in
- Scale out

Observabilidade 

AWS CloudWatch - logs

Designing services, not servers.

Securing infrastructure with encryption in transit and at rest.

# AULA 06/08

IAM

# AULA 13/08
IAM Roles -> definição para cargos temporários para usuários.

Policies e permissions
Identity based policies -> Permissão para usuário.
Resource based policies -> Permissão para um recurso. (Definir comportamento global, todos usuários que mexem no s3 só podem ler, por exemplo)


# AULA 20/08

S3 -> Block storage, File storage, object store (foto,json,xml);

Dados ilimitados.
Todo objeto recebe uma url publica, mas não necessariamente estará disponível para visualização. 

Durabilidade -> 11 noves, 99.999999999
Disponibilidade -> 4 noves, 99.99
Alta performance

Hospedar sites estáticos

Buckets são globais, porém um balde sempre está em uma região.
Multipart upload

Upload 

internet -> S3 Mais lento
internet -> edge location (cloudfront) -> s3 Mais rápido

AWS Transfer Family
Conectar no s3 via protocolo FTP.

Storage class
Standard, Intelligent tiering, infrequent-access, glacier instant retrieval, glacier flexible retriever, glacier deep archive;

# AULA 27/08

S3 -> Escolher região:
leis -> latência -> features do S3 por região -> custo de armazenamento

AWS S3 Inventory
API além da básica para gerar relatório sobre os objetos do bucket
