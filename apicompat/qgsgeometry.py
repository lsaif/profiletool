import qgis.core

# fromPoint() was renamed to fromPointXY() in QGis3
# The same with the other QgsGeometries -- from [geometry] in QGIS 2 to [geometry]XY in QGIS 3
qgis.core.QgsGeometry.fromPointXY = qgis.core.QgsGeometry.fromPoint
qgis.core.QgsGeometry.fromPolylineXY = qgis.core.QgsGeometry.fromPolyline
qgis.core.QgsGeometry.fromMultiPolylineXY = qgis.core.QgsGeometry.fromMultiPolyline
