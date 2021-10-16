<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SajawalHassan/volume_gesture_control_python">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Gesture Volume Control</h3>

  <p align="center">
    A volome controller to controll a device volume with you hands!
    <br />
    <a href="https://github.com/SajawalHassan/volume_gesture_control_python/issues">Report Bug</a>
    ·
    <a href="https://github.com/SajawalHassan/volume_gesture_control_python/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#how-it-works">How it works</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is a **mediapipe**, **opencv** and **python** project which are some great if not best programming/packeges for computer vision.

This project is **opensourced** so you can add **amazing** features more on that <a href="#contributing">here</a>

<p align="right"><a href="#top">back to top</a></p>

### Built With

This project is built with **mediapipe**, **opencv** and **python** the links to their documentation are listed below

- [python](https://python.org/)
- [open-cv](https://docs.opencv.org/)
- [mediapipe](https://google.github.io/mediapipe/)

<p align="right"><a href="#top">back to top</a></p>

## How it works

This project uses mediapipe as the algorithm to detect hands

1. Detect the hands which then returns 21 landmarks

Here is the list of landmarks it returns:

```py
   """The 21 hand landmarks."""
   WRIST = 0
   THUMB_CMC = 1
   THUMB_MCP = 2
   THUMB_IP = 3
   THUMB_TIP = 4
   INDEX_FINGER_MCP = 5
   INDEX_FINGER_PIP = 6
   INDEX_FINGER_DIP = 7
   INDEX_FINGER_TIP = 8
   MIDDLE_FINGER_MCP = 9
   MIDDLE_FINGER_PIP = 10
   MIDDLE_FINGER_DIP = 11
   MIDDLE_FINGER_TIP = 12
   RING_FINGER_MCP = 13
   RING_FINGER_PIP = 14
   RING_FINGER_DIP = 15
   RING_FINGER_TIP = 16
   PINKY_MCP = 17
   PINKY_PIP = 18
   PINKY_DIP = 19
   PINKY_TIP = 20
```

2. draw a circle on the THUMB_TIP and the INDEX_FINGER_TIP and a line between them

```py
# Drawing circle on thumb and index finger
cv.circle(img, pointA, 10, (255, 0, 0), -1)
cv.circle(img, pointB, 10, (255, 0, 0), -1)

# Drawing line between them
cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
```

3. calculate the distance between point a and point b via the coordinates of the thumb and minusing its coordinates with the index finger coordinates

```py
lenght = math.hypot(x1 - x2, y1 - y2)
```

And finally i set the master volume to the lenght

```py
call(["amixer", "-D", "pulse", "sset", "Master", f"{lenght_percentage}%"])
```

<p align="right"><a href="#top">back to top</a></p>

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Here are some of the prerequisites you need to work with the project

- python
- opencv
- mediapipe # You don't need this one but its reccomended in case you want to add things to the module

### Installation

1. [python](https://python.org/)

2. mediapipe

   ```sh
   pip install mediapipe
   ```

3. open-cv
   ```sh
   pip install opencv-python
   ```

<p align="right"><a href="#top">back to top</a></p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="#top">back to top</a></p>
