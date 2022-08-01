from enum import Enum
from wikijspy.types.general import Output


class AuthenticationStrategyOutput(Output):
    _validation_list = [
        "key",
        "props",
        "title",
        "description",
        "isAvailable",
        "useForm",
        "usernameType",
        "logo",
        "color",
        "website",
        "icon"
    ]

class AuthenticationActiveStrategyOutput(Output):
    _validation_list = [
        "key",
        "strategy",
        "displayName",
        "order",
        "isEnabled",
        "config",
        "selfRegistration",
        "domainWhitelist",
        "autoEnrollGroups"
    ]

class AuthenticationUserErrors(Enum):
    Nothing = 0
    AuthGenericError = 1001
    AuthLoginFailed = 1002
    AuthProviderInvalid = 1003
    AuthAccountAlreadyExists = 1004
    AuthTFAFailed = 1005
    AuthTFAInvalid = 1006
    BruteInstanceIsInvalid = 1007
    BruteTooManyAttempts = 1008
    UserCreationFailed = 1009
    AuthRegistrationDisabled = 1010
    AuthRegistrationDomainUnauthorized = 1011
    InputInvalid = 1012
    AuthAccountBanned = 1013
    AuthAccountNotVerified = 1014
    AuthValidationTokenInvalid = 1015
    UserNotFound = 1016
    UserDeleteForeignConstraint = 1017
    UserDeleteProtected = 1018
    AuthRequired = 1019
    AuthPasswordInvalid = 1020
