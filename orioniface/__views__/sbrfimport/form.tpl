{% import 'forms/main.tpl' as forms %}

{% extends 'base.tpl' %}

{% block content %}
	<div class="col-md-12" id="main-container">
		{{ forms.build (form) if form else msg }}
	</div>
{% endblock content %}
