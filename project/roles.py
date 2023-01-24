from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_funcionario': True,
        'cadastrar_professor': True,
        'listagem_funcionario': True,
        'listagem_professor': True,
    }

class Funcionario(AbstractUserRole):
    available_permissions = {
        'cadastrar_aluno': True
    }

class Professor(AbstractUserRole):
    available_permissions = {
        'registro_de_presenca': True
    }