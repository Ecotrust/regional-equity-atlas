app_settings = {};

googleSatellite = new OpenLayers.Layer.Google("Satellite", {
    type: google.maps.MapTypeId.SATELLITE,
    sphericalMercator: true,
    isBaseLayer: true,
    numZoomLevels: 20,
    maxZoomLevel: 19,
    visibility: false,
    textColor: "white"
});

openStreetMap = new OpenLayers.Layer.OSM(
    "Open Street Map",
    [
      "http://a.tile.openstreetmap.org/${z}/${x}/${y}.png",
      "http://b.tile.openstreetmap.org/${z}/${x}/${y}.png",
      "http://c.tile.openstreetmap.org/${z}/${x}/${y}.png"
    ],
    {
        sphericalMercator: true,
        isBaseLayer: true,
        textColor: "black",
        numZoomLevels: 20,
        minZoomLevel: 0,
        maxZoomLevel: 19
    });

mapboxKey = 'pk.eyJ1IjoicmVhc3VwcG9ydCIsImEiOiJjampyZXRvMHowdnJxM3FtYTIwa2c1cWhoIn0.RUZePEKa27PImp399s2B4w';
MapBoxHybrid = new OpenLayers.Layer.XYZ(
  "Hybrid",
  [
    "http://a.tiles.mapbox.com/v4/mapbox.streets-satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey,
    "http://b.tiles.mapbox.com/v4/mapbox.streets-satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey,
    "http://c.tiles.mapbox.com/v4/mapbox.streets-satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey,
    "http://d.tiles.mapbox.com/v4/mapbox.streets-satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey
  ], {
      attribution: "<div style='background-color:#CCC; padding: 3px 8px; margin-bottom: 2px;'>Tiles &copy; <a href='http://mapbox.com/'>MapBox</a></div>",
      sphericalMercator: true,
      wrapDateLine: true,
      textColor: "white",
      numZoomLevels: 20,
      maxZoomLevel: 19
  });

MapBoxSat = new OpenLayers.Layer.XYZ(
  "Satellite",
  [
    "http://a.tiles.mapbox.com/v4/mapbox.satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey,
    "http://b.tiles.mapbox.com/v4/mapbox.satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey,
    "http://c.tiles.mapbox.com/v4/mapbox.satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey,
    "http://d.tiles.mapbox.com/v4/mapbox.satellite/${z}/${x}/${y}@2x.png?access_token=" + mapboxKey
  ], {
      attribution: "<div style='background-color:#CCC; padding: 3px 8px; margin-bottom: 2px;'>Tiles &copy; <a href='http://mapbox.com/'>MapBox</a></div>",
      sphericalMercator: true,
      wrapDateLine: true,
      textColor: "white",
      numZoomLevels: 20,
      maxZoomLevel: 19
  });

ESRITopo = new OpenLayers.Layer.XYZ(
  "Terrain",
  "http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/${z}/${y}/${x}",
  {
      sphericalMercator: true,
      textColor: "black",
      numZoomLevels: 20,
      maxZoomLevel: 19,
      wrapDateLine: true,
      attribution: "<div style='background-color:#CCC; padding: 3px 8px; margin-bottom: 2px;'>Basemap by ESRI, USGS</div>"
  }
);

app_settings.baselayers = [MapBoxHybrid, ESRITopo, openStreetMap, googleSatellite]

app_settings.minzoom = 10;
app_settings.maxzoom = 20;
