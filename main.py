import sys
import csv
from statistics import mean


def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    with open(input_file_path)as f:
        reader =csv.reader(f, delimiter=',')
        for line in reader:
            newlist=[]
            for numbers in line:
                newlist.append(float(numbers))
            mean(newlist)
            print(mean(newlist))

if __name__ == "__main__":
    main()
