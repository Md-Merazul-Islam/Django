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

    {% extends "base.html" %}

    {% block content %}
    {% load crispy_forms_tags %}
    <h1 class='text-center'> Add profile page  page</h1>

    <div style="width: 50%; margin: auto;">
    <form action="" method="POST">
        {% csrf_token %}
        {{ form | crispy }}
        <button class="btn btn-warning">Submit</button>
    </form>
    </div>
    {% endblock %}


# static file : 

    import os
    
    "crispy_forms",
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]

    ...
    

