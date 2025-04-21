import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QTextEdit,
    QProgressBar,
    QGroupBox,
    QFormLayout,
)
import qdarkstyle


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Complex PyQt5 DarkStyle Example")
        self.setGeometry(100, 100, 600, 400)

        # 创建控件
        self.label = QLabel("Enter some text:", self)
        self.textbox = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.result_label = QLabel("", self)

        # 下拉框选择主题
        self.theme_combo = QComboBox(self)
        self.theme_combo.addItem("Dark Mode")
        self.theme_combo.addItem("Light Mode")
        self.theme_combo.currentIndexChanged.connect(self.change_theme)

        # 复选框
        self.checkbox = QCheckBox("Enable Feature", self)

        # 单选框
        self.radio_button1 = QRadioButton("Option 1", self)
        self.radio_button2 = QRadioButton("Option 2", self)

        # 多行文本框
        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText("Enter additional information here...")

        # 进度条
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(50)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.theme_combo)
        layout.addWidget(self.checkbox)

        # 单选框放入一个组
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.radio_button1)
        radio_layout.addWidget(self.radio_button2)
        radio_group_box = QGroupBox("Choose an option:", self)
        radio_group_box.setLayout(radio_layout)

        layout.addWidget(radio_group_box)
        layout.addWidget(self.text_area)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        # 按钮点击事件
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        # 获取文本框输入并显示在结果标签上
        user_input = self.textbox.text()
        self.result_label.setText(f"You entered: {user_input}")

    def change_theme(self):
        # 切换主题
        if self.theme_combo.currentIndex() == 0:
            self.setStyleSheet(qdarkstyle.load_stylesheet())
        else:
            self.setStyleSheet("")


# 启动应用
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 默认加载深色主题
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
