{%- import '%s/%s' % (path, 'main.tpl') as main -%}
<form name="{{ ctrl.name }}" enctype="multipart/form-data" method="post">
	<input type="hidden" name="__submitted__" value="submitted" />
	{{ main.children (ctrl, path) }}
	<table class="form-submit">
		<td><input type="submit" class="input-submit" {% if ctrl.submit %}value="{{ ctrl.submit }}"{% endif %}/></td>
		{% if ctrl.cancel %}
			<td><input type="button" class="input-submit" value="{{ ctrl.cancel }}" onclick="javascript: location.href = '{{ ctrl.cancel_link }}';"/></td>
		{% endif %}
	</table>
</form>

