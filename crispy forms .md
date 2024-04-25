# Install this plugin using pip:
  
    
    pip install crispy-bootstrap5
    


# Usage
You will need to update your project's settings file to add crispy_forms and crispy_bootstrap5 to your projects INSTALLED_APPS. Also set bootstrap5 as and allowed template pack and as the default template pack for your project


INSTALLED_APPS = (

    ...
    
    "crispy_forms",
    
    "crispy_bootstrap5",
    
    ...
    
)
# add also 

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


# Html forms 

https://github.com/Md-Merazul-Islam/Django/blob/main/15.5%20Module%20Practice%20Day/musicians_directory/musician/templates/musician/musician_form.html
