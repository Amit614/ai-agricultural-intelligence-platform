def handle_drift(score):
    return "RETRAIN" if score > 0.15 else "MONITOR"
