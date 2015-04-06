<div class="form-group">
	<div>
	<label for="{{ ctrl.name|e }}">{{ required_mark (ctrl) }}{{ ctrl.title|e }}</label>
	</div>
	<select id="{{ ctrl.name|e }}" name="{{ ctrl.name|e }}">
		{%- for code, text in ctrl.items %}
			<option value="{{ code|e }}" {% if code == ctrl.value %}selected{% endif %}>{{ text|e }}</option>
		{%- endfor %}
	</select>
	{{ errors (ctrl) }}
</div>
