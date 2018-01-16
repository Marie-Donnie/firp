function init() {

    L.CursorHandler = L.Handler.extend({

	addHooks: function () {
            this._popup = new L.Popup();
            this._map.on('click', this._open, this);
	},

	removeHooks: function () {
            this._map.off('click', this._open, this);
	},

	_open: function (e) {
	    this._popup.setLatLng(e.latlng)
		.setContent(`x, y (${e.latlng.lng},${e.latlng.lat})`);
            this._popup.openOn(this._map);
	},

    });

    L.Map.addInitHook('addHandler', 'cursor', L.CursorHandler);


    var map = L.map('map', {
	crs: L.CRS.Simple,
	minZoom: 0,
	cursor: true,
    });

    var bounds = [[0,0], [1000,1000]];
    var image = L.imageOverlay('/fiches/media/images/maps/noirebois.PNG', bounds).addTo(map);

    map.fitBounds(bounds);

    var yx = L.latLng;

    var xy = function(x, y) {
	if (L.Util.isArray(x)) {    // When doing xy([x, y]);
            return yx(x[1], x[0]);
	}
	return yx(y, x);  // When doing xy(x, y);
    };

    var quete_libre = L.icon({
	iconUrl: '/fiches/media/images/site/map/quest.PNG',
	iconSize: [16, 31]
    });

    var quete_reservee = L.icon({
	iconUrl: '/fiches/media/images/site/map/quest_taken.PNG',
	iconSize: [16, 31]
    });

    $.ajax( "quetes_json" )
	.done(function(data) {
	    var json = JSON.parse(data);
	    json.forEach(function(quete) {
		var url = `<a href="/firp/quetes/${quete.pk}">${quete.fields.nom}</a>`;
		var icon = quete.fields.etat===1 ? quete_libre : quete_reservee;
		L.marker( xy(quete.fields.x, quete.fields.y), {icon: icon})
		    .addTo(map)
		    .bindPopup( L.popup().setContent(url));
	    });
	});

}

$(init)
