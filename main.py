import tkinter as tk
from controllers.curp_controller import CurpController

# Ejecutamos el poryecto
if __name__ == "__main__":
    root = tk.Tk()
    app = CurpController(root)
    root.mainloop()