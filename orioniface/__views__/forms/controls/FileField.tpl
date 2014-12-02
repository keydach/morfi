{%- import '%s/%s' % (path, 'main.tpl') as main -%}
<div class="form-group">
	<input 
  		type="file"
  		{% if ctrl.name %}name="{{ ctrl.name }}"{% endif %}
  	/>
	{{ main.errors (ctrl) }}
</div>
