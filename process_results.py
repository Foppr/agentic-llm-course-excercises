import json
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def plot_valence_trajectory(
        source_path: str | Path,
        ax=None,
        label: str | None = None,
        persona: str | None = None,
        rolling_window: int | None = None,
):
    """Plot valence over simulated time nodes.json."""
    path = Path(source_path)
    records = []

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    nodes = data.values() if isinstance(data, dict) else data
    for node in nodes:
        if "valence" in node and node["valence"] is not None and "created" in node:
            records.append({
                "time": pd.to_datetime(node["created"]),
                "valence": float(node["valence"]),
                "type": node.get("type", ""),
            })

    if not records:
        raise ValueError(f"No valence records found in {path}")

    df = pd.DataFrame(records).sort_values("time").reset_index(drop=True)
    df = df[df["time"] <= pd.Timestamp("2023-02-13 08:30:00", tz=df["time"].dt.tz)]
    df = df[df["time"] >= pd.Timestamp("2023-02-13 07:00:00", tz=df["time"].dt.tz)]

    print(df)
    print(f'---------------------')

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 4))

    series_label = label or path.stem
    ax.plot(df["time"], df["valence"], marker="o", markersize=3, linewidth=1.2, alpha=0.75, label=series_label)

    if rolling_window and len(df) >= rolling_window:
        df["rolling"] = df["valence"].rolling(rolling_window, min_periods=1).mean()
        ax.plot(df["time"], df["rolling"], linewidth=2.2, label=f"{series_label} (rolling {rolling_window})")

    ax.axhline(0, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
    ax.set_xlabel("Simulated Time")
    ax.set_ylabel("Valence")
    ax.set_title("Valence Trajectory Over Simulated Time")
    ax.legend()
    ax.grid(True, alpha=0.25)
    plt.xticks(rotation=30)
    plt.tight_layout()
    return ax, df


fig, ax = plt.subplots(figsize=(11, 4.5))
plot_valence_trajectory(
    "simulation/model_a/personas/Bernard Lowe/bootstrap_memory/associative_memory/nodes.json",
    ax=ax,
    label="gpt-5-nano (Model A)",
    rolling_window=None,
)
plot_valence_trajectory(
    "simulation/model_b/personas/Bernard Lowe/bootstrap_memory/associative_memory/nodes.json",
    ax=ax,
    label="llama3.1:8b (Model B)",
    rolling_window=None,
)
plt.savefig('Valence trajectory gpt-5-nano llama3.1-8b.png')
plt.show()
