(function(){
	var t = setInterval(function () {
		var btn = document.createElement("div"),
			parent = document.getElementById("jobswidget"),
			header_height = 0,
			sidebar_width = 0;

		if (!Ext.getCmp("header_panel")) return;

		clearInterval(t);

		header_height = Ext.getCmp("header_panel").height;

		if (Ext.getCmp("master_panel"))
			sidebar_width = Ext.getCmp("master_panel").width;

		btn.id = "zen_btn";
		btn.innerText = "Zen mode";
		btn.className = parent.className;

		parent.appendChild(btn);

		btn.style = Ext.apply(btn.style, {
			position: "relative",
			display: "inline-block",
			left: "-64px",
			top: "-1px",
			fontSize: "12px",
			fontWeight: "bold",
			height: "24px",
			paddingTop: "4px"
		});

		btn.onclick = function (e) {
			e.stopPropagation();

			if (Ext.getCmp("header_panel").height > 0) {
				Ext.getCmp("header_panel").setHeight(0);
				if (Ext.getCmp("master_panel"))
					Ext.getCmp("master_panel").setWidth(0);
				document.cookie = "zen_mode=1;path=/";
			} else {
				Ext.getCmp("header_panel").setHeight(header_height);
				if (Ext.getCmp("master_panel"))
					Ext.getCmp("master_panel").setWidth(sidebar_width);
				document.cookie = "zen_mode=;path=/";
			}
		};

		if (document.cookie.indexOf("zen_mode=1") != -1 ) {
			Ext.getCmp("header_panel").setHeight(0);
			if (Ext.getCmp("master_panel"))
				Ext.getCmp("master_panel").setWidth(0);
		}
	}, 50);
})();


Ext.onReady(function() {

    var s = Zenoss.settings;

    if (s.header_bg) {
    	document.getElementById("primarynav").style.backgroundColor = s.header_bg;
    	document.getElementsByClassName("bg-logo")[0].style.backgroundColor = s.header_bg;
    	// Hide left cap, because it overlaps on submenu too
    	document.getElementsByClassName("bg-leftcap")[0].style.paddingLeft = "0";
    }

	if (s.header_sub_bg) {
		document.getElementById("secondarynav").style.backgroundColor = s.header_sub_bg;
		document.getElementsByClassName("bg-leftcap")[0].style.paddingLeft = "0";
	}

	if (s.sidebar_bg) {
		var style = document.createElement("style");
		style.innerText = ""
			+ "#master_panel .x-panel-body-hierarchy {background-color: " + s.sidebar_bg + " !important;}"
			+ "#master_panel .x-toolbar-default {background: " + s.sidebar_bg + " !important;}"
			+ ".x-zenoss-master-panel .x-panel-body {background: " + s.sidebar_bg + " !important;}"
			+ "#master_panel #subselecttreepaneldetail_nav .x-grid-cell {background: " + s.sidebar_bg + " !important;}"
		document.getElementsByTagName("head")[0].appendChild(style);
	}

	if (s.main_bg) {
		var style = document.createElement("style");
		style.innerText = ""
			+ ".x-grid-row .x-grid-cell {background-color: " + s.main_bg + " !important;}"
			//+ ".x-grid-view {background-color: " + s.main_bg_alt + " !important;}"
		document.getElementsByTagName("head")[0].appendChild(style);
	}

	if (s.main_bg_alt) {
		var style = document.createElement("style");
		style.innerText = ""
			+ ".x-grid-row-alt .x-grid-cell {background-color: " + s.main_bg_alt + " !important;}"
		document.getElementsByTagName("head")[0].appendChild(style);
	}

});