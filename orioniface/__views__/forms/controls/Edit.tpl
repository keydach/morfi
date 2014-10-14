{%- import '%s/%s' % (path, 'main.tpl') as main -%}
<div class="form-group">
	<label for="{{ ctrl.name|e }}">{{ main.required_mark (ctrl) }}{{ ctrl.title|e }}</label>
	<input 
  		type="text"
  		class="form-control"
  		name="{{ ctrl.name|e }}"
  		value="{{ ctrl.value|e if ctrl.value else '' }}"
  		{{ 'maxlength=%d' % ctrl.maxlength if ctrl.maxlength else '' }}
  	/>
	{{ main.errors (ctrl) }}
</div>
