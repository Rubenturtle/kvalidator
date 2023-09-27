from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsRasterLayer
from qgis.utils import iface

def validate_raster():
    # Get the active layer
    layer = iface.activeLayer()

    # Check if it's a raster layer
    if isinstance(layer, QgsRasterLayer):
        # Check the raster format (e.g., TIFF, JPEG, PNG)
        format = layer.providerType()
        if format:
            QMessageBox.information(None, "Raster Validation", f"Raster format: {format}")
        else:
            QMessageBox.warning(None, "Raster Validation", "Invalid raster format.")
    else:
        QMessageBox.warning(None, "Raster Validation", "Select a raster layer to validate.")

# Create a QAction to trigger the validation
action = QAction("Validate Raster", iface.mainWindow())
action.triggered.connect(validate_raster)

# Add the QAction to the Plugins menu
iface.addPluginToMenu("Validate Raster", action)