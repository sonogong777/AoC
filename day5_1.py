#!/usr/local/bin/python3

highest_seatid=0
try:
    with open('day5.input', 'r') as input_file:
        for line in input_file.readlines():
            row_init=[ *range(0,128) ]
            column_init=[ *range(0,8) ]
            for i in line[0:7]:
                if i == 'B':
                    new_row = row_init[int(len(row_init)/2):]
                    row_init = new_row
                else:
                    new_row = row_init[:int(len(row_init)/2)]
                    row_init = new_row    
            for i in line[7:10]:
                if i == 'R':
                    new_column = column_init[int(len(column_init)/2):]
                    column_init = new_column
                else:
                    new_column = column_init[:int(len(column_init)/2)]
                    column_init = new_column
            seat_id=(int(new_row[0])*8)+int(new_column[0])
            print(new_row,new_column,"seatID: ",seat_id)
            if seat_id > highest_seatid:
                highest_seatid = seat_id

except IOError:
    print("Something went wrong when attempting to read file.")

print(highest_seatid)