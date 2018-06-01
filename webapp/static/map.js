var attribution = new ol.control.Attribution({
        collapsible: false
});

var map = new ol.Map({
	controls: ol.control.defaults({attribution: false}).extend([attribution]),
	layers: [
		new ol.layer.Tile({
			source: new ol.source.OSM()
		})
	],
	target: 'map',
	view: new ol.View({
		center: [0, 0],
		zoom: 2
	}),
});

function checkSize() {
	var small = map.getSize()[0] < 600;
	attribution.setCollasible(small);
	attribution.setCollapsed(small);
}

window.addEventListener("resize", checkSize);
checkSize();
