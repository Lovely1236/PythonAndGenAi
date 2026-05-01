def log_exception():
    try:
        int("abc")
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(f"{type(e).__name__}: {e}")
log_exception()
