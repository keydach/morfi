{%- import '%s/%s' % (path, 'main.tpl') as main -%}
<div class="panel panel-default">
	<div class="panel-heading"><h3 class="panel-title">{{ ctrl.title|e if ctrl.title else '' }}</h3></div>
	<div class="panel-body">
		{{ main.children (ctrl, path) }}
	</div>
</div>