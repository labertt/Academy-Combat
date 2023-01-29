from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_funcionario': True,
        'cadastrar_professor': True,
        'listagem_funcionario': True,
        'listagem_professor': True,
        'cadastrar_aluno': True,
        'listagem_aluno': True,
        'listagem': True,
    }

class Funcionario(AbstractUserRole):
    available_permissions = {
        'cadastrar_aluno': True,
        'listagem_aluno': True,
    }

class Professor(AbstractUserRole):
    available_permissions = {
        'registrar_presenca': True,
        'listagem_aluno': True,
    }