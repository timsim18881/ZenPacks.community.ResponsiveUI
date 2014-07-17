(function(){
	setTimeout(function () {
		var btn = document.createElement("div"),
			parent = document.getElementById("jobswidget"),
			header_height = Ext.getCmp("header_panel").height,
			sidebar_width = Ext.getCmp("master_panel").width;

		btn.id = "zen_btn";
		btn.innerText = "Zen";
		btn.className = parent.className;

		parent.appendChild(btn);

		btn.style = Ext.apply(btn.style, {
			position: "relative",
			display: "inline-block",
			left: "-34px",
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
				Ext.getCmp("master_panel").setWidth(0);
			} else {
				Ext.getCmp("header_panel").setHeight(header_height);
				Ext.getCmp("master_panel").setWidth(sidebar_width);
			}
		}
	}, 3000);
})();