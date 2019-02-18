import os
import time

import xml.etree.cElementTree as ET

def writeXML():
	#<?xml version="1.0"?>
	
	header = ET.Element("?xml",version="1.0")
	root = ET.Element("LabeledInt")
	doc = ET.SubElement(root, "label").text="test"
	_int = ET.SubElement(root, "_int").text="43"
	tree = ET.ElementTree(root)
	
	
	tree.write("filename.xml",xml_declaration ="xml")



def prepdir(d):
	os.system('rd '+d+' /S /Q')
	os.system('md '+d)

def hammer():
	mylist = [4,8,16,32]
	for x in mylist:
		y=x*x
		bas= ((y*y)+5)
		hu=y
		yaml = 'default:' \
		'\n'\
	    '    trainer: ppo' \
	    '\n'\
	    '    batch_size: '+str(2) +\
	    '\n'\
	    '    beta: 5.0e-3'\
	    '\n'\
	    "    buffer_size: "+str(200) +\
	    '\n'\
	    "    epsilon: 0.2"\
	    '\n'\
	    "    gamma: 0.99"\
	    '\n'\
	    "    hidden_units: "+str(hu) + \
	    '\n'\
	    "    lambd: 0.95"\
	    '\n'\
	    "    learning_rate: 3.0e-4"\
	    '\n'\
	    "    max_steps: 5.0e7"\
	    '\n'\
	    "    memory_size: 256"\
	    '\n'\
	    "    normalize: false"\
	    '\n'\
	    "    num_epoch: 3"\
	    '\n'\
	    "    num_layers: 2"\
	    '\n'\
	    "    time_horizon: "+str(20) +\
	    '\n'\
	    "    sequence_length: 64"\
	    '\n'\
	    "    summary_freq: 100"\
	    '\n'\
	    "    use_recurrent: false"\
	    '\n'\
	    "    use_curiosity: true"\
	    '\n'\
	    "    curiosity_strength: 0.01"\
	    '\n'\
		"    curiosity_enc_size: 128"
		'\n'
		

		

		print(x)
		
		run_id = str(x)
		env2= "radagast"
		env= "e:/ML/"+env2+"/"+env2
		worker=str(20+x-1)

		dd= 'hammer.'+worker	
		prepdir(dd)
		config_file = dd+"/Output.yaml"
		with open(config_file, "w") as text_file:
			text_file.write(yaml)		
		os.system('start mlagents-learn ' + config_file + ' --run-id=hammer_working_tsthu3' + run_id + ' --env=' + env + ' --train' + ' --worker-id=' + worker + '& pause')
		time.sleep(25)
hammer()
	#mlagents-learn config/trainer_config.yaml --run-id=%1 --env=e:\ML\%1\%1 --train
	#mlagents-learn config/trainer_config.yaml --run-id=radagastlight1 --env=e:\ML\radagast2\radagast2 --train --worker-id=3 --no-graphics