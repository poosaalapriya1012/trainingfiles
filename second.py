root = tk.Tk()
root.title("Text Widget with Scrollbar")

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
text_widget = tk.Text(frame, height=10, width=40, yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH)

sample_text = "\n".join(f"Line {i}" for i in range(1, 51))
text_widget.insert(tk.END, sample_text)

root.mainloop()
