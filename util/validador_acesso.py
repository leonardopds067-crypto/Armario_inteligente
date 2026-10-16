requisicao = {
    "docente_ativo": True,
    "hora_atual": 4,
    "nicho_ocupado": False,
    "chave_solicitada": "Lab 01"
}

if not requisicao["docente_ativo"]:
    print("Acesso Negado: Cadastro Inativo.")
elif requisicao["hora_atual"] >= 23 or requisicao["hora_atual"] < 5:
    print("Acesso Negado: Trava Noturna  (indisponivel entre 23:00 e 05:00).")
elif requisicao["nicho_ocupado"]:
    print("Acesso Negado: Chave Indisponivel.")
else:
    print(f"Acesso Concedido: Chave do {requisicao['chave_solicitada']} Liberada.")


colaboradores={
    "123": {
        "nome_completo": "Equino egua"
        "tipo_cargo": "docente",
        "ativo": "true",
        "admin": "false",
        "num_chaves_em_uso": 1,
    }

    "321": {
            "nome_completo": "Equino suino"
            "tipo_cargo": "cordenação",
            "ativo": "true",
            "admin": "false",
            "num_chaves_em_uso": 1,
        }
    "132": {
            "nome_completo": "Equino ave"
            "tipo_cargo": "limpeza",
            "ativo": "false",
            "admin": "false",
            "num_chaves_em_uso": 1,
        }

    "123": {
            "nome_completo": "Equino egua"
            "tipo_cargo": "docente",
            "ativo": "true",
            "admin": "false",
            "num_chaves_em_uso": 1,
        }
}
