{%- import '%s/%s' % (path, 'main.tpl') as main -%}
<div class="form-group">
	<input 
  		type="file"
  	/>
	{{ main.errors (ctrl) }}
</div>
