import sys
from pathlib import Path


def read_data(input_path):
    data = []
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) < 2:
                continue
            name = parts[0].strip()
            value = parts[1].strip()
            data.append((name, value))
    return data


def write_summary(output_path, summary_lines):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write('Name,Value\n')
        for line in summary_lines:
            file.write(f"{line}\n")


def summarize_data(data):
    summary = []
    for name, value in data:
        summary.append(f"{name},{value}")
    return summary


def main():
    if len(sys.argv) != 3:
        print('Usage: python starter-code.py <input_file> <output_file>')
        return

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f'Error: input file not found: {input_path}')
        return

    data = read_data(input_path)
    summary = summarize_data(data)
    write_summary(output_path, summary)
    print(f'Processed {len(data)} records and wrote summary to {output_path}')


if __name__ == '__main__':
    main()
