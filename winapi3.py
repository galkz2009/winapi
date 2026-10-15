import win32clipboard

data = ""
while True:
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(13):
            new_data = win32clipboard.GetClipboardData(13)
            win32clipboard.CloseClipboard()
            if new_data != data:
                print(f"Clipboard data: {new_data}")
                data = new_data
        else:
            win32clipboard.CloseClipboard()
    except Exception as e:
        pass