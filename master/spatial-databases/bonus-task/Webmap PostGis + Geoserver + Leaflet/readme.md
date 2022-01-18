Webmap developed using GeoServer, Leaflet, PostGIS and PostgreSQL. 
GeoServer and PostgreSQL were running on localhost port 8080. Layers taken from database, which were uploaded using PostGIS.

Features: Dynamic filters for residences and lakes by their names (filter items change when object properties change), CRUD
	* C – create objects (postboxes) by clicking somewhere on the map, with WFS insert transactions
	* R - read data from database
	* U - update objects with WFS update transactions
	* D - delete objects with WFS delete transactions