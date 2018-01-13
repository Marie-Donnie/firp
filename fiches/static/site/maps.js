function init() {
    var map = L.map('map', {
	crs: L.CRS.Simple,
	minZoom: -1
    });

    var bounds = [[0,0], [1000,1000]];
    var image = L.imageOverlay('/fiches/media/images/maps/noirebois.PNG', bounds).addTo(map);

    map.fitBounds(bounds);
}

$(init)
