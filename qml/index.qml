import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

ApplicationWindow{
    id: window 
    width:  400
    height:  600
    visible: true
    title: qsTr("Nike Scrapper")

    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint

    Material.theme: Material.Light
    Material.accent:   "#000"

    
    Item{
        id:settings
        anchors{
            left:parent.left
            right:parent.right
            top:parent.top
            margins:10
        }
        anchors.horizontalCenter: parent.horizontalCenter

        Text{ //label
            id:settings_label
            text: qsTr("Set your settings")
            color: Material.accent
            font.pointSize: 15
            anchors.horizontalCenter: parent.horizontalCenter
            anchors{
                top: parent.top
                margins:10
            }
        }

        Rectangle{
            id:settings_browser
            height:60
            color:"transparent"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors{
                    left: parent.left
                    top: settings_label.bottom
                    margins:10
                }
            Text{ //header
                id:settings_browser_header
                color: Material.accent
                font.pointSize: 11
                text:qsTr("Choose your browser")
                anchors{
                    top:parent.top
                    left:parent.left
                }
            }
            ComboBox{ //selector
                id:settings_browser_selector
                width:parent.width
                model:["Chrome","Firefox","Edge"]
                anchors{
                    top:settings_browser_header.bottom
                    left:parent.left
                }
            }
        }
        
        //Checkbox & TextField
        Rectangle{
            id:settings_driver
            height:80
            color:"transparent"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors{
                left:parent.left
                top:settings_browser.bottom
                topMargin:10
                leftMargin:10
                rightMargin:10
            }
            Text{ //header
                id:settings_driver_header
                color: Material.accent
                font.pointSize: 11
                text:qsTr("Set your browser driver")
                anchors{
                    top:parent.top
                    left:parent.left
                }
            }
            TextField{ //path
                id:settings_driver_path
                placeholderText: qsTr("Set your path")
                width: parent.width - 20 - settings_driver_checker.width
                anchors{
                    left: parent.left
                    top: settings_driver_header.bottom
                }
            }
            CheckBox{ //checker
                id:settings_driver_checker
                checked:false
                text:qsTr("Auto")
                anchors{
                    top: settings_driver_header.bottom
                    left:settings_driver_path.right
                    leftMargin:10
                }
            }
            Text{ //label
                id:settings_driver_label
                text:qsTr("C:/ProgramFiles (x86)/driver.exe")
                color:Material.accent
                opacity: 0.2
                anchors{
                    left:parent.left
                    top:settings_driver_path.bottom
                    bottomMargin:10
                }
            }
        }
        Rectangle{
            id:settings_delay
            height:65
            anchors.horizontalCenter: parent.horizontalCenter
            color:"transparent"
            anchors{
                    top:settings_driver.bottom
                    left:parent.left
                    margins:10
                }
            Text{ //header
                id:settings_delay_header
                color: Material.accent
                font.pointSize: 11
                text:qsTr("Delay on seconds")
                anchors{
                    top:parent.top
                    left:parent.left
                }
            }
            TabBar{ //value
                id:settings_delay_value
                currentIndex:1
                contentWidth:parent.width
                anchors{
                    top:settings_delay_header.bottom
                    left:parent.left
                }
                TabButton{
                    text:qsTr("1")
                }
                TabButton{
                    text:qsTr("2")
                }
                TabButton{
                    text:qsTr("3")
                }
                TabButton{
                    text:qsTr("5")
                }
                TabButton{
                    text:qsTr("10")
                }
            }
        }
    }
}