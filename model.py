def predict(x1, x2):
    try:
        x1 = float(x1)
    except (ValueError, TypeError):
        x1 = 0.0

    try:
        x2 = float(x2)
    except (ValueError, TypeError):
        x2 = 0.0

    return 1 if (x1 + x2) > 5.8 else 0