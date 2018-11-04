# import serial
# import time
from guizero import App, TextBox, Text, PushButton, CheckBox 

def start():
	if(inputbox_bin1_colour.value == '1'):
		# ser.write(b'1')
		debugText.value = 'good input value'
	else:
		debugText.value = 'bad input value'


app = App(title="Rules UI", layout='grid', width=600, height=750)
title = Text(app, text="Magic the Gathering Card Sorter", size=16, grid=[250,10])
header_bin1 = Text(app, text="Bin 1:", size=14, grid=[2,50])
checkbox_bin1_colour = CheckBox(app, text="Colour: ", grid=[5,150], align='left')
inputbox_bin1_colour = TextBox(app, grid=[10,150], align='left')
checkbox_bin1_set = CheckBox(app, text="Set: ", grid=[5,160], align='left')
inputbox_bin1_set = TextBox(app, grid=[10,160], align='left')
checkbox_bin1_deck = CheckBox(app, text="Deck: ", grid=[5,170], align='left')
inputbox_bin1_deck = TextBox(app, grid=[10,170], multiline=True, align='left')
checkbox_bin1_garbage = CheckBox(app, text="Garbage: ", grid=[5,180], align='left')
inputbox_bin1_garbage = TextBox(app, grid=[10,180])
header_bin2 = Text(app, text="Bin 2:", size=14, grid=[2,250])
checkbox_bin2_colour = CheckBox(app, text="Colour: ", grid=[5,350], align='left')
inputbox_bin2_colour = TextBox(app, grid=[10,350], align='left')
checkbox_bin2_set = CheckBox(app, text="Set: ", grid=[5,360], align='left')
inputbox_bin2_set = TextBox(app, grid=[10,360], align='left')
checkbox_bin2_deck = CheckBox(app, text="Deck: ", grid=[5,370], align='left')
inputbox_bin2_deck = TextBox(app, grid=[10,370], multiline=True, align='left')
checkbox_bin2_garbage = CheckBox(app, text="Garbage: ", grid=[5,380], align='left')
inputbox_bin2_garbage = TextBox(app, grid=[10,380])
header_bin3 = Text(app, text="Bin 3:", size=14, grid=[2,450])
checkbox_bin3_colour = CheckBox(app, text="Colour: ", grid=[5,550], align='left')
inputbox_bin3_colour = TextBox(app, grid=[10,550], align='left')
checkbox_bin3_set = CheckBox(app, text="Set: ", grid=[5,560], align='left')
inputbox_bin3_set = TextBox(app, grid=[10,560], align='left')
checkbox_bin3_deck = CheckBox(app, text="Deck: ", grid=[5,570], align='left')
inputbox_bin3_deck = TextBox(app, grid=[10,570], multiline=True, align='left')
checkbox_bin3_garbage = CheckBox(app, text="Garbage: ", grid=[5,580], align='left')
inputbox_bin3_garbage = TextBox(app, grid=[10,580])
header_bin4 = Text(app, text="Bin 4:", size=14, grid=[2,650])
checkbox_bin4_colour = CheckBox(app, text="Colour: ", grid=[5,750], align='left')
inputbox_bin4_colour = TextBox(app, grid=[10,750], align='left')
checkbox_bin4_set = CheckBox(app, text="Set: ", grid=[5,760], align='left')
inputbox_bin4_set = TextBox(app, grid=[10,760], align='left')
checkbox_bin4_deck = CheckBox(app, text="Deck: ", grid=[5,770], align='left')
inputbox_bin4_deck = TextBox(app, grid=[10,770], multiline=True, align='left')
checkbox_bin4_garbage = CheckBox(app, text="Garbage: ", grid=[5,780], align='left')
inputbox_bin4_garbage = TextBox(app, grid=[10,780])
header_bin5 = Text(app, text="Bin 5:", size=14, grid=[2,850])
checkbox_bin5_colour = CheckBox(app, text="Colour: ", grid=[5,950], align='left')
inputbox_bin5_colour = TextBox(app, grid=[10,950], align='left')
checkbox_bin5_set = CheckBox(app, text="Set: ", grid=[5,960], align='left')
inputbox_bin5_set = TextBox(app, grid=[10,960], align='left')
checkbox_bin5_deck = CheckBox(app, text="Deck: ", grid=[5,970], align='left')
inputbox_bin5_deck = TextBox(app, grid=[10,970], multiline=True, align='left')
checkbox_bin5_garbage = CheckBox(app, text="Garbage: ", grid=[5,980], align='left')
inputbox_bin5_garbage = TextBox(app, grid=[10,980])


debugText = Text(app, 'debugText', grid=[300,1299])


# ser = serial.Serial('/dev/cu.wchusbserial14620', 9600) 
# time.sleep(2)
# print(ser.name) 


button = PushButton(app, start, text="start program", grid=[300,1300])


app.display()
# print(ser.name) 
# ser.close() 
