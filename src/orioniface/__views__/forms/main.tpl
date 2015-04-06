{%- macro children (ctrl, path) -%}
	{%- for child in ctrl.fields () %}
		{{ build (child) }}
	{% endfor -%}
{%- endmacro -%}

{%- macro errors (ctrl) -%}
	{%- if ctrl.errors -%}
		<div style="margin-left: 40px; margin-top: 8px;">
		{%- for message in ctrl.errors %}
			<span class="label label-danger">{{ message }}</span>
		{% endfor -%}
		</div>
	{%- endif %}
{%- endmacro %}

{%- macro required_mark (ctrl) -%}
{%- if ctrl.is_required %}<span class="glyphicon glyphicon-asterisk" style="color: red"></span> {% endif -%}
{%- endmacro -%}

{%- macro build (ctrl, path = 'forms') %}
	{%- include '%s/controls/%s.%s' % (path, ctrl.__template__ if ctrl.__template__ else ctrl.__class__.__name__, 'tpl') -%}
{%- endmacro %}
