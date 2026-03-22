import numpy as np
import pandas as pd

np.random.seed(1)

num_samples = 30
alcohol_ppm = np.random.randint(50, 450, num_samples)
person_ids = [f"P{i+1}" for i in range(num_samples)]

df = pd.DataFrame({
    "Person_ID": person_ids,
    "Alcohol_ppm": alcohol_ppm
})

ALCOHOL_LIMIT = 200
df["Limit_ppm"] = ALCOHOL_LIMIT

def engine_decision(alcohol):
    if alcohol > ALCOHOL_LIMIT:
        return "OFF"
    else:
        return "ON"

df["Engine_Status"] = df["Alcohol_ppm"].apply(engine_decision)


def remark(alcohol):
    if alcohol > ALCOHOL_LIMIT:
        return "Limit Exceeded - Vehicle Locked"
    else:
        return "Safe - Vehicle Can Start"

df["Remark"] = df["Alcohol_ppm"].apply(remark)

print("\nFinal Alcohol Detection Dataset:\n")
print(df)

df.to_csv("alcohol_sensor_dataset.csv", index=False)
print("\nDataset saved successfully!")
