from PySide6.QtGui import QAction
from PySide6.QtWidgets import *
import sys

committeeName = ""
topic = ""
conferenceName = ""
delegatesList=[]
presentVotingList=[#same index as delegatesList
    [],#present
    []#voting
]

class committeeCreate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oratora — Create Committee")
        self.setGeometry(100, 100, 500, 400)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        self.label = QLabel("<h1>Create a new committee</h1>")
        layout.addWidget(self.label)

        self.label = QLabel("\nCommittee name*")
        layout.addWidget(self.label)
        self.committeeName = QLineEdit()
        self.committeeName.setPlaceholderText("Enter committee name (required)")
        layout.addWidget(self.committeeName)

        self.label = QLabel("\nTopic")
        layout.addWidget(self.label)
        self.topic = QLineEdit()
        self.topic.setPlaceholderText("Enter topic")
        layout.addWidget(self.topic)

        self.label = QLabel("\nConference")
        layout.addWidget(self.label)
        self.conferenceName = QLineEdit()
        self.conferenceName.setPlaceholderText("Enter conference name")
        layout.addWidget(self.conferenceName)

        submit = QPushButton("⇒ Create committee")
        submit.clicked.connect(self.submitForm)
        layout.addWidget(submit)

        layout.addStretch()
        self.initMenuBar()

    def submitForm(self):
        committeeName = self.committeeName.text()
        topic = self.topic.text()
        conferenceName = self.conferenceName.text()

        print(committeeName, topic, conferenceName)

        if committeeName.strip() == "":
            QMessageBox.warning(self, "Missing Info", "Committee name cannot be empty")
        else:
            self.dashboard = participants(committeeName, topic, conferenceName)
            self.dashboard.show()
            self.close()

    def initMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        fileMenu = menuBar.addMenu("File")

        loadAction = QAction("Load", self)
        loadAction.triggered.connect(lambda: print("Load clicked!"))
        fileMenu.addAction(loadAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)


class participants(QMainWindow):
    def __init__(self, committeeName="", topic="", conferenceName=""):
        super().__init__()
        print(committeeName, topic, conferenceName)
        self.setWindowTitle("Oratora — Dashboard")
        self.setGeometry(100, 100, 500, 400)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        self.label = QLabel(f"<h1>{committeeName}</h1>")
        layout.addWidget(self.label)
        self.label = QLabel(f"<h4>Topic: {topic}</h4>")
        layout.addWidget(self.label)
        self.label = QLabel(f"<h4>Conference: {conferenceName}</h4>")
        layout.addWidget(self.label)

        self.label = QLabel(f"\nParticipating delegates:")
        layout.addWidget(self.label)

        self.delegates = QComboBox()
        self.delegates.addItems([ #all UN nations blegh
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
            "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
            "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
            "Burkina Faso", "Burundi", "Cape Verde", "Cambodia", "Cameroon", "Canada",
            "Central African Republic", "Chad", "Chile", "China (People's Republic of China)", "Colombia", "Comoros", "Costa Rica", "Croatia", "Cuba",
            "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica",
            "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
            "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
            "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
            "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
            "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
            "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait",
            "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
            "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
            "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
            "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
            "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
            "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
            "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay",
            "Peru", "Philippines", "Poland", "Portugal", "Qatar",
            "Republic of the Congo", "Romania", "Russia",
            "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
            "Saint Vincent and the Grenadines", "Samoa", "San Marino",
            "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
            "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
            "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan",
            "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan (Republic of China)", "Tajikistan", "Tanzania",
            "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
            "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
            "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
            "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen",
            "Zambia", "Zimbabwe"
        ])
        layout.addWidget(self.delegates)
        self.label = QLabel(f"...or add custom")
        layout.addWidget(self.label)
        self.customDel = QLineEdit()
        layout.addWidget(self.customDel)

        addDelegates = QPushButton("Add Delegate")
        addDelegates.clicked.connect(self.addDelegate)
        layout.addWidget(addDelegates)

        self.delegateList = QListWidget()
        layout.addWidget(self.delegateList)

        next = QPushButton("Next...")
        next.clicked.connect(self.next)
        layout.addWidget(next)
        self.initMenuBar()
        layout.addStretch()


    def addDelegate(self):
        if self.customDel.text().strip() == "":
            delegateAdded = self.delegates.currentText().strip()
        else:
            delegateAdded = self.customDel.text().strip()
            self.customDel.clear()
        if delegateAdded.strip() not in delegatesList:
            self.delegateList.addItem(delegateAdded)
            delegatesList.append(delegateAdded)
            print(delegatesList)

    def next(self):
        if len(delegatesList) < 2:
            return
        self.presentWindow = presentationWindow()
        self.setup = attendance(self.presentWindow)
        self.setup.show()
        self.close()

    def initMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        fileMenu = menuBar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(lambda: print("Update roll call clicked!"))
        fileMenu.addAction(save)

        exitAction = QAction("Load", self)
        exitAction.triggered.connect(QApplication.quit)
        fileMenu.addAction(exitAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

class attendance(QMainWindow):
    def __init__(self, presentWindow):
        super().__init__()
        self.presentWindow = presentWindow
        self.setWindowTitle("Oratora — Roll Call")
        self.setGeometry(100, 100, 500, 400)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        verticalLayout = QVBoxLayout()
        centralWidget.setLayout(verticalLayout)

        self.rollCall = []

        for delegate in delegatesList:
            layout = QHBoxLayout()

            label = QLabel(delegate)
            present = QCheckBox("Present")
            voting = QCheckBox("Voting")
            voting.setEnabled(False)

            self.connectCheckboxes(present, voting)

            layout.addWidget(label)
            layout.addStretch()
            layout.addWidget(present)
            layout.addWidget(voting)

            verticalLayout.addLayout(layout)

            self.rollCall.append({
                "delegate": delegate,
                "present": present,
                "voting": voting,
            })

        submit = QPushButton("Update roll-call")
        submit.clicked.connect(self.submit)
        verticalLayout.addWidget(submit)
        self.initMenuBar()
        verticalLayout.addStretch()


    def connectCheckboxes(self, present, voting):
        def onStateChanged(state):
            if state:
                voting.setEnabled(True)
            else:
                voting.setEnabled(False)
        present.stateChanged.connect(onStateChanged)

    def submit(self):
        presentVotingList[0].clear()
        presentVotingList[1].clear()

        for record in self.rollCall:
            isPresent = record["present"].isChecked()
            isVoting = record["voting"].isChecked()
            presentVotingList[0].append(isPresent)
            presentVotingList[1].append(isVoting)

        self.presentWindow.updateContents()
        self.presentWindow.show()

    def initMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        fileMenu = menuBar.addMenu("File")

        saveAction = QAction("Save", self)
        saveAction.triggered.connect(lambda: print("Save clicked!"))
        fileMenu.addAction(saveAction)

        loadAction = QAction("Load", self)
        loadAction.triggered.connect(lambda: print("Load clicked!"))
        fileMenu.addAction(loadAction)

        actionMenu = menuBar.addMenu("Actions")

        createMotion = QAction("Create Motion", self)
        createMotion.triggered.connect(self.openMotionWindow)
        actionMenu.addAction(createMotion)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

    def openMotionWindow(self):
        self.motionWindow = motions(self.presentWindow)
        self.motionWindow.show()
        self.close()

class presentationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roll call")
        self.setGeometry(150, 150, 1280, 720)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.verticalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.verticalLayout)

        self.header = QLabel("<h1>Roll call</h1>")
        self.verticalLayout.addWidget(self.header)

        self.contentLayout = QVBoxLayout()
        self.verticalLayout.addLayout(self.contentLayout)

        self.verticalLayout.addStretch()
    def displayMotion(self, motionType, proposer, title=None, totalMinutes=None, totalSeconds=None,
                      speakingTime=None):
        self.clearLayout(self.contentLayout)

        motionLabel = QLabel(f"<h2>{motionType}</h2>")
        self.contentLayout.addWidget(motionLabel)

        proposerLabel = QLabel(f"Proposed by: {proposer}")
        self.contentLayout.addWidget(proposerLabel)

        if title:
            titleLabel = QLabel(f"Title: {title}")
            self.contentLayout.addWidget(titleLabel)

        if totalMinutes is not None and totalSeconds is not None:
            duration = f"{totalMinutes} min {totalSeconds} sec"
            timeLabel = QLabel(f"Total time: {duration}")
            self.contentLayout.addWidget(timeLabel)

        if speakingTime is not None:
            speakingLabel = QLabel(f"Speaking time: {speakingTime} sec")
            self.contentLayout.addWidget(speakingLabel)

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout():
                self.clearLayout(item.layout())
    def updateContents(self):
        while self.contentLayout.count():
            item = self.contentLayout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clearLayout(item.layout())
                item.layout().deleteLater()

        for i in range(len(delegatesList)):
            rowLayout = QHBoxLayout()
            nameLabel = QLabel(delegatesList[i])
            rowLayout.addWidget(nameLabel)
            rowLayout.addStretch()

            present = presentVotingList[0][i]
            voting = presentVotingList[1][i]

            presentLabel = QLabel("Present" if present else "Not present")
            presentLabel.setStyleSheet("color: green;" if present else "color: red;")
            rowLayout.addWidget(presentLabel)

            votingLabel = QLabel("Voting" if voting else "Can abstain")
            votingLabel.setStyleSheet("color: #5b92e5;" if voting else "color: gray;")
            rowLayout.addWidget(votingLabel)

            centered = QHBoxLayout()
            centered.addStretch()
            centered.addLayout(rowLayout)
            centered.addStretch()

            self.contentLayout.addLayout(centered)

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clearLayout(item.layout())
                item.layout().deleteLater()



class motions(QMainWindow):
    def __init__(self, presentWindow):
        super().__init__()
        self.presentWindow = presentWindow
        self.setWindowTitle("Oratora — Create Motion")
        self.setGeometry(100, 100, 500, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        self.motionType = QComboBox()
        self.motionType.addItems([
            "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus", "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution", "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate","Adjourn Session","Suspend Session"
        ])
        layout.addWidget(QLabel("Motion for:"))
        layout.addWidget(self.motionType)

        layout.addWidget(QLabel("Proposer:"))
        self.proposer = QComboBox()
        self.proposer.addItems(delegatesList)
        layout.addWidget(self.proposer)

        self.title = QLineEdit()
        self.title.setPlaceholderText("Enter title of caucus")
        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title)

        layout.addWidget(QLabel("Total time for caucus:"))

        timeLayout = QHBoxLayout()
        self.totalTimeMinutes = QSpinBox()
        self.totalTimeMinutes.setRange(0, 60)
        self.totalTimeMinutes.setSuffix(" min")
        timeLayout.addWidget(self.totalTimeMinutes)

        self.totalTimeSeconds = QSpinBox()
        self.totalTimeSeconds.setRange(0, 59)
        self.totalTimeSeconds.setSuffix(" sec")
        timeLayout.addWidget(self.totalTimeSeconds)

        layout.addLayout(timeLayout)

        layout.addWidget(QLabel("Speaking time per speaker:"))
        self.speakingTime = QSpinBox()
        self.speakingTime.setRange(5, 300)
        self.speakingTime.setSuffix(" sec")
        layout.addWidget(self.speakingTime)

        submit = QPushButton("Start Motion")
        submit.clicked.connect(self.submitMotion)
        layout.addWidget(submit)
        self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

        layout.addStretch()

    def submitMotion(self):
        motionType = self.motionType.currentText()
        proposer = self.proposer.currentText()
        title = self.title.text() if hasattr(self, "title") else None
        totalMin = self.totalTimeMinutes.value() if hasattr(self, "totalTimeMinutes") else None
        totalSec = self.totalTimeSeconds.value() if hasattr(self, "totalTimeSeconds") else None
        speaking = self.speakingTime.value() if hasattr(self, "speakingTime") else None

        self.presentWindow.displayMotion(motionType, proposer, title, totalMin, totalSec, speaking)
        self.presentWindow.show()

    def onTypeChanged(self, layout, presentWindow):
        motionType = self.motionType.currentText()
        self.clearLayout(layout)
        if motionType == "Open Moderated Caucus":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Open Moderated Caucus")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            self.title = QLineEdit()
            self.title.setPlaceholderText("Enter title of caucus")
            layout.addWidget(QLabel("Title:"))
            layout.addWidget(self.title)

            layout.addWidget(QLabel("Total time for caucus:"))

            timeLayout = QHBoxLayout()
            self.totalTimeMinutes = QSpinBox()
            self.totalTimeMinutes.setRange(0, 60)
            self.totalTimeMinutes.setSuffix(" min")
            timeLayout.addWidget(self.totalTimeMinutes)

            self.totalTimeSeconds = QSpinBox()
            self.totalTimeSeconds.setRange(0, 59)
            self.totalTimeSeconds.setSuffix(" sec")
            timeLayout.addWidget(self.totalTimeSeconds)

            layout.addLayout(timeLayout)

            layout.addWidget(QLabel("Speaking time per speaker:"))
            self.speakingTime = QSpinBox()
            self.speakingTime.setRange(5, 300)
            self.speakingTime.setSuffix(" sec")
            layout.addWidget(self.speakingTime)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()
        elif motionType == "Open Unmoderated Caucus":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Open Unmoderated Caucus")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            layout.addWidget(QLabel("Total time for caucus:"))

            timeLayout = QHBoxLayout()
            self.totalTimeMinutes = QSpinBox()
            self.totalTimeMinutes.setRange(0, 60)
            self.totalTimeMinutes.setSuffix(" min")
            timeLayout.addWidget(self.totalTimeMinutes)

            self.totalTimeSeconds = QSpinBox()
            self.totalTimeSeconds.setRange(0, 59)
            self.totalTimeSeconds.setSuffix(" sec")
            timeLayout.addWidget(self.totalTimeSeconds)

            layout.addLayout(timeLayout)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()
        elif motionType == "Extend Unmoderated Caucus":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Extend Unmoderated Caucus")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            layout.addWidget(QLabel("Extend unmoderated caucus by:"))

            timeLayout = QHBoxLayout()
            self.totalTimeMinutes = QSpinBox()
            self.totalTimeMinutes.setRange(0, 60)
            self.totalTimeMinutes.setSuffix(" min")
            timeLayout.addWidget(self.totalTimeMinutes)

            self.totalTimeSeconds = QSpinBox()
            self.totalTimeSeconds.setRange(0, 59)
            self.totalTimeSeconds.setSuffix(" sec")
            timeLayout.addWidget(self.totalTimeSeconds)

            layout.addLayout(timeLayout)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()
        elif motionType == "Open Debate":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Open Debate")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()
        elif motionType == "Close Debate":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Close Debate")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()
        elif motionType == "Adjourn Session":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Adjourn Session")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()
        elif motionType == "Suspend Session":
            self.presentWindow = presentWindow
            self.setWindowTitle("Oratora — Create Motion")
            self.setGeometry(100, 100, 500, 300)

            centralWidget = QWidget()
            self.setCentralWidget(centralWidget)
            layout = QVBoxLayout()
            centralWidget.setLayout(layout)

            self.motionType = QComboBox()
            self.motionType.addItems([
                "Open Moderated Caucus", "Open Unmoderated Caucus", "Extend Unmoderated Caucus",
                "Extend Moderated Caucus", "Close Moderated Caucus", "Introduce Draft Resolution",
                "Introduce Amendment", "Vote on Resolution", "Open Debate", "Close Debate", "Adjourn Session",
                "Suspend Session"
            ])
            layout.addWidget(QLabel("Motion for:"))
            layout.addWidget(self.motionType)
            self.motionType.setCurrentText("Suspend Session")

            layout.addWidget(QLabel("Proposer:"))
            self.proposer = QComboBox()
            self.proposer.addItems(delegatesList)
            layout.addWidget(self.proposer)

            submit = QPushButton("Start Motion")
            submit.clicked.connect(self.submitMotion)
            layout.addWidget(submit)
            self.motionType.currentTextChanged.connect(lambda: self.onTypeChanged(layout, presentWindow))

            layout.addStretch()



    def initMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        fileMenu = menuBar.addMenu("File")

        saveAction = QAction("Save", self)
        saveAction.triggered.connect(lambda: print("Save clicked!"))
        fileMenu.addAction(saveAction)

        loadAction = QAction("Load", self)
        loadAction.triggered.connect(lambda: print("Load clicked!"))
        fileMenu.addAction(loadAction)

        actionMenu = menuBar.addMenu("Actions")

        createMotion = QAction("Create Motion", self)
        actionMenu.triggered.connect(lambda: print("Create Motion clicked!"))
        actionMenu.addAction(createMotion)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = committeeCreate()
    window.show()
    sys.exit(app.exec())
