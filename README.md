# alcohol-detection-system
🚗 Smart vehicle safety system that detects alcohol levels and automatically locks engine if limit exceeds. Built using Python, data simulation, and visualization.

# 🚗 Alcohol Detection & Smart Vehicle Locking System

## 📌 Project Overview

This project simulates a smart vehicle safety system that detects alcohol levels in a driver and automatically disables the vehicle ignition if the alcohol level exceeds a defined safety limit.

The system is designed to help prevent drunk driving using automated decision-making logic.

---

## 📊 Project Output

### 📈 Bar Graph
![Bar](https://raw.githubusercontent.com/your-username/alcohol-detection-system/main/images/bar.jpg)

### 📉 Chart
![Chart](https://raw.githubusercontent.com/your-username/alcohol-detection-system/main/images/chart.jpg)

### 🥧 Pie Chart
![Pie](https://raw.githubusercontent.com/your-username/alcohol-detection-system/main/images/pie.jpg)

### 📋 Data
![Data](https://raw.githubusercontent.com/your-username/alcohol-detection-system/main/images/data.jpg)


## 🎯 Objective

To develop a software-based model of an alcohol detection system that:

* Monitors alcohol levels (ppm)
* Compares with a legal safety threshold
* Controls vehicle engine status automatically

---

## ⚙️ Features

* Simulated alcohol sensor readings
* Defined threshold limit (200 ppm)
* Automatic engine ON/OFF control
* Dataset generation using Python
* Data analysis and visualization
* Safety remark system

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib

---

## 📂 Dataset Details

The dataset includes:

* **Person_ID** – Unique identifier
* **Alcohol_ppm** – Alcohol level
* **Limit_ppm** – Safety limit (200 ppm)
* **Engine_Status** – ON/OFF
* **Remark** – Safety message

---

## 🔄 System Workflow

1. Alcohol level is measured using a simulated sensor
2. Value is compared with threshold (200 ppm)
3. If level ≤ limit → Engine ON
4. If level > limit → Engine OFF
5. Data is stored in dataset for analysis

---

## 📊 Results & Analysis

* 66.7% cases exceeded alcohol limit → Engine OFF
* 33.3% cases were safe → Engine ON
* Automated system ensures safety without human intervention

---


## 🚀 Future Scope

* Real-time implementation using MQ-3 alcohol sensor
* Integration with microcontrollers (Arduino/ESP32)
* IoT-based vehicle monitoring system
* Mobile app integration for alerts

---

## 📌 Conclusion

This project demonstrates how software logic and data analysis can be used to build a real-world safety system that helps prevent accidents caused by drunk driving.

---

## 🙌 Acknowledgment

Developed as part of internship at SparkiIT.

---

## 👩‍💻 Author Samrudhi Jadhav

Your Name
