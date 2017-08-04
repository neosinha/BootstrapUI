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




