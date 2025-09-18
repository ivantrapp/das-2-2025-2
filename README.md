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

# AULA 03/09 Cloud computing
- Serviços computacionais da AWS (EC2)
- EC2 -> Maquina virtual
- On-demand ($$$), Reserved instance ($$), Spot-instance($)
- EKS, ECS -> Containers
- LightSail -> Virtual Private Servers (VPS);
- Elastic Beanstalk - PaaS;
- Lambda e Fargate - Serverless;
- Amazon Machine Images (AMI)
- Tipos de Instâncias
- Tipos de Storage (EBS/Instance Store)
- Acesso via SSH

# AULA 10/09

- Instance store: Cache foda. Não persistente.
Hd físico na placa mãe
- Amazon EBS: Hd para EC2. Persistente.
Precisa monitorar saúde dos discos provisionados (fazer backup e trocar de volume EBS de tempos em tempos) 

- EBS e S3 não é fileshare;

- Fileshares AWS -> Amazon EFS (linux) e Amazon FSx (windows)

- Amazon EFS -> Linux
- Elastic Fileshare, protocolo NFS, petabytes de storage;
- Copia em 3 az diferente, com 3 placas de redes;

- Amazon FSx -> 4 tipos
- For windows, For NETAPP, For openzfs, For luster HPC(High performance);
- Não é elastico
- Compatível com Linux

# AULA 17/09

AMI -> BASIC, SILVER, GOLDEN;
Maquinas virtuais pré configuradas.

Placement groups -> Pode definir localização física da maquina virtual.
Estratégias de placement -> Cluster, Spread, Partition;

Cluster -> Colocar no mesmo data center, no mesmo rack fisico, alta performance.
Spread -> Maquinas espalhadas em varios data center dentro da mesma regiao, alta disponibilidade.
Partition -> Meio termo, não agrupa maquinas com o mesmo grupo lógico de dados.

Precificação EC2

- On-demand, 
- Reserved instance (reservar maquina por x anos),
- Savings plans (commit de assinatura de ec2 basicamente) 
- Spot instance (usa maquinas ociosas, mas pode cair a qualquer momento pela aws pegar de volta a maquina).

REDES NA AWS

Amazon VPC -> Rede da aws
Vpc está em uma região.
Subnet está em uma zona de disponibilidade.

Subnet publica: visivel para internte
1- Internet gateway -> roteador
2- subnet publica
3- ip publico internet gateway

Peering conection
Conexão entre 2 vpc

AWS Site-to-site VPN
Empresa -> Customer gateway -> internet -> Virtual gateway -> AWS

AWS Direct Connect
Fibra óptica da empresa pra região.

VPC Endpoints
Túnel por dentro da aws para falar com outro serviço dentro da aws.

Vpc endpoint gateway -> s3 e dynamoDB, muito manual, gratis.
Vpc endpoint interface -> Conecta com quase todos serviços, fácil de usar e precisa pagar.

AWS Transit gateway
Hub de redes, faz a conexão de tudo de redes entre vpc, peering, vpn etc.
Por região.
É possível conectar 2 AWS Transit Gateway com peering e fazer a wan.

Firewall na AWS 

Security group firewall -> inbound and outbound rule; Stateful
Network ACLs -> Stateless

A -> IPV4
AAAA -> IPV6
CNAME -> Apontando para outro dns

Amazon Route 53
