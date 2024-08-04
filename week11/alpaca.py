from datasets import load_dataset

def is_valid(row):
    if row["input"]:
        return False

    if len(row["instruction"]) > 100:
        return False

    if len(row["output"]) > 500:
        return False

    return True

ds = load_dataset("tatsu-lab/alpaca")["train"]
print(len(ds))

ds = ds.filter(is_valid)
print(len(ds))

ds = ds.shuffle(seed=42).select(range(100))

ds = ds.select_columns(['instruction'])

ds.to_csv("alpaca.csv")
