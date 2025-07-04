from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QTimer
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

#i am going to fucking commit murderrrrrrrrRRRRRRRRRR
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

        createMod = QAction("Moderated Caucus / GSL", self)
        createMod.triggered.connect(self.openModCauc)
        actionMenu.addAction(createMod)

        unmodAction = QAction("Unmoderated Caucus", self)
        unmodAction.triggered.connect(self.openUnmodWindow)
        actionMenu.addAction(unmodAction)

        voteAction = QAction("Voting", self)
        voteAction.triggered.connect(self.openVotingPanel)
        actionMenu.addAction(voteAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

    def openMotionWindow(self):
        self.motionWindow = motions(self.presentWindow)
        self.motionWindow.show()
        self.close()

    def openUnmodWindow(self):
        self.unmodWindow = unmod(self.presentWindow)
        self.unmodWindow.show()
        self.close()

    def openModCauc(self):
        self.modCauc = modCauc(self.presentWindow)
        self.modCauc.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()


class presentationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.motionHistory = []
        self.setWindowTitle("Roll call")
        self.setGeometry(150, 150, 1280, 720)
        self.isShowingMotion = False
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.verticalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.verticalLayout)

        self.header = QLabel("<h1>Roll call</h1>")
        self.verticalLayout.addWidget(self.header)

        self.contentLayout = QVBoxLayout()
        self.verticalLayout.addLayout(self.contentLayout)

        self.verticalLayout.addStretch()

    def displayModCauc(self, currentSpeaker, upcomingSpeakers, remainingSpeakerTime, remainingTotalTime):
        self.header.setText("<h1>Moderated Caucus</h1>")
        self.clearLayout(self.contentLayout)

        current = QLabel(f"<h2>Current Speaker: {currentSpeaker}</h2>")
        self.contentLayout.addWidget(current)

        speakerTimeMin = remainingSpeakerTime // 60000
        speakerTimeSec = (remainingSpeakerTime % 60000) // 1000
        totalTimeMin = remainingTotalTime // 60000
        totalTimeSec = (remainingTotalTime % 60000) // 1000

        speakerTimeLabel = QLabel(f"Time left for speaker: {speakerTimeMin:02}:{speakerTimeSec:02}")
        totalTimeLabel = QLabel(f"Total time left: {totalTimeMin:02}:{totalTimeSec:02}")

        self.contentLayout.addWidget(speakerTimeLabel)
        self.contentLayout.addWidget(totalTimeLabel)

        if upcomingSpeakers:
            upcomingLabel = QLabel("<b>Upcoming Speakers:</b>")
            self.contentLayout.addWidget(upcomingLabel)

            for speaker in upcomingSpeakers:
                self.contentLayout.addWidget(QLabel(f"– {speaker}"))

    def displayMotion(self, motionType, proposer, title=None, totalMinutes=None, totalSeconds=None, speakingTime=None, result=None):
        self.isShowingMotion = True
        self.header.setText("<h1>Motion</h1>")
        self.clearLayout(self.contentLayout)
        buttonLayout = QHBoxLayout()
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

        if result:
            self.contentLayout.addWidget(QLabel(f"<b>Result: {result}</b>"))


        self.contentLayout.addLayout(buttonLayout)

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

    def finalizeMotion(self, motionType, proposer, title, totalMinutes, totalSeconds, speakingTime, result):
        motionData = {
            "type": motionType,
            "proposer": proposer,
            "title": title,
            "totalMinutes": totalMinutes,
            "totalSeconds": totalSeconds,
            "speakingTime": speakingTime,
            "result": result
        }

        self.motionHistory.append(motionData)

        QMessageBox.information(self, "Motion Result", f"{motionType} {result}.")

        self.updateContents()

    def recordMotion(self, motionType, proposer, title=None, totalMinutes=None, totalSeconds=None, speakingTime=None, result=None):
        motion = {
            "type": motionType,
            "proposer": proposer,
            "title": title,
            "totalMinutes": totalMinutes,
            "totalSeconds": totalSeconds,
            "speakingTime": speakingTime,
            "result": result
        }
        self.motionHistory.append(motion)
        self.displayMotion(motionType, proposer, title, totalMinutes, totalSeconds, speakingTime, result)

class motions(QMainWindow):
    def __init__(self, presentWindow):
        super().__init__()
        self.presentWindow = presentWindow
        self.setWindowTitle("Oratora — Create Motion")
        self.setGeometry(100, 100, 500, 400)
        self.motionQueue = []

        self.initMenuBar()
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.motionType = QComboBox()
        self.motionType.addItems([
            "Open Moderated Caucus", "Open Unmoderated Caucus",
            #"Extend Unmoderated Caucus", "Extend Moderated Caucus"
            # , "Close Moderated Caucus", "Introduce Draft Resolution",
            #"Introduce Amendment", "Vote on Resolution",
            "Open Debate", "Close Debate",
            "Adjourn Session", "Suspend Session"
        ])
        self.layout.addWidget(QLabel("Motion for:"))
        self.layout.addWidget(self.motionType)

        self.layout.addWidget(QLabel("Proposer:"))
        self.proposer = QComboBox()
        self.proposer.addItems(delegatesList)
        self.layout.addWidget(self.proposer)

        self.titleLabel = QLabel("Title:")
        self.title = QLineEdit()
        self.title.setPlaceholderText("Enter title of caucus")
        self.layout.addWidget(self.titleLabel)
        self.layout.addWidget(self.title)

        self.layout.addWidget(QLabel("Total time for caucus:"))
        timeLayout = QHBoxLayout()
        self.totalTimeMinutes = QSpinBox()
        self.totalTimeMinutes.setRange(0, 60)
        self.totalTimeMinutes.setSuffix(" min")
        timeLayout.addWidget(self.totalTimeMinutes)

        self.totalTimeSeconds = QSpinBox()
        self.totalTimeSeconds.setRange(0, 59)
        self.totalTimeSeconds.setSuffix(" sec")
        timeLayout.addWidget(self.totalTimeSeconds)
        self.layout.addLayout(timeLayout)

        self.speakingLabel = QLabel("Speaking time per speaker:")
        self.speakingTime = QSpinBox()
        self.speakingTime.setRange(5, 300)
        self.speakingTime.setSuffix(" sec")
        self.layout.addWidget(self.speakingLabel)
        self.layout.addWidget(self.speakingTime)

        self.submitBtn = QPushButton("Start Motion")
        self.submitBtn.clicked.connect(self.submitMotion)
        self.layout.addWidget(self.submitBtn)

        self.resultButtons = QHBoxLayout()
        self.passButton = QPushButton("Pass")
        self.failButton = QPushButton("Fail")
        self.passButton.clicked.connect(lambda: self.finalizeMotion("Passed"))
        self.failButton.clicked.connect(lambda: self.finalizeMotion("Failed"))
        self.resultButtons.addStretch()
        self.resultButtons.addWidget(self.passButton)
        self.resultButtons.addWidget(self.failButton)
        self.resultButtons.addStretch()
        self.layout.addLayout(self.resultButtons)

        self.motionType.currentTextChanged.connect(self.adjustFormForMotion)
        self.adjustFormForMotion(self.motionType.currentText())

    def adjustFormForMotion(self, motionType):
        needsTitle = motionType == "Open Moderated Caucus"
        needsTime = motionType in [
            "Open Moderated Caucus", "Open Unmoderated Caucus",
            "Extend Unmoderated Caucus", "Extend Moderated Caucus"
        ]
        needsSpeaking = motionType == "Open Moderated Caucus"

        self.titleLabel.setVisible(needsTitle)
        self.title.setVisible(needsTitle)

        self.totalTimeMinutes.setVisible(needsTime)
        self.totalTimeSeconds.setVisible(needsTime)

        self.speakingLabel.setVisible(needsSpeaking)
        self.speakingTime.setVisible(needsSpeaking)

    def submitMotion(self):
        motionType = self.motionType.currentText()
        proposer = self.proposer.currentText()
        title = self.title.text() if self.title.isVisible() else None
        totalMin = self.totalTimeMinutes.value() if self.totalTimeMinutes.isVisible() else None
        totalSec = self.totalTimeSeconds.value() if self.totalTimeSeconds.isVisible() else None
        speaking = self.speakingTime.value() if self.speakingTime.isVisible() else None

        motion = {
            "type": motionType,
            "proposer": proposer,
            "title": title,
            "totalMin": totalMin,
            "totalSec": totalSec,
            "speaking": speaking,
            "status": "Pending"
        }
        self.motionQueue.append(motion)

        # immediately show in presentationWindow
        self.presentWindow.recordMotion(
            motion["type"],
            motion["proposer"],
            motion["title"],
            motion["totalMin"],
            motion["totalSec"],
            motion["speaking"],
            motion["status"]
        )
        self.presentWindow.show()

    def finalizeMotion(self, result):
        if not self.motionQueue:
            return

        latest = self.motionQueue[-1]
        latest["status"] = result

        self.presentWindow.recordMotion(
            latest["type"],
            latest["proposer"],
            latest["title"],
            latest["totalMin"],
            latest["totalSec"],
            latest["speaking"],
            result
        )

        QMessageBox.information(self, "Motion Status Updated", f"Motion marked as {result}.")
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

        rollCall = QAction("Roll Call", self)
        rollCall.triggered.connect(self.openRollCall)
        actionMenu.addAction(rollCall)

        createMod = QAction("Moderated Caucus / GSL", self)
        createMod.triggered.connect(self.openModCauc)
        actionMenu.addAction(createMod)

        unmodTimerAction = QAction("Unmoderated Caucus", self)
        unmodTimerAction.triggered.connect(self.openUnmod)
        actionMenu.addAction(unmodTimerAction)

        voteAction = QAction("Voting", self)
        voteAction.triggered.connect(self.openVotingPanel)
        actionMenu.addAction(voteAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

    def openRollCall(self):
        self.attendanceWindow = attendance(self.presentWindow)
        self.attendanceWindow.show()
        self.close()

    def openUnmod(self):
        self.unmodWindow = unmod(self.presentWindow)
        self.unmodWindow.show()
        self.close()

    def openModCauc(self):
        self.modCauc = modCauc(self.presentWindow)
        self.modCauc.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()


class unmod(QMainWindow):
    def __init__(self, presentWindow, totalMinutes=5, totalSeconds=0):
        super().__init__()
        self.presentWindow = presentWindow
        self.setWindowTitle("Oratora — Unmoderated Caucus")
        self.setGeometry(100, 100, 400, 400)

        self.initMenuBar()

        self.initUI()

    def initUI(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.layout = QVBoxLayout()
        self.central.setLayout(self.layout)
        self.layout.addWidget(QLabel("<h1>Unmoderated Caucus</h1>"))
        self.layout.addWidget(QLabel("Set Duration:"))

        timeInputLayout = QHBoxLayout()
        self.minutesInput = QSpinBox()
        self.minutesInput.setRange(0, 60)
        self.minutesInput.setSuffix(" min")
        self.minutesInput.setValue(5)

        self.secondsInput = QSpinBox()
        self.secondsInput.setRange(0, 59)
        self.secondsInput.setSuffix(" sec")
        self.secondsInput.setValue(0)

        timeInputLayout.addWidget(self.minutesInput)
        timeInputLayout.addWidget(self.secondsInput)
        self.layout.addLayout(timeInputLayout)

        self.setTimeButton = QPushButton("Set Time")
        self.setTimeButton.clicked.connect(self.setTimer)
        self.layout.addWidget(self.setTimeButton)

        self.timerDisplay = QLabel("00:00")
        self.timerDisplay.setStyleSheet("font-size: 100px; qproperty-alignment: 'AlignCenter';")
        self.timerDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.timerDisplay)

        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.startTimer)
        self.layout.addWidget(self.startButton)

        self.pauseButton = QPushButton("Pause")
        self.pauseButton.clicked.connect(self.pauseTimer)
        self.layout.addWidget(self.pauseButton)

        self.resetButton = QPushButton("Reset")
        self.resetButton.clicked.connect(self.resetTimer)
        self.layout.addWidget(self.resetButton)

        # Timer setup
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateTimer)

        self.totalDuration = 5 * 60 * 1000
        self.remainingTime = self.totalDuration
        self.updateTimerDisplay()

    def setTimer(self):
        minutes = self.minutesInput.value()
        seconds = self.secondsInput.value()
        self.totalDuration = (minutes * 60 + seconds) * 1000
        self.remainingTime = self.totalDuration
        self.updateTimerDisplay()

    def updateTimer(self):
        self.remainingTime -= 1000
        if self.remainingTime <= 0:
            self.timer.stop()
            self.remainingTime = 0
            self.timerDisplay.setText("Time's up!")
        else:
            self.updateTimerDisplay()

    def updateTimerDisplay(self):
        minutes = self.remainingTime // 60000
        seconds = (self.remainingTime % 60000) // 1000
        self.timerDisplay.setText(f"{minutes:02}:{seconds:02}")

    def startTimer(self):
        if self.remainingTime > 0:
            self.timer.start()

    def pauseTimer(self):
        self.timer.stop()

    def resetTimer(self):
        self.timer.stop()
        self.remainingTime = self.totalDuration
        self.updateTimerDisplay()

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

        rollCall = QAction("Roll Call", self)
        rollCall.triggered.connect(self.openRollCall)
        actionMenu.addAction(rollCall)

        createMotion = QAction("Create Motion", self)
        createMotion.triggered.connect(self.openMotionWindow)
        actionMenu.addAction(createMotion)

        createMod = QAction("Moderated Caucus / GSL", self)
        createMod.triggered.connect(self.openModCauc)
        actionMenu.addAction(createMod)

        voteAction = QAction("Voting", self)
        voteAction.triggered.connect(self.openVotingPanel)
        actionMenu.addAction(voteAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

    def openRollCall(self):
        self.attendanceWindow = attendance(self.presentWindow)
        self.attendanceWindow.show()
        self.close()

    def openMotionWindow(self):
        self.motionWindow = motions(self.presentWindow)
        self.motionWindow.show()
        self.close()

    def openModCauc(self):
        self.modCauc = modCauc(self.presentWindow)
        self.modCauc.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()

class modCauc(QMainWindow):
    def __init__(self, presentWindow):
        super().__init__()
        self.presentWindow = presentWindow
        self.setWindowTitle("Oratora — Moderated Caucus")
        self.setGeometry(100, 100, 500, 400)
        self.initMenuBar()
#god fucking save me i am very much goign insane i hate this python library so much but it's way way too late to turn back save me save me save me save me save me akldflj,sa,vsdh,vfksdcsdkf krill meeeeee
        if not self.presentWindow.isVisible():
            self.presentWindow.show()
        self.totalTime = 5 * 60 * 1000
        self.speakerTime = 60 * 1000
        self.remainingTotal = self.totalTime
        self.remainingSpeaker = self.speakerTime

        self.speakers = []
        self.currentSpeakerIndex = 0

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateTimers)

        self.initUI()

    def initUI(self):
        central = QWidget()
        self.setCentralWidget(central)
        self.mainLayout = QVBoxLayout()
        central.setLayout(self.mainLayout)

        self.speakerDropdown = QComboBox()
        self.speakerDropdown.addItems(delegatesList)
        self.mainLayout.addWidget(self.speakerDropdown)

        addBtn = QPushButton("Add Speaker")
        addBtn.clicked.connect(self.addSpeaker)
        self.mainLayout.addWidget(addBtn)

        self.speakerListWidget = QListWidget()
        self.mainLayout.addWidget(self.speakerListWidget)

        self.totalTimeInput = QSpinBox()
        self.totalTimeInput.setRange(1, 120)
        self.totalTimeInput.setSuffix(" min")
        self.totalTimeInput.setValue(5)
        self.mainLayout.addWidget(QLabel("Total caucus time:"))
        self.mainLayout.addWidget(self.totalTimeInput)

        self.speakerTimeInput = QSpinBox()
        self.speakerTimeInput.setRange(10, 300)
        self.speakerTimeInput.setSuffix(" sec")
        self.speakerTimeInput.setValue(60)
        self.mainLayout.addWidget(QLabel("Time per speaker:"))
        self.mainLayout.addWidget(self.speakerTimeInput)


        self.startBtn = QPushButton("Start")
        self.startBtn.clicked.connect(self.startTimers)
        self.mainLayout.addWidget(self.startBtn)

        self.pauseBtn = QPushButton("Pause")
        self.pauseBtn.clicked.connect(self.pauseTimers)
        self.mainLayout.addWidget(self.pauseBtn)

        self.resetBtn = QPushButton("Reset")
        self.resetBtn.clicked.connect(self.resetTimers)

        self.yieldButton = QPushButton("Yield Time")
        self.yieldButton.clicked.connect(self.yieldTime)
        self.mainLayout.addWidget(self.yieldButton)

        self.mainLayout.addWidget(self.resetBtn)

        self.updatePresentation()

    def yieldTime(self):
        self.nextSpeaker()

    def nextSpeaker(self):
        self.timer.stop()

        self.currentSpeakerIndex += 1
        if self.currentSpeakerIndex >= len(self.speakers):
            QMessageBox.information(self, "GSL", "No more speakers.")
            self.presentWindow.clearLayout(self.presentWindow.contentLayout)
            return

        self.speakerRemainingTime = self.speakerTime
        self.updatePresentation()
        self.timer.start()

    def addSpeaker(self):
        name = self.speakerDropdown.currentText()
        self.speakers.append(name)
        self.speakerListWidget.addItem(name)
        self.updatePresentation()

    def startTimers(self):
        self.totalTime = self.totalTimeInput.value() * 60 * 1000
        self.speakerTime = self.speakerTimeInput.value() * 1000
        self.remainingTotal = self.totalTime
        self.remainingSpeaker = self.speakerTime
        self.timer.start()
        self.updatePresentation()

    def pauseTimers(self):
        self.timer.stop()

    def resetTimers(self):
        self.remainingTotal = self.totalTime
        self.remainingSpeaker = self.speakerTime
        self.currentSpeakerIndex = 0
        self.timer.stop()
        self.updatePresentation()

    def updateTimers(self):
        self.remainingSpeaker -= 1000
        self.remainingTotal -= 1000

        if self.remainingSpeaker <= 0:
            self.remainingSpeaker = self.speakerTime
            self.currentSpeakerIndex += 1
            if self.currentSpeakerIndex >= len(self.speakers):
                self.timer.stop()
                return

        self.updatePresentation()

    def updatePresentation(self):
        current = self.speakers[self.currentSpeakerIndex] if self.currentSpeakerIndex < len(self.speakers) else "(None)"
        upcoming = self.speakers[self.currentSpeakerIndex+1:]

        self.presentWindow.displayModCauc(
            current,
            upcoming,
            self.remainingSpeaker,
            self.remainingTotal
        )
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

        rollCall = QAction("Roll Call", self)
        rollCall.triggered.connect(self.openRollCall)
        actionMenu.addAction(rollCall)

        createMotion = QAction("Create Motion", self)
        createMotion.triggered.connect(self.openMotionWindow)
        actionMenu.addAction(createMotion)

        unmodTimerAction = QAction("Unmoderated Caucus", self)
        unmodTimerAction.triggered.connect(self.openUnmod)
        actionMenu.addAction(unmodTimerAction)

        voteAction = QAction("Voting", self)
        voteAction.triggered.connect(self.openVotingPanel)
        actionMenu.addAction(voteAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

    def openRollCall(self):
        self.attendanceWindow = attendance(self.presentWindow)
        self.attendanceWindow.show()
        self.close()

    def openUnmod(self):
        self.unmodWindow = unmod(self.presentWindow)
        self.unmodWindow.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()

    def openMotionWindow(self):
        self.motionWindow = motions(self.presentWindow)
        self.motionWindow.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()

class votingPanel(QMainWindow):
    def __init__(self, presentWindow):
        super().__init__()
        self.presentWindow = presentWindow
        self.setWindowTitle("Oratora — Voting Panel")
        self.setGeometry(100, 100, 400, 300)
        self.initMenuBar()
        self.yesCount = 0
        self.noCount = 0
        self.abstainCount = 0
        self.requiredPercent = 50  # default threshold to pass

        self.initUI()
        self.presentWindow.show()  # Automatically show presentation window

    def initUI(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        central.setLayout(layout)

        self.voteDisplays = {}
        for label in ["Yes", "No", "Abstain"]:
            h = QHBoxLayout()
            countLabel = QLabel(f"{label}: 0")
            self.voteDisplays[label] = countLabel
            h.addWidget(countLabel)
            plus = QPushButton("+")
            minus = QPushButton("-")
            plus.clicked.connect(lambda _, l=label: self.adjustVote(l, 1))
            minus.clicked.connect(lambda _, l=label: self.adjustVote(l, -1))
            h.addWidget(plus)
            h.addWidget(minus)
            layout.addLayout(h)

        self.percentInput = QSpinBox()
        self.percentInput.setRange(0, 100)
        self.percentInput.setValue(self.requiredPercent)
        self.percentInput.setSuffix("% required to pass")
        self.percentInput.valueChanged.connect(self.recalculate)
        layout.addWidget(self.percentInput)

        layout.addStretch()
        self.recalculate()

    def adjustVote(self, category, delta):
        if category == "Yes":
            self.yesCount = max(0, self.yesCount + delta)
        elif category == "No":
            self.noCount = max(0, self.noCount + delta)
        elif category == "Abstain":
            self.abstainCount = max(0, self.abstainCount + delta)
        self.updateVotes()
        self.recalculate()

    def updateVotes(self):
        self.voteDisplays["Yes"].setText(f"Yes: {self.yesCount}")
        self.voteDisplays["No"].setText(f"No: {self.noCount}")
        self.voteDisplays["Abstain"].setText(f"Abstain: {self.abstainCount}")

    def recalculate(self):
        totalVoting = self.yesCount + self.noCount
        if totalVoting == 0:
            resultText = "—"
            resultStyle = "color: black;"
        else:
            yesPercentage = (self.yesCount / totalVoting) * 100
            required = self.percentInput.value()
            if yesPercentage >= required:
                resultText = f"Passed ({yesPercentage:.1f}% Yes)"
                resultStyle = "color: green;"
            else:
                resultText = f"Failed ({yesPercentage:.1f}% Yes)"
                resultStyle = "color: red;"

        self.displayOnPresentation(resultText, resultStyle)

    def displayOnPresentation(self, resultText, resultStyle):
        self.presentWindow.clearLayout(self.presentWindow.contentLayout)
        self.presentWindow.header.setText("<h1>Voting Results</h1>")

        yes = QLabel(f"Yes: {self.yesCount}")
        no = QLabel(f"No: {self.noCount}")
        abstain = QLabel(f"Abstain: {self.abstainCount}")
        required = QLabel(f"Required to Pass: {self.percentInput.value()}%")
        result = QLabel(f"<b>{resultText}</b>")
        result.setStyleSheet(resultStyle + " font-size: 24px;")

        self.presentWindow.contentLayout.addWidget(yes)
        self.presentWindow.contentLayout.addWidget(no)
        self.presentWindow.contentLayout.addWidget(abstain)
        self.presentWindow.contentLayout.addWidget(required)
        self.presentWindow.contentLayout.addWidget(result)

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

        rollCall = QAction("Roll Call", self)
        rollCall.triggered.connect(self.openRollCall)
        actionMenu.addAction(rollCall)

        createMotion = QAction("Create Motion", self)
        createMotion.triggered.connect(self.openMotionWindow)
        actionMenu.addAction(createMotion)

        createMod = QAction("Moderated Caucus / GSL", self)
        createMod.triggered.connect(self.openModCauc)
        actionMenu.addAction(createMod)

        unmodTimerAction = QAction("Unmoderated Caucus", self)
        unmodTimerAction.triggered.connect(self.openUnmod)
        actionMenu.addAction(unmodTimerAction)

        helpMenu = menuBar.addMenu("Help")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(lambda: QMessageBox.information(self, "About Oratora", "Made with ❤️ by Astra"))
        helpMenu.addAction(aboutAction)

    def openRollCall(self):
        self.attendanceWindow = attendance(self.presentWindow)
        self.attendanceWindow.show()
        self.close()

    def openUnmod(self):
        self.unmodWindow = unmod(self.presentWindow)
        self.unmodWindow.show()
        self.close()

    def openVotingPanel(self):
        self.voteWindow = votingPanel(self.presentWindow)
        self.voteWindow.show()
        self.close()

    def openMotionWindow(self):
        self.motionWindow = motions(self.presentWindow)
        self.motionWindow.show()
        self.close()

    def openModCauc(self):
        self.modCauc = modCauc(self.presentWindow)
        self.modCauc.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = committeeCreate()
    window.show()
    sys.exit(app.exec())