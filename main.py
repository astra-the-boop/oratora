from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QComboBox
)
import sys

committeeName = ""
topic = ""
conferenceName = ""
delegatesList=[]

class committeeCreate(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oratora — Create Committee")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Create a new committee")
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
        self.setLayout(layout)

    def submitForm(self):
        committeeName = self.committeeName.text()
        topic = self.topic.text()
        conferenceName = self.conferenceName.text()

        print(committeeName, topic, conferenceName)

        if committeeName.strip() == "":
            warning = QLabel("Committee name cannot be empty")
            self.layout().addWidget(warning)
        else:
            self.dashboard = participants(committeeName, topic, conferenceName)
            self.dashboard.show()
            self.close()


class participants(QWidget):
    def __init__(self, committeeName="", topic="", conferenceName=""):
        super().__init__()
        print(committeeName, topic, conferenceName)
        self.setWindowTitle("Oratora — Dashboard")
        self.setGeometry(100, 100, 500, 400)
        layout = QVBoxLayout()

        self.label = QLabel(committeeName)
        layout.addWidget(self.label)
        self.label = QLabel(f"Topic: {topic}")
        layout.addWidget(self.label)
        self.label = QLabel(f"Conference: {conferenceName}")
        layout.addWidget(self.label)

        self.label = QLabel(f"\nParticipating delegates:")
        layout.addWidget(self.label)

        self.delegates = QComboBox()
        self.delegates.addItems([ #all UN nations blegh
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
            "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
            "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
            "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
            "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
            "Congo (Brazzaville)", "Congo (Kinshasa)", "Costa Rica", "Croatia", "Cuba",
            "Cyprus", "Czech Republic (Czechia)", "Denmark", "Djibouti", "Dominica",
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
            "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
            "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
            "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
            "Saint Vincent and the Grenadines", "Samoa", "San Marino",
            "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
            "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
            "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan",
            "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania",
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

        layout.addStretch()
        self.setLayout(layout)

    def addDelegate(self):
        if self.customDel.text().strip() == "":
            delegateAdded = self.delegates.currentText().strip()
        else:
            delegateAdded = self.customDel.text().strip()
        if delegateAdded.strip() not in delegatesList:
            self.delegateList.addItem(delegateAdded)
            delegatesList.append(delegateAdded)
            print(delegatesList)

    def next(self):
        if len(delegatesList) < 2:
            pass
        else:
            pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = committeeCreate()
    window.show()
    sys.exit(app.exec())
