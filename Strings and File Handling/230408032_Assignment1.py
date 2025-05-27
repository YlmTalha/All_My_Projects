def process_logs(input_file):
    error_lines = []
    info_lines = []
    warning_lines = []
    error_count = 0

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            
            if "ERROR" in line:
                error_lines.append(line)
                error_count += 1
            if "INFO" in line:
                info_lines.append(line)
            if "WARNING" in line:
                warning_lines.append(line)

    with open("error_logs.txt", "w", encoding="utf-8") as f:
        f.writelines(error_lines)

    with open("info_logs.txt", "w", encoding="utf-8") as f:
        f.writelines(info_lines)

    with open("warning_logs.txt", "w", encoding="utf-8") as f:
        f.writelines(warning_lines)

    print("Total ERROR count:", error_count)

if __name__ == "__main__":
    input_file = r"server_logs.txt"
    process_logs(input_file)