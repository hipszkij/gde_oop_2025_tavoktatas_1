class LightningConnector:
    """Lightning csatlakozó interfész Apple eszközökhöz."""
    def connect_lightning(self):
        pass

class AppleCharger:
    """Apple töltő, ami Lightning csatlakozót használ."""
    def charge(self, connector: LightningConnector):
        connector.connect_lightning()
        print("Apple eszköz töltődik.")

class MicroUSBConnector:
    """MicroUSB csatlakozó interfész Android eszközökhöz."""
    def connect_micro_usb(self):
        pass

class AndroidDevice(MicroUSBConnector):
    """Android készülék, ami MicroUSB csatlakozót használ."""
    def connect_micro_usb(self):
        print("MicroUSB csatlakoztatva.")

class MicroUSBToLightningAdapter(LightningConnector):
    """Adapter, ami lehetővé teszi, hogy MicroUSB eszköz Lightning-ként viselkedjen."""
    def __init__(self, android_device: AndroidDevice):
        self.android_device = android_device

    def connect_lightning(self):
        self.android_device.connect_micro_usb()
        print("Adapter átalakította a MicroUSB-t Lightninggá.")

# Használati példa
android_device = AndroidDevice()
adapter = MicroUSBToLightningAdapter(android_device)
apple_charger = AppleCharger()
apple_charger.charge(adapter)
