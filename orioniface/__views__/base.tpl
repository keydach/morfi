<!DOCTYPE html>
<html lang="ru">

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="generator" content="CherryPy 3.2, cherrybase, Jinja 2, RFID-WMS 0.0.4a">
	<!--  link rel="shortcut icon" href="../../assets/ico/favicon.png" -->
	
	<title>{% block title %}Это ТАЙТЛ по дефолту{% endblock %}</title>
	
	<link href="/static/font/roboto.css" rel="stylesheet">
	
	<!-- Bootstrap core CSS -->
	<link href="/static/bs/css/bootstrap.css" rel="stylesheet">
	
	<!-- Custom styles for this template -->
	{% block head %}
	{% endblock %}
	
	<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
	<!--[if lt IE 9]>
		<script src="/static/bs/assets/html5shiv.js"></script>
		<script src="/static/bs/assets/respond.min.js"></script>
	<![endif]-->
</head>

<body data-spy="scroll" data-target="#sidebar">

    <div class="container">
	    <div class="row">
	    	{% block content %}
		    {% endblock %}
	    </div>
    </div>	

	<!-- Bootstrap core JavaScript
	================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="/static/bs/assets/jquery.js"></script>
	<script src="/static/bs/js/bootstrap.min.js"></script>

	{% block scripts %}{% endblock	%}
</body>

</html>