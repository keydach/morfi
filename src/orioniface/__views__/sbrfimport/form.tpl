{% import 'forms/main.tpl' as forms %}
{% if form %}
	<div class="col-md-12" id="main-container">
		{{ forms.build (form) }}
	</div>
{% endif %}
{% if msg %}{{ msg }}{% endif %}
