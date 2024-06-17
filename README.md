# Gesture-Based Navigation for Laptops Using Mediapipe and OpenCV

## Project Overview

This project is an implementation of [https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe) . 

This repo expands upon the gestures available by adding 6 more gesture options with each gesture linked to a corresponding action. 

This project leverages the Mediapipe object detection model to analyze hand gestures, enabling users to intuitively navigate their laptops without touching the mouse. By integrating OpenCV for real-time video processing and PyAutoGUI for simulating mouse and keyboard actions, this solution offers an accessible way to interact with a computer. This project is particularly beneficial for disabled individuals or those with faulty input devices, providing a seamless and user-friendly alternative for device interaction.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- **Gesture Recognition:** Detects and interprets various hand gestures to control mouse movements and clicks.
- **Real-Time Processing:** Uses OpenCV to process video feed from the webcam in real time.
- **Accessibility:** Offers an alternative input method for individuals with disabilities or broken input devices.
- **Customizable Gestures:** Easily expandable to include new gestures for additional commands.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/gesture-based-navigation.git
   cd gesture-based-navigation
   ```

2. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure your webcam is properly connected and accessible by OpenCV.**

## Usage

1. **Run the main script:**
   ```sh
   python app.py
   ```

2. **Perform gestures in front of your webcam to navigate your laptop.** The following gestures are recognized:
   - **Move Mouse:** Move your hand to control the mouse pointer.
   - **Click:** Pinch or tap gesture to simulate mouse clicks.
   - **Scroll:** Swipe gestures to simulate scrolling.

3. **Customize gestures** by modifying the gesture recognition logic in `gestures.py`.

## Dependencies

This project requires the following Python libraries:
- Mediapipe
- OpenCV
- PyAutoGUI
- Numpy

Install all dependencies with:
```sh
pip install mediapipe opencv-python pyautogui numpy
```

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**
   ```sh
   git checkout -b feature-branch
   ```
3. **Make your changes and commit them:**
   ```sh
   git commit -m 'Add some feature'
   ```
4. **Push to the branch:**
   ```sh
   git push origin feature-branch
   ```
5. **Create a pull request.**

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Mediapipe](https://mediapipe.dev/) for providing the hand tracking and gesture recognition model.
- [OpenCV](https://opencv.org/) for the robust computer vision library.
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) for the automation of GUI interactions.

---

By leveraging Mediapipe and OpenCV, this project provides an innovative solution for touch-free navigation on laptops, enhancing accessibility and usability for all users.
