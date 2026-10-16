def validar_acesso(id_cracha:str, horario: int) -> dict:
    """
    Função que valida o acesso do colaborador ao armário de chave
    
    Args:
        id_cracha (str): ID do crachá do colaborador.
        horario (int): horario de retirada ou devolução.

    returns:
        dict: Dicionário com o resultado da validação.
    """
    colaborador_senai = colaboradores.get(id_cracha)
    

