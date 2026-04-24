def format_errors(logs):
    lines = logs.split("\n")
    
    for line in lines:
        if "ERROR" in line:
            line = line.replace("ERROR at line", "Error: line ")
            line = line.replace(": ", " - ")
            print(line)
        elif "WARNING" in line:
            line = line.replace("WARNING at line", "Warning: line ")
            line = line.replace(": ", " - ")
            print(line)
logs = "ERROR at line12: missing ; \nWARNING at line15: unused variable"
format_errors(logs)