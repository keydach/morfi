{% extends 'forms/element.tpl' %}
{%- block begin %}
	{{- super () }}
	<td class="form-line" colspan="2">
		<label for="{{ el.name }}">{{ isRequired (el) }}{{ el.caption }}</label><br />
		<textarea
			class="input-text"
			rows="8"
			id="{{ el.name }}"
			name="{{ el.name }}"
			{% if el.maxLength > 0 %}maxlength="{{ el.maxLength }}"{% endif %}
		>{{ el.value }}</textarea>
		{{ errors (el) }}
	</td>
{%- endblock %}
