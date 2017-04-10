# -*- coding: utf-8 -*-
#
# Thida Aung
# Lab1 COEN 146 Wed
# writing the value of lists into a file using Time Division Multiplexing,
# Statistical Time Division Multiplexing and, reading back from the file using
# demultiplexing and print the list in tuple
# concept with given testcase template and sample cases

# TA Arman Elahi

# The part where we open the file and write the value of lists into a file using Time Division Multiplexing,
# Statistical Time Division Multiplexing
# extra credit if we print only one "No messages" per each machine using Statistical Time Division Multiplexing
def multiplex(messages):
        num = 0                 # to return total no# of message
        messages_left = True    # to check whether any more to read in each list
        start_pos = 0           #counter for items in each list

        with open('muxed_stream', 'w') as f:
          while messages_left :
            messages_left = False
            for i in range (len(messages)) :
                row_done = False
                for j in range(start_pos, start_pos + 5) :
                   if (j < len(messages[i])) :
                        #for as long as i elements in the messages list, write every 5 j elements from 0 to start_pos+ 5 items 
                        f.write("6040{} : {}\n".format(i, messages[i][j]))    #format: 6040,machine no#, index # of the list 
                        num += 1   # count only the messages not empty messages
                   else:
                        f.write("6040{} : No Messages\n".format(i))
                        row_done = True  # row is done once I see no more messages
                        break            # 
                
                messages_left = not row_done or messages_left
                
            start_pos += 5
        #return print(num)
        return num

# the part where we open the file, put the messages back into list
# print the list in tuple using demultiplexing


def demultiplex(input_file='muxed_stream'):
        row_list = [[], [], [], [], []]  #creating 5 lists to hold messages 
        with open('muxed_stream', 'r') as f:
            for line in f:     # going through the file line by line 
                machine_num = int(line[4]) #string to int
                if machine_num > 4:   #all other machines go to machine_num 4 as well 
                    machine_num = 4 
                message = line[8:].strip()  #message are 9th item if including space, line[7:] if excluding space in "6040{} : No Messages\n"
                if message != "No Messages":
                    row_list[machine_num].append(message) #until I see "No messages" keep storing in the list in order of machine_num
        print (tuple(row_list), "\n")
        return tuple(row_list)
        

## YOU DON'T NEED TO EDIT ANYTHING BELOW HERE

def test_case_1():
    """Testing Multiplexing with tons of messages."""

    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ('1', '2', '3', '4', '5', '6', '7', '8', '9'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'),
        ('1', '2', '3', '4'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')
    )

    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]

    multiplex(messages_copy)
    messages_received = demultiplex('muxed_stream')

    assert len(messages_received[0]) == 9
    assert len(messages_received[1]) == 17
    assert len(messages_received[2]) == 20
    assert len(messages_received[3]) == 16
    assert len(messages_received[4]) == 24

def test_case_2():
    """Testing multiplexing with tons of lost messages."""

    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ("This ain't", "no intro,", " this the entree"),
        (),
        (),
        (),
        ("Hit that", "intro with Kanye ", "and sound like Andre"),
        ("Tryna", "turn", "my", "baby", "mama", "to", "my", "fiancee"),
        ("She like"," music, she from", "Houston",  "like Auntie Yonce"),
        ("Man my daughter couldn't", "have a better mother"),
        ("If she ever", "find another, he", "better", "love", "her")
    )

    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]

    multiplex(messages_copy)
    messages_received = demultiplex('muxed_stream')

    assert len(messages_received[0]) == 3
    assert len(messages_received[1]) == 0
    assert len(messages_received[2]) == 0
    assert len(messages_received[3]) == 0
    assert len(messages_received[4]) == 22


if __name__ == '__main__':

    test_case_1()
    test_case_2()
