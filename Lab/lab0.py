# -*- coding: utf-8 -*-
# Thida Aung
# Lab1 COEN 146 Wed 
# TA Arman Clahi

def multiplex(messages):
        num = 0
        with open('muxed_stream', 'w') as f:
          for i in range(10):
            for k in range (len(messages)):
                for j in range(i*5, (i+1)*5):
                   if (j < len(messages[k])) :
                        #for as long as k elements in the messages list, if j count is less than each row (messages[k]) append j start from 0 to i+1 up to 5 items for 10 times(i)
                        f.write("6040{} : {}\n".format(k, messages[k][j]))
                        num += 1
                   else:
                        f.write("6040{} : No Messages\n".format(k))
                        #for value in messages:#msg = [list(msgs) for msgs in messages]
        return  num



                # We have three rows and flags row1_done, row2_done, row3_done       
                # messages_left = not (row1_done and row2_done and row3_done) = not row1_done or not row2_done or not row3_done
                # a = not row1_done or not row2_done
                # b = not row3_done
                # c = a or b


def demultiplex(input_file='muxed_stream'):
        lists = [[]*5]
        with open('muxed_stream', 'r') as f:
            for line in f:
                #print(line)
                if(line[0:5] == '60400'): #left is inclusive right is exclusive
                    lists[0].append(line[7:])
        print(lists)
        return tuple(lists)


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
