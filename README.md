# Bootstrap UI
Generating Dynamic HTML UI with Bootstrap framework. 

Have you been in a situation in which you need to build a UI or MVC but are dragged into learning some big framework or some new technology completely? I have found myself juggling between iOS/Java/HTML/Angular and different types of HTML frameworks. There are a lot of frameworks which produce responsive web-pages and are mobile ready. However, only a few come close to Bootstrap. This framework is really simple, very complete and very well supported. 
However, as an app developer, I find myself struggling to keep up with layout and alignment changes. I just found it very difficult to keep writing regular HTML or just remembering the bootstrap classes or structure. Almost all framework suffer from the "class" blow-up problem, making you keep the documentation page open always. 

BootstrapUI Framework,
1. brings the power of DOM manipulations to Javascript/TypeScript to very fast UI implementations. 
2. does not ask you to write HTML which is then processed through CSS or Javascript. 
3. It sits on top of Bootstrap Framework. 

Example: The main app would like,  
```html
<head>
<!--  BootstrapUI JS     -->
    <script src="https://api.sinhallc.com/uifiles/utils/js/bootstrapui.js"></script>
    <!--  Application Logic -->
    <script src="js/app.js"></script>
    <!--  All stacked views are defined in this file     -->
    <script src="js/views.app.js"></script>
</head>
<body id = "mainbody">
 	<!--  Placeholder tags -->
	<div class="container" id="mcontent"></div>
	<div id="appmodal" class="modal fade" role="dialog"></div>
  
 	<!--  Fire off JS function upon load -->
	<script>
		appInit();
	</script>
</body>

```

Now, app.js would like 
```javascript

function appInit() {
	appNavBar();
	loadLandingView(); 
}


function loadLandingView() {
		var h1x = ui.h3(null, 'Example UI', null);
		jum = ui.jumbotron('view1', h1x,' bg-basic'); 
		
		
		//create tab area
		tabs = new Array();
		tabs.push({'name' : "Login" , 'content' : loginForm()});
		tabs.push({'name' : "Register" ,'content' : registerForm()});
		navtabs= ui.navtabs('tabbed', 'justified bg-basic text-warning', tabs);
		
		notifyarea = ui.createElement('div', 'notify');
		
		jum.appendChild(navtabs);
		jum.appendChild(notifyarea);
		
		
		ui.addSubViewToMain([jum]);
	}

```

Finally, the views used are built as follows, 
```javascript
// file holds the code which designs the UI views
// or bigger/composite UI view elements
ui = new Bootstrap();

function appNavBar() {
	navbar = ui.navbar("navarea", 'App Company');
	ui.addSubViewToMain([navbar]);
}

function registerForm() {
	
	inpx = new Array();
	inpx.push({'label' : "User Name", 
			'type' : "text", 
			'name' : 'rusername',
			'id'   : 'rusername',
			'placeholder': "User Name"});
	
	inpx.push({'label' : "Password", 
		'type' : "password", 
		'name' : 'rpasswordx',
		'id'   : 'rpasswordx',
		'placeholder': "Password"}); 
	
	inpx.push({'label' : "Confirm Password", 
		'type' : "password", 
		'name' : 'cpasswordx',
		'id'   : 'cpasswordx',
		'placeholder': "Confirm Password"}); 
	
	inpx.push({'label' : null, 
		'type' : "submit", 
		'name' : 'Register',
		'value': 'Register', 
		'class': 'btn-info', 
		'onclick': 'register();', //call a function to perform registeration
		'placeholder': "Register"});
		
	form1 = ui.createForm('registerform', inpx);
	
	return form1
}




function loginForm() {

	inpx = new Array();
	inpx.push({'label' : "User Name", 
			'type' : "text", 
			'id'	: 'usernamex',
			'name' : 'usernamex',
			'placeholder': "User Name"});
	
	inpx.push({'label' : "Password", 
		'type' : "password", 
		'name' : 'passwordx',
		'id' : 'passwordx',
		'placeholder': "Password"}); 
	
	inpx.push({'label' : null, 
		'type' : "submit", 
		'name' : 'Login',
		'value': 'Login', 
		'class': 'btn-info',
		'onclick' : 'authenticate();',
		'placeholder': "Login"});
		
	form1 = ui.createForm('loginform', inpx);
	
	return form1; 
}



function loginView() {
	var h1x = ui.h3(null, '', null);
	jum = ui.jumbotron('view1', h1x);
	
	
	tabs = new Array();
	tabs.push({'name' : "Login" , 'content' : designLoginForm()});
	tabs.push({'name' : "Register" , 'content' : registerForm()});
	navtabs= ui.navtabs('tabbed', 'justified', tabs);
	
	notifyarea = ui.createElement('div', 'notify');
	
	jum.appendChild(navtabs);
	jum.appendChild(notifyarea);
	
	
	//loginview = ui.addSubView(jum, navtabs);
	
	//showView([navbar, jum]);
	//view = ui.addSubViewById('mcontent', [loginview]);
	ui.addSubViewToMain([jum]);
}

```




