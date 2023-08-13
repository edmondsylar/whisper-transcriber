# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtMultimedia import QAudioRecorder, QAudioEncoderSettings

# Import sounddevice and soundfile modules
import sounddevice as sd
import soundfile as sf

# Define a class for the recorder GUI
class Recorder(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the audio recorder
        self.recorder = QAudioRecorder()

        # Set the audio encoder settings
        self.settings = QAudioEncoderSettings()
        self.settings.setCodec("audio/ogg")
        self.settings.setQuality(QAudioEncoderSettings.HighQuality)

        # Set the output file name
        self.output = "recording.ogg"

        # Create a button to start recording
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start)

        # Create a button to stop recording
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setEnabled(False)

        # Create a label to show the status
        self.status_label = QLabel("Ready", self)

        # Set the layout of the widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.status_label)
        self.setLayout(self.layout)

    def start(self):
        # Start recording with the given settings and output file
        self.recorder.setEncodingSettings(self.settings)
        self.recorder.setOutputLocation(QUrl.fromLocalFile(self.output))
        self.recorder.record()

        # Enable stop button and disable start button
        self.stop_button.setEnabled(True)
        self.start_button.setEnabled(False)

        # Update the status label
        self.status_label.setText("Recording...")

    def stop(self):
        # Stop recording
        self.recorder.stop()

        # Enable start button and disable stop button
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

        # Update the status label
        self.status_label.setText("Saved to " + self.output)

# Create an application instance
app = QApplication([])

# Create and show the recorder widget
recorder = Recorder()
recorder.show()

# Run the application loop
app.exec_()
