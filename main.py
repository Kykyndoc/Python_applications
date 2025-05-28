import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFileDialog, QLabel, QSlider
)

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, Qt, QTime

class AudioPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Аудиоплеер с плейлистом (PyQt6)")
        self.setGeometry(300, 300, 600, 400)

        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)

        self.add_button = QPushButton("Открыть песню")
        self.play_button = QPushButton("Воспроизвести")
        self.pause_button = QPushButton("Пауза")
        self.status_label = QLabel("Файл не загружен")

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50) #Начальная громкость
        self.audio_output.setVolume(0.5)

        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 0)

        self.time_label = QLabel("00:00 / 00:00")

        self.play_button.setEnabled(False)
        self.pause_button.setEnabled(False)


        layout = QVBoxLayout()
        layout.addWidget(self.add_button)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.play_button)
        btn_layout.addWidget(self.pause_button)
        layout.addWidget(self.status_label)
        layout.addLayout(btn_layout)

        layout.addWidget(QLabel("Громкость:"))
        layout.addWidget(self.volume_slider)

        layout.addWidget(self.position_slider)
        layout.addWidget(self.time_label)
        
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_files)
        self.play_button.clicked.connect(self.play_audio)
        self.pause_button.clicked.connect(self.pause_audio)
        self.volume_slider.valueChanged.connect(self.change_volume)

        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)
        self.position_slider.sliderMoved.connect(self.set_position)

    def add_files(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Открыть аудиофайл", "", "Аудиофайлы (*.mp3 *.wav *.oog)"
        )
        if filename:
            url = QUrl.fromLocalFile(filename)
            self.media_player.setSource(url)
            self.status_label.setText(f"Файл: {filename}")
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(True)

    def play_audio(self):
        if self.media_player.source().isEmpty():
            self.load_track(self.current_index)
        self.media_player.play()
        self.status_label.setText("Воспроизведение...")

    def pause_audio(self):
        self.media_player.pause()
        self.status_label.setText("Пауза")

    def change_volume(self, value):
        self.audio_output.setVolume(value / 100)

    def update_position(self, position):
        self.position_slider.setValue(position)
        self.update_time_label(position, self.media_player.duration())

    def update_duration(self, duration):
        self.position_slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_time_label(self, current_ms, total_ms):
        def ms_to_time(ms):
            t = QTime(0, 0, 0)
            t = t.addMSecs(ms)
            return t.toString("mm:ss")

        self.time_label.setText(f"{ms_to_time(current_ms)} / {ms_to_time(total_ms)}")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec())