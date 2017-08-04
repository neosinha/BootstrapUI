// file holds the code which designs the UI views
// or bigger/composite UI view elements


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
		'onclick': 'register();', 
		'placeholder': "Register"});
		
	form1 = ui.createForm('registerform', inpx);
	
	return form1
}




function designLoginForm() {

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

function appNavBar() {
	navbar = ui.navbar("navarea", 'SDOMUS');
	ui.addSubViewToMain([navbar]);
}


function relayConfigView() {
	
	inpx = new Array();
	inpx.push({'label' : "Relay 10A", 
			'type' : "checkbox", 
			'id'	: 'relay1',
			'name' : 'usernamex',
			'placeholder': "Device"});
		
	inpx.push({'label' : "Relay 20A", 
		'type' : "checkbox", 
		'id'	: 'usernamex',
		'name' : 'usernamex',
		'placeholder': "Device"});
	
	form1 = ui.createForm('dconfigview', inpx);
	
	return form1; 
}


