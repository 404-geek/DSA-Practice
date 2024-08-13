class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:

        message_length = len(message)
        # Initialize sum of lengths of all suffixes
        suffix_length_sum = 0
      
        # Iterate through the possible number of parts to split the message into
        for parts_count in range(1, message_length + 1):
            # Increment the sum of lengths of suffixes by the length of the current suffix
            suffix_length_sum += len(str(parts_count))
            # Calculate the total length of suffixes for the current number of parts
            total_suffix_length = len(str(parts_count)) * parts_count
            # Calculate the total length of separators needed for all parts ("<", "/", ">", for each part)
            separators_length = 3 * parts_count
            # Check if the message can fit into the specified limit when split into current number of parts
            if limit * parts_count - (suffix_length_sum + total_suffix_length + separators_length) >= message_length:
                # Initialize the list to store the resulting split message parts
                splitted_messages = []
                # Start index for slicing the message
                current_index = 0
                # Generate each part with its corresponding suffix
                for part_number in range(1, parts_count + 1):
                    # Create the string suffix for the current part
                    suffix = f'<{part_number}/{parts_count}>'
                    # Calculate and obtain the substring for the current part based on the limit and suffix
                    substring = message[current_index : current_index + limit - len(suffix)] + suffix
                    # Add the part to the list of split messages
                    splitted_messages.append(substring)
                    # Update the current index to the starting index of the next part
                    current_index += limit - len(suffix)
                # Return the list of split message parts
                return splitted_messages
        # Return an empty list if the message cannot be split within the limit
        return []
