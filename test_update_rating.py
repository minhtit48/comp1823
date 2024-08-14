import tkinter as tk
from update_video import UpdateVideo
import video_library as lib
import pytest

def test_update_video_successful_update(capsys, mocker):
    # Mock the Tkinter window and UpdateVideo class
    window = tk.Tk()
    update_video_app = UpdateVideo(window)

    # Set test inputs
    update_video_app.number_txt.insert(0, "01")
    update_video_app.new_rating.insert(0, "8")

    # Mock the lib.set_rating method
    mocker.patch('video_library.set_rating')

    # Call the update_new_rating method
    update_video_app.update_new_rating()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the status label text was updated correctly
    assert update_video_app.status_lbl.cget("text") == "Rating updated successfully."
    lib.set_rating.assert_called_once_with("01", 8)

    # Check the printed output
    assert "Rating updated successfully." in captured.out


def test_update_video_invalid_rating(capsys):
    # Mock the Tkinter window and UpdateVideo class
    window = tk.Tk()
    update_video_app = UpdateVideo(window)

    # Set test inputs
    update_video_app.number_txt.insert(0, "01")
    update_video_app.new_rating.insert(0, "20")  # Invalid rating

    # Call the update_new_rating method
    update_video_app.update_new_rating()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the status label text was updated correctly
    assert update_video_app.status_lbl.cget("text") == "Rating must be between 0 and 10."

    # Check the printed output
    assert "Rating must be between 0 and 10." in captured.out


def test_update_video_invalid_key(capsys):
    # Mock the Tkinter window and UpdateVideo class
    window = tk.Tk()
    update_video_app = UpdateVideo(window)

    # Set test inputs
    update_video_app.number_txt.insert(0, "99")  # Non-existent key
    update_video_app.new_rating.insert(0, "5")

    # Call the update_new_rating method
    update_video_app.update_new_rating()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the status label text was updated correctly
    assert update_video_app.status_lbl.cget("text") == "Video 99 not found."

    # Check the printed output
    assert "Video 99 not found." in captured.out


def test_update_video_invalid_input(capsys):
    # Mock the Tkinter window and UpdateVideo class
    window = tk.Tk()
    update_video_app = UpdateVideo(window)

    # Set test inputs
    update_video_app.number_txt.insert(0, "01")
    update_video_app.new_rating.insert(0, "abc")  # Invalid input

    # Call the update_new_rating method
    update_video_app.update_new_rating()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the status label text was updated correctly
    assert update_video_app.status_lbl.cget("text") == "Invalid input. Please enter valid numbers."

    # Check the printed output
    assert "Invalid input. Please enter valid numbers." in captured.out
