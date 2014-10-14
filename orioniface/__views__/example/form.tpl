{% import 'forms/main.tpl' as forms %}

{% extends 'base.tpl' %}

{% block title %} Это типа заголовок, что ли {% endblock title %}

{% block content %}
	<div class="col-md-12" id="main-container">
		{{ forms.build (form) if form else msg }}
	</div>
{% endblock content %}
