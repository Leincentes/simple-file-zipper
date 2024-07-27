def update_progress_bar(progress_bar, value, root):
    progress_bar['value'] = value
    root.update_idletasks()
