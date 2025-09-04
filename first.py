require 'tk'
root = TkRoot.new { title "Double Click Event" }
button = TkButton.new(root) do
  text "Hover Over Me"
  pack { padx 10; pady 10 }
end
button.bind("Double-1") do
  button.text = "Double Clicked!"
end
Tk.mainloop
