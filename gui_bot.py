import tkinter as tk
from tkinter import ttk, messagebox
import time
from logger import log_info, log_error

class BasicBot:
    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            log_info(f"GUI Simulated Order - symbol: {symbol}, side: {side}, type: {order_type}, quantity: {quantity}, price: {price}, stop_price: {stop_price}")
            time.sleep(1)
            simulated_response = {
                "symbol": symbol,
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
                "price": price or "market price",
                "stop_price": stop_price or "N/A",
                "status": "FILLED",
                "orderId": int(time.time()),
                "timestamp": int(time.time() * 1000)
            }
            log_info(f"GUI Simulated Response: {simulated_response}")
            return simulated_response
        except Exception as e:
            log_error(str(e))
            return {"error": str(e)}

def place_order():
    symbol = symbol_var.get().upper()
    side = side_var.get().upper()
    order_type = type_var.get()
    quantity = quantity_var.get()
    price = price_var.get()
    stop_price = stop_var.get()

    if not symbol or not side or not order_type or not quantity:
        messagebox.showerror("Missing Input", "Please fill all required fields.")
        return

    result = bot.place_order(symbol, side, order_type, quantity, price or None, stop_price or None)
    messagebox.showinfo("✅ Order Placed", f"📋 Order Result:\n{result}")

# GUI Setup
root = tk.Tk()
root.title("📈 Binance Futures Trading Bot")
root.geometry("500x520")
root.configure(bg="#f0f4f8")

title = tk.Label(root, text="Binance Futures Trading Bot", font=("Helvetica", 18, "bold"), fg="#1f77b4", bg="#f0f4f8")
title.pack(pady=10)

form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack(pady=10)

def create_field(label_text, var, is_dropdown=False, options=None):
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 11, "bold"), bg="#f0f4f8")
    label.pack(pady=(8, 2))
    if is_dropdown:
        dropdown = ttk.Combobox(form_frame, textvariable=var, values=options, state="readonly", width=40)
        dropdown.pack()
    else:
        entry = tk.Entry(form_frame, textvariable=var, width=44)
        entry.pack()

symbol_var = tk.StringVar()
side_var = tk.StringVar()
type_var = tk.StringVar()
quantity_var = tk.StringVar()
price_var = tk.StringVar()
stop_var = tk.StringVar()

bot = BasicBot()

create_field("🔹 Symbol (e.g., BTCUSDT):", symbol_var)
create_field("🔹 Side:", side_var, is_dropdown=True, options=["BUY", "SELL"])
create_field("🔹 Order Type:", type_var, is_dropdown=True, options=["MARKET", "LIMIT", "STOP", "STOP_LIMIT"])
create_field("🔹 Quantity:", quantity_var)
create_field("🔹 Price (if applicable):", price_var)
create_field("🔹 Stop Price (if applicable):", stop_var)

place_btn = tk.Button(root, text="🚀 Place Order", command=place_order, font=("Helvetica", 12, "bold"), bg="#1f77b4", fg="white", padx=10, pady=6)
place_btn.pack(pady=20)

footer = tk.Label(root, text="Developed by Lokendra ❤️", font=("Helvetica", 9), bg="#f0f4f8", fg="gray")
footer.pack(pady=10)

root.mainloop()
