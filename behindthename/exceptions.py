class BehindTheNameError(Exception):
  pass

class ValidationError(BehindTheNameError):
  pass

class CountValidationError(ValidationError):
  pass

class GenderValidatioNError(ValidationError):
  pass

class KeyValidationError(ValidationError):
  pass

class NameValidatioNError(ValidationError):
  pass

class UsageValidationError(ValidationError):
  pass


