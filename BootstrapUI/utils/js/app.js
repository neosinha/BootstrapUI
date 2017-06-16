ui = new Bootstrap();

var usermodel = {
		 'authenticated' : false, 
		 'accountid' :  null, 
		 'username' : null, 
		 'auuthepoch' : 0
 }; 
 
var gpiolist = [ {'pin' : 4, 'type': 'inout'},
				 {'pin' : 5, 'type': 'inout'},
				 {'pin' : 12, 'type': 'inout'},
				 {'pin' : 13, 'type': 'inout'},
				 {'pin' : 15, 'type': 'out'}
				];

var sensortype = ['Relay', 'DHT22'] ;

 var devicemodel = {
		 'serial' : null, 
		 'mac' : null, 
		 'relays' : {'count' : 0, 'voltage' : 240, 'current' : 10 },
		 'dht': 0, 
		 'photo' : 0, 
		 'power' : 0, 
		 'current': 0, 
		 'partnumber' : null 
		 
 }; 
 



function appInit() {
	appNavBar();
	loginView();
}



function loadView2() {
	ui.clearViewById('view1');
	relayconf= deviceConfigView();
	
	h = ui.h3('', 'This is content 1');
	paneldef = new Array(); 
	paneldef.push({ 'type' : 'primary', 'content' : relayconf, 'heading' : 'Relay Configuration'});
	
	panels = ui.createPanels('configpanel', paneldef);
	
	ui.addSubViewById('view1', [panels]); 
	
}





function getChipId() {
	chipx = { 'chipid' : '1B2A29',
			  'mac' : '292A1BA620A0' }; 

	return chipx; 
}



function showView(elems) {
	ui.clearView();
	mainel = document.getElementById('mcontent');
	for (i=0; i < elems.length; i++) {
		el = elems[i];
		mainel.appendChild(el);
	}
}



function authenticate() {
	user = document.getElementById('usernamex').value;
	pass = document.getElementById('passwordx').value;

	cond = false; 
	upass = false; 
	ppass = false; 
	if (user.length > 0) {
		upass = true; 
	} 	
	if (pass.length>0) {
		ppass = true; 
	} 
	
	//alert('Authenticating...');
	
	if (upass & ppass) {
		params = 'accountid='+user.trim()+'&password='+pass.trim(); 
		params = params + '&service=smartdomus'; 
		url = "https://api.sinhallc.com/webservices/authaccount?"; 
		urlx = url + params; 
		$.get(urlx,
			function(data, status){
			authresp = JSON.parse(data);
			dt = new Date(); 
			console.log('Auth: '+ JSON.stringify(authresp));
			if (authresp['auth']) {
				usermodel['authenticated'] = true; 
				usermodel['username'] = user.trim();
				usermodel['accountid'] = authresp['id'];
				usermodel['authepoch'] = dt.getTime(); 
				alert('Loading next page...');
				loadView2();
			} else {
				if (authresp['id']) {
					x = ui.createNotification('danger', 
					'Password is incorrect');
					el = document.getElementById('notify');
					el.appendChild(x);
				} else {
					x = ui.createNotification('danger', 
					'Username does not exist. Please create a new account.');
					el = document.getElementById('notify');
					el.appendChild(x);
				}
			}
        });
		
	} else {
		//alert('Password or Username blank');
		x = ui.createNotification('danger', 
				'Password or Username is blank');
		
		el = document.getElementById('notify');
		el.appendChild(x);
	}
}
