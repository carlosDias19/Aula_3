import os
import sys

# Adiciona o diretório pai de 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.domain.entities import Livro, Usuario
    from src.domain.value_objects.email import Email
    from src.domain.value_objects.isbn import ISBN

    print("Importações do domínio funcionando")

    # Teste de criação de entidades
    livro = Livro(id="", titulo="Clean Architecture", autor="Robert Martin", isbn=ISBN("978-0134494166"))
    print(f"Livro criado: {livro.titulo}")

    email = Email("teste@email.com")
    usuario = Usuario(id="", nome="João Silva", email=email)
    print(f"Usuário criado: {usuario.nome}")

    # Teste de comportamentos
    livro.emprestar()
    print(f"Livro emprestado: disponível = {livro.disponivel}")

    livro.devolver()
    print(f"Livro devolvido: disponível = {livro.disponivel}")

    print("Estrutura DDD funcionando corretamente!")

    from src.infrastructure.repositories.user_repository import UserRepository
    from src.application.use_case.create_user_use_case import CreateUserUseCase
    from src.application.use_case.list_users_use_case import ListUsersUseCase
    from src.application.use_case.update_user_use_case import UpdateUserUseCase
    from src.presentation.schemas.user_schema import UserCreateSchema, UserUpdateSchema

    def main():
        # Instanciando repositório e use cases
        repo = UserRepository()
        create_uc = CreateUserUseCase(repo)
        list_uc = ListUsersUseCase(repo)
        update_uc = UpdateUserUseCase(repo)

        # Criando múltiplos usuários
        users_data = [
            UserCreateSchema(nome="João Silva", email="joao@email.com"),
            UserCreateSchema(nome="Maria Souza", email="maria@email.com"),
            UserCreateSchema(nome="Carlos Dias", email="carlos@email.com"),
            UserCreateSchema(nome="Yuri Martins", email="yuri@email.com"),
        ]
        usuarios_criados = []
        for user_data in users_data:
            usuario = create_uc.execute(user_data.model_dump())
            usuarios_criados.append(usuario)
            print(f"Usuário criado: {usuario.nome} - {usuario.email}")

        # Listando usuários
        usuarios = list_uc.execute()
        print("Usuários cadastrados:")
        for u in usuarios:
            print(f"- {u.nome} ({u.email})")

        # Atualizando o segundo usuário
        update_data = UserUpdateSchema(nome="Maria Souza Atualizada")
        usuario_atualizado = update_uc.execute(usuarios_criados[1].id, update_data.model_dump(exclude_unset=True))
        print(f"Usuário atualizado: {usuario_atualizado.nome} - {usuario_atualizado.email}")

    if __name__ == "__main__":
        main()

except Exception as e:
    print(f"Erro: {e}")
    import traceback

    traceback.print_exc()