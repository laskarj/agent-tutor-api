class BaseApplicationError(Exception):
    pass


class AppError(BaseApplicationError):
    pass


class ClientError(AppError):
    pass
