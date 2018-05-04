import qgis.core

# fromPoint() was renamed to fromPointXY() in QGis3
qgis.core.QgsGeometry.fromPointXY = qgis.core.QgsGeometry.fromPoint
