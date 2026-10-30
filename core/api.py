# core/api.py
from ninja import NinjaAPI, Schema
from django.db import connection
# Instância principal do Django Ninja
api = NinjaAPI(
title="API Armário Inteligente SENAI",
version="1.0.0",
description="Serviços RESTful para validação e controle de chaves
RFID/NFC"
)
# 1. Schemas Pydantic (DTOs de Entrada e Saída)
class StatusResponseSchema(Schema):
status: str
servidor: str
versao: str
class ConsultaUUIDSchema(Schema):
uuid: str
tipo_identificado: str # 'DOCENTE', 'CHAVE' ou 'DESCONHECIDO'
autorizado: bool
mensagem: str
# 2. Endpoint de Saúde do Sistema (Health Check)
@api.get("/status", response=StatusResponseSchema, tags=["Sistema"])
def status_sistema(request):
return {
"status": "ONLINE",
"servidor": "Django Ninja + Supabase",
"versao": "1.0.0"
}


@api.get("/consulta-uuid/{uuid}", response=ConsultaUUIDSchema, tags=
["Portaria / Claviculário"])
def consultar_uuid(request, uuid: str):
"""
Consulta um UUID lido pelo leitor RFID/NFC.
Identifica se pertence a um docente ativo ou a uma chave e verifica
autorização.
"""
uuid_limpo = uuid.strip().upper()
# Consulta no banco de dados Supabase via cursor
with connection.cursor() as cursor:

# 1. Verifica se e um Cracha de Docente
cursor.execute(
"SELECT nome_docente, status_docente FROM tb_docente WHERE

uuid_cracha = %s;",
[uuid_limpo]
)
docente = cursor.fetchone()
if docente:
nome, ativo = docente
if ativo:
return {
"uuid": uuid_limpo,
"tipo_identificado": "DOCENTE",
"autorizado": True,
"mensagem": f"Docente {nome} identificado e ativo."
}
return {
"uuid": uuid_limpo,
"tipo_identificado": "DOCENTE",
"autorizado": False,
"mensagem": f"Acesso Negado: Docente {nome} está

inativo."
}
# 2. Se não for docente, verifica se e uma Tag de Chave
cursor.execute(
"SELECT id_nicho, status_nicho FROM tb_nicho WHERE

uuid_tag_chave = %s;",
[uuid_limpo]
)
chave = cursor.fetchone()
if chave:
id_nicho, status_nicho = chave
return {
"uuid": uuid_limpo,
"tipo_identificado": "CHAVE",
"autorizado": True,
"mensagem": f"Chave vinculada ao Nicho #{id_nicho}

(Status: {status_nicho})."

}
# 3. UUID não localizado no banco
return {
"uuid": uuid_limpo,
"tipo_identificado": "DESCONHECIDO",
"autorizado": False,
"mensagem": "Cartão/Tag não cadastrado no sistema."
}