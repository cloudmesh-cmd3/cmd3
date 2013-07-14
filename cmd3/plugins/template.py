import textwrap


class template:

    def activate_template(self):
        self.prompt = "cm> "

        self.banner = textwrap.dedent("""
                          FutureGrid - Cloud Mesh Shell
            ------------------------------------------------------
               ____ _                 _   __  __           _
              / ___| | ___  _   _  __| | |  \/  | ___  ___| |__
             | |   | |/ _ \| | | |/ _` | | |\/| |/ _ \/ __| '_ \
             | |___| | (_) | |_| | (_| | | |  | |  __/\__ \ | | |
              \____|_|\___/ \__,_|\__,_| |_|  |_|\___||___/_| |_|
            ======================================================
            """)

    def preloop(self):
        print textwrap.dedent(self.banner)
