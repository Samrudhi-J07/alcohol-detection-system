import pandas as pd
import matplotlib.pyplot as plt

#Load dataset
df = pd.read_csv("alcohol_sensor_dataset.csv")

print(df.head())

print("Dataset Shape:", df.shape)

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

engine_counts = df["Engine_Status"].value_counts()
print("\nEngine Status Count:")
print(engine_counts)

plt.figure()
plt.bar(df["Person_ID"], df["Alcohol_ppm"])
plt.axhline(y=200, linestyle="--", label="Alcohol Limit")
plt.xlabel("Person ID")
plt.ylabel("Alcohol Level (ppm)")
plt.title("Alcohol Detection Sensor Readings")
plt.legend()
plt.show()

plt.figure()
engine_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Engine ON vs OFF Distribution")
plt.ylabel("")
plt.show()

