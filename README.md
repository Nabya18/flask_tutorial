Purpose: For make API Server

Flask is a straightforward, speedy, scalable library, used for building, compact web applications. It is a micro framework, that presents developers, useful tools, and, features, for coding REST APIs, and backend data processing, of web apps.

Notes:
1. A redirect is used in the Flask class to send the user to a particular URL with the status code.
2. The url_for() method, is used to prepare a URL, for a function dynamically, such that, changing URLs, in the application, is avoided.
3. render_template() is a function within the Flask web framework used to render HTML templates for display in a web browser.
    - You have to make templates directory
4. Bootstrap inheritance in Flask applications refers to the combination of Jinja2 template inheritance with the styling and components provided by the Bootstrap framework.
5. Send information
---
{% block content %}
information
{% endblock %}
---
6. request.form["nm"] based on login.html
7. A session is used to store information related to a user, across different requests, as they interact with a web app.
8. To avoid error in message Flashing we need make app.secret_key.
   - SECRET_KEY is used in almost all extensions where there is something security related and IIRC you can't start an app in debug mode without it.
9. session.pop to remove data from browser.
10. If session.permanent is true, the cookie’s expiration will be set this number of seconds in the future. Can either be a datetime.timedelta or an int.