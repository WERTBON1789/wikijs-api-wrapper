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
