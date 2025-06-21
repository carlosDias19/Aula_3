from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    nome: str
    email: EmailStr

class UserUpdateSchema(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None