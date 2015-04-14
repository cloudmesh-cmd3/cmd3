import textwrap
from cmd3.console import Console

class template:

    def activate_template(self):
        """activates the template"""
        self.prompt = "cm> "

        self.banner = textwrap.dedent("""
            ======================================================
               ____ _                 _                     _     
              / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__  
             | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \ 
             | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | |
              \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_|
            ======================================================
                                 Cloudmesh Shell
            """)

    def preloop(self):
        """adds the banner to the preloop"""
        lines = textwrap.dedent(self.banner).split("\n")
        for line in lines:
            Console._print("BLUE", "", line)