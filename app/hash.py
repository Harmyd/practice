from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

class Hash():
    def hash_password(password):
        return password_context.hash(password)
    def verify_hash(plain_password,Hashed_password):
        return password_context.verify(plain_password,Hashed_password)