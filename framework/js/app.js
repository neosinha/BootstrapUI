

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
		tabs.push({'name' : "Panel" ,'content' : loadPanels()});
		
		navtabs= ui.navtabs('tabbed', 'justified bg-basic text-warning', tabs);
		
		notifyarea = ui.createElement('div', 'notify');
		
		jum.appendChild(navtabs);
		jum.appendChild(notifyarea);
		
		
		ui.addSubViewToMain([jum]);
	}

	




