function init() {
    var map = L.map('map', {
	crs: L.CRS.Simple,
	minZoom: 0
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
		if (quete.fields.etat !== 3) {
		    var url = `<a href="/firp/quetes/${quete.pk}">${quete.fields.nom}</a>`;
		    var icon = quete.fields.etat===1 ? quete_libre : quete_reservee;
		    L.marker( xy(quete.fields.x, quete.fields.y), {icon: icon})
			.addTo(map)
			.bindPopup( L.popup().setContent(url));
		}
	    });
	});

    // var sol = xy(245, 480.0);
    // var mizar    = xy( 41.6, 130.1);
    // var kruegerZ = xy( 0,  56.5);
    // var deneb    = xy(218.7,   8.3);

    // var popuptest = L.popup(className='lolçamarchepas')
    // 	.setContent('<a href="http://127.0.0.1:8000/quetes/2/">Une quête suicidaire</a>')
    // ;

    // L.marker(     sol, {icon: quest}).addTo(map).bindPopup(popuptest);
    // L.marker(   mizar, {icon: quest}).addTo(map).bindPopup(    'Mizar');
    // L.marker(kruegerZ, {icon: quest}).addTo(map).bindPopup('Krueger-Z');
    // L.marker(   deneb, {icon: quest}).addTo(map).bindPopup(    'Deneb');
}

$(init)
