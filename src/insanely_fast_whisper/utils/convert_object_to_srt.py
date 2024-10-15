"""
Python Object to SRT Converter

This script converts a Python object containing timestamped chunks of text
into an SRT (SubRip Subtitle) format file.

Input: A Python object with the following structure:
{
    "speakers": [], # Optional list of speaker information
    "chunks": [
        {
            "timestamp": [startSeconds, endSeconds],
            "text": "Subtitle text"
        },
        ...
    ]
}

Where:
- startSeconds: Number of seconds elapsed from the start of the video to the beginning of the subtitle
- endSeconds: Number of seconds elapsed from the start of the video to the end of the subtitle

Note: Timestamps are floating-point numbers representing seconds, potentially including fractional parts.
For example, 13.4 represents 13 seconds and 400 milliseconds.

Output: An SRT file with formatted subtitles

Usage: Python 3.x is required to run this script.
You can import and use the functions in this script in your Python code.
"""

import datetime

def convert_object_to_srt(data):
    """
    Converts Python object data to SRT format
    :param data: The Python object containing subtitle data
    :return: The formatted SRT content as a string
    """
    chunks = data["chunks"]
    srt_content = []
    subtitle_index = 1

    for chunk in chunks:
        start_time = format_time(chunk["timestamp"][0])
        end_time = format_time(chunk["timestamp"][1])
        text = chunk["text"].strip()

        srt_content.append(f"{subtitle_index}\n{start_time} --> {end_time}\n{text}\n")
        subtitle_index += 1

    return "\n".join(srt_content)

def format_time(seconds):
    """
    Formats a timestamp in seconds to SRT time format (HH:MM:SS,mmm)
    :param seconds: The timestamp in seconds
    :return: Formatted time string
    """
    time = datetime.timedelta(seconds=seconds)
    hours, remainder = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int(time.microseconds / 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def process_object(data, output_path):
    """
    Converts the input Python object to SRT and writes the output file
    :param data: The input Python object containing subtitle data
    :param output_path: Path for the output SRT file
    """
    try:
        srt_content = convert_object_to_srt(data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        print('SRT file has been saved successfully.')
    except Exception as e:
        print(f'Error processing data: {str(e)}')

# Example usage
if __name__ == "__main__":
    # Example input data
    input_data = {
        "speakers": [],
        "chunks": [
            {"timestamp": [0, 5.5], "text": "Hello, this is the first subtitle."},
            {"timestamp": [6, 10.2], "text": "And this is the second one."},
            {"timestamp": [11, 15.8], "text": "Finally, the third subtitle."}
        ]
    }
    
    output_path = 'output.srt'
    process_object(input_data, output_path)
