class DomainError(Exception):
    """Base domain exception. Framework-agnostic — HTTP mapping happens in the presentation layer."""

class TagAlreadyExists(DomainError):
    pass

class UserAlreadyExists(DomainError):
    pass

class InvalidCredentials(DomainError):
    pass