{% extends 'forms/element.tpl' %}
{%- block begin %}
	{{- super () }}
<tr class = "form-line">
	<td class = "form-caption">
		<label for="{{ el.name }}">{{ isRequired (el) }}{{ el.caption }}</label>
	</td>
	<td id = "{{ el.name }}">
		<input class = "input-text"
			type = "text"
			id = "{{ el.name }}id"
			name = "{{ el.name }}"
			{% if el.value %} value = "{{ el.displayValue }}"{% endif %}
			{% if el.disabled %} disabled{% endif %}
		/>
		<script type="text/javascript">
			$(document).ready (function ()
			{
				$('#{{ el.name }}id').datetimepicker (
					{
						{%- if el.disabled %}disabled: true,{%- endif %}
						showSecond: true,
						dateFormat: '{{ el.jqueryDateFormat }}',
						timeFormat: 'hh:mm:ss'
					}
				);
			});
		</script>
		{{ errors (el) }}
	</td>
</tr>
{%- endblock %}