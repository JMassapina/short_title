def short_title(title, length):
    """
    This function receives a title and a maximum length, and returns a shortened version of the title according to the rules:
    Full title should be no longer than length symbols
    If title is longer than length symbols, "..." should be added at the end
    Title should end on a full word
    """

    # Check if title is empty or consists only of spaces
    if not title.strip():
        return "Title cannot be empty or consist of only spaces."
    
    # If the title is already short enough, return it as is
    if len(title) <= length:
        return title
    
    # Split the title into words
    words = title.split()
    short_title = ""
    # Iterate through the words and add them to the short title, until it reaches the maximum length
    for word in words:
        if len(short_title) + len(word) + 3 <= length:
            short_title += word + " "
        else:
            break
    # Return the short title with "..." added at the end
    return short_title.strip() + "..."
