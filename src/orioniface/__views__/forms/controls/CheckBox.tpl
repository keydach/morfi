{% extends 'forms/element.tpl' %}
{%- block begin %}
	{{- super () }}
	<td class="form-caption">
		<label for="{{ el.name }}">{{ isRequired (el) }}{{ el.caption }}</label>
	</td>
	<td>
		<input type="checkbox" name="{{ el.name }}" {% if el.value %}checked{% endif %} />
		{{ errors (el) }}
	</td>
{%- endblock %}