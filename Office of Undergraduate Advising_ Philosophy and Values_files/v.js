// Pop-Up Window plugin
// Rob Knight's "Who's your uncle" plugin
// Zebra Table Striping via http://15daysofjquery.com/examples/zebra/
	$(document).ready(function(){
			$('a.nwin').click( function() { window.open(this.href,'','resizable=no,location=no,menubar=no,scrollbars=no,status=no,toolbar=no,fullscreen=no,dependent=no,status'); return false; } ) 
			if($.browser.msie == false) { $( function() { $('#nav_primary ul li ul li ul li.menuparent.active-1 a').addClass('active'); } ); }
			$(".aTableDir tr").mouseover(function() {$(this).addClass("over");}).mouseout(function() {$(this).removeClass("over");});
			$(".aTableDir tr:even").addClass("alt");
		});

// that form select thing that Tracy put in
	function MM_jumpMenu(targ,selObj,restore){ //v3.0
	  eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
	  if (restore) selObj.selectedIndex=0;
	}
	function MM_findObj(n, d) { //v4.01
	  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
	    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
	  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
	  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
	  if(!x && d.getElementById) x=d.getElementById(n); return x;
	}
	function MM_jumpMenuGo(selName,targ,restore){ //v3.0
	  var selObj = MM_findObj(selName); if (selObj) MM_jumpMenu(targ,selObj,restore);
	}


// cbb function by Roger Johansson, http://456bereastreet.com
	var cbb = {
		init : function() {
		// Check that the browser supports the DOM methods used
			if (!document.getElementById || !document.createElement || !document.appendChild) return false;
			var oElement, oOuter, oI1, oI2, tempId;
		// Find all elements with a class name of cbb
			var arrElements = document.getElementsByTagName('*');
			var oRegExp = new RegExp("(block-block)|(block-sidecontent)|(block-views)");
			for (var i=0; i<arrElements.length; i++) {
		// Save the original outer element for later
				oElement = arrElements[i];
				if (oRegExp.test(oElement.className)) {
		// 	Create a new element and give it the original element's class name(s) while replacing 'cbb' with 'cb'
					oOuter = document.createElement('div');
					oOuter.className = oElement.className.replace(oRegExp, '$1cb$2');
		// Give the new div the original element's id if it has one
					if (oElement.getAttribute("id")) {
						tempId = oElement.id;
						oElement.removeAttribute('id');
						oOuter.setAttribute('id', '');
						oOuter.id = tempId;
					}
		// Change the original element's class name and replace it with the new div
					oElement.className = 'i3';
					oElement.parentNode.replaceChild(oOuter, oElement);
		// Create two new div elements and insert them into the outermost div
					oI1 = document.createElement('div');
					oI1.className = 'i1';
					oOuter.appendChild(oI1);
					oI2 = document.createElement('div');
					oI2.className = 'i2';
					oI1.appendChild(oI2);
		// Insert the original element
					oI2.appendChild(oElement);
		// Insert the top and bottom divs
					cbb.insertTop(oOuter);
					cbb.insertBottom(oOuter);
				}
			}
		},
		insertTop : function(obj) {
			var oOuter, oInner;
		// Create the two div elements needed for the top of the box
			oOuter=document.createElement("div");
			oOuter.className="bt"; // The outer div needs a class name
		    oInner=document.createElement("div");
		    oOuter.appendChild(oInner);
			obj.insertBefore(oOuter,obj.firstChild);
		},
		insertBottom : function(obj) {
			var oOuter, oInner;
		// Create the two div elements needed for the bottom of the box
			oOuter=document.createElement("div");
			oOuter.className="bb"; // The outer div needs a class name
		    oInner=document.createElement("div");
		    oOuter.appendChild(oInner);
			obj.appendChild(oOuter);
		},
		// addEvent function from http://www.quirksmode.org/blog/archives/2005/10/_and_the_winner_1.html
		addEvent : function(obj, type, fn) {
			if (obj.addEventListener)
				obj.addEventListener(type, fn, false);
			else if (obj.attachEvent) {
				obj["e"+type+fn] = fn;
				obj[type+fn] = function() { obj["e"+type+fn]( window.event ); }
				obj.attachEvent("on"+type, obj[type+fn]);
			}
		}
	};
	cbb.addEvent(window, 'load', cbb.init);