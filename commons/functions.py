import numpy as np

def softmax(w):
	e = np.exp(np.array(w, dtype=np.float32))
	dist = e / np.sum(e)
	return dist

def sign(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return 0

def formatRule(root):
	resp = ''
	
	for i in range(0, root):
		resp = resp + '   '
	
	return resp	

def storeRule(file,content):
	f = open(file, "a+")
	f.writelines(content)
	f.writelines("\n")

def createFile(file,content):
	f = open(file, "w")
	f.write(content)

def initializeParams(config):
	algorithm = 'ID3'
	enableRandomForest = False; num_of_trees = 5; enableMultitasking = False
	enableGBM = False; epochs = 10; learning_rate = 1
	enableAdaboost = False
	debug = False
	
	for key, value in config.items():
		if key == 'debug':
			debug = value
		elif key == 'algorithm':
			algorithm = value
		#---------------------------------	
		elif key == 'enableRandomForest':
			enableRandomForest = value
		elif key == 'num_of_trees':
			num_of_trees = value
		elif key == 'enableMultitasking':
			enableMultitasking = value
		#---------------------------------
		elif key == 'enableGBM':
			enableGBM = value
		elif key == 'epochs':
			epochs = value
		elif key == 'learning_rate':
			learning_rate = value
		#---------------------------------	
		elif key == 'enableAdaboost':
			enableAdaboost = value
			
	config['debug'] = debug
	config['algorithm'] = algorithm
	config['enableRandomForest'] = enableRandomForest
	config['num_of_trees'] = num_of_trees
	config['enableMultitasking'] = enableMultitasking
	config['enableGBM'] = enableGBM
	config['epochs'] = epochs
	config['learning_rate'] = learning_rate
	config['enableAdaboost'] = enableAdaboost
	
	return config
