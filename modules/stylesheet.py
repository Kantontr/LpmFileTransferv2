import os


class Stylesheet:

    def __init__(self):
        self.dark = {}
        self.dark["background"] = "color:rgb(222,222,222);" \
                                  "background-color: " \
                                  "rgba(41,41,41,200); " \
                                  "border: 2px ;"

        self.dark["button"] = "QPushButton {" \
                              "color:rgb(222,222,222); " \
                              "background-color: rgba(70,70,70,200); " \
                              "border: 1px;" \
                              "border-width: 1px;" \
                              "border-radius: 4px;" \
                              "border-style: outset;" \
                              "border-color: rgba(0,0,0,1);" \
                              "}" \
                              "QPushButton:pressed { background-color: rgba(20,20,20,200) }" \
                              "QPushButton:hover { background-color: rgba(150,150,150,200) }"

        self.dark["tree"] = "QTreeWidget {" \
                            "show-decoration-selected: 1;"\
                            "color:rgb(222,222,222); " \
                            "background-color: rgba(50,50,50,200); " \
                            "border: 2px;" \
                            "border-width: 1px;" \
                            "border-radius: 4px;" \
                            "border-style: outset;" \
                            "border-color: rgba(0,0,0,1);" \
                            "}" \
                            "QTreeWidget:item:selected {" \
                            "background-color: rgba(90,90,90,200)" \
                            "}" \
                            "QTreeWidget:item:hover {" \
                            "background-color: rgba(90,90,90,200)" \
                            "}"\
