from django.core.validators import   RegexValidator
from django.utils.translation   import ugettext_lazy as _  
class HexadecimalValidator(RegexValidator):
     regex = r'#[a-fA-F0-9]{6}' 
     message =_('Color should be a 6 digit hexadecimal number.')   
     code  =  'VAL_ERR: invalid color code'