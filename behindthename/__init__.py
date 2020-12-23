import requests
from behindthename import usages
from behindthename import exceptions

class Request(object):
  Genders = {'f', 'm', 'u', 'both'}
  Usages = usages.load()
  def __init__(self, api_key=None, exact=None, gender=None, name=None, number=None, surname=None, usage=None, **kwargs):
    self.slug = 'https://www.behindthename.com/api/'
    self.key = api_key
    self.gender = gender
    self.number = number
    self.usage = Request.Usages[usage.lower()] if usage else usage
    self.surname = surname
    self.exact = exact
    self.name = name
  
  def validate(self):
    self.validate_key()
  
  def validate_key(self):
    if key is None:
      raise exceptions.KeyValidationError('API key cannot be none!')
  
  def validate_gender(self):
    if self.gender not in Request.Genders:
      valid = ', '.join([f'{g!r}' for g in list(Request.Genders)])
      e = f'{self.gender!r} is not a valid gender. Use one of {valid}.'
      raise exceptions.GenderValidationError(e)
  
  def validate_gender_or_none(self):
    if self.gender is None:
      return
    self.validate_gender()
  
  def validate_usage(self):
    if self.usage not in Request.Usages:
      e = f'{self.usage!r} is not a valid usage code.'
      raise exceptions.UsageValidationError(e)
  
  def validate_usage_or_none(self):
    if self.usage is None:
      return
    self.validate_usage()
  
  def validate_name(self):
    if not self.name or not isinstance(self.name, str):
      e = f'{self.name!r} is not a valid name or is empty.'
      raise exceptions.NameValidationError(e)
  
  def validate_count(self):
    if self.number not in range(1, 7):
      raise exceptions.CountValidationError(f'{self.number} not in range [1,6].')


class NameLookup(Request):
  def __init__(self, api_key=None, name=None, exact=False, **kwargs):
    super().__init__(api_key, name=name, exact=exact, **kwargs)
    self.url = self.slug + 'lookup.json'
    self.validate()
  
  def get(self):
    parameters = {
      'name' : self.name,
      'exact': 'yes' if self.exact else 'no',
      'key'  : self.key
    }
    r = requests.get(self.url, parameters)
    if r.status_code != requests.codes.ok:
      r.raise_for_status()
    return r.json()
  
  def validate(self):
    self.validate_name()


class RelatedName(Request):
  def __init__(self, api_key=None, gender=None, name=None, usage=None, **kwargs)):
    super().__init__(
      api_key=api_key,
      name=name,
      usage=usage,
      gender=gender,
      **kwargs)
    
    self.url = self.slug + 'related.json'
    self.validate()
    
  def get(self):
    parameters = {
      'gender' : self.gender,
      'usage'  : self.usage,
      'name'   : self.name,
      'key'    : self.key
    }
    r = requests.get(self.url, parameters)
    if r.status_code != requests.codes.ok:
      r.raise_for_status()
    return r.json()
  
  def validate(self):
    self.validate_name()
    self.validate_usage_or_none()
    self.validate_gender_or_none()


class RandomName(Request):
  def __init__(self, api_key=None, gender='both', number=2, surname=True, usage='all', **kwargs):
    super().__init__(
      api_key=api_key,
      gender=gender,
      number=number,
      surname=surname,
      usage=usage
      **kwargs)
    self.url = self.slug + 'random.json'
    self.validate()
  
  def get(self):
    parameters = {
      'gender' : self.gender,
      'usage'  : self.usage,
      'number' : self.number,
      'randomsurname' : 'yes' if self.surname else 'no',
      'key' : self.key
    }
    r = requests.get(self.url, parameters)
    if r.status_code != requests.codes.ok:
      r.raise_for_status()
    return r.json()
    
  def validate(self):
    self.validate_usage()
    self.validate_gender()
    self.validate_count()
  
  
