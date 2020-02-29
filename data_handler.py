import csv


def data_reader(filename, returned_line_idx):
	with open(filename, newline='') as f:
    		reader = csv.reader(f)
    		data = list(reader)
	return data[returned_line_idx]


if __name__ == "__main__":
	x = data_reader('pics_data.csv', 0)
	print(x)

	y = data_reader('words_data.csv', 0)
	print(y)
