# FILE_LIST = 'file_list_5fold_main.pkl'
# ANNOTATION_PATH = 'k400_all.pkl'
DATA_ROOT = '../data/TSN_4fps_pad/'
TRAIN_ANNOTATION_PATH = DATA_ROOT + 'k400_mr345_train_min_change_duration0.3.pkl'
VAL_ANNOTATION_PATH = DATA_ROOT + 'k400_mr345_val_min_change_duration0.3.pkl'
TEST_ANNOTATION_PATH = 'test_len.json'

TRAIN_DATA_PATH = DATA_ROOT + 'train/'
VAL_DATA_PATH = DATA_ROOT + 'val/'
TEST_DATA_PATH = DATA_ROOT + 'test/'

PRED_PATH = 'k400_pred.pkl'
VISUAL_DATA_PATH = './visualizing/'
MODEL_SAVE_PATH = './models/'

DEVICE = 'cuda'

FEATURE_DIM = 4096 # 6400 for SF_TSN, 6912 for SF_TSN_TSP

FEATURE_LEN = 40 # DO NOT CHANGE
TIME_UNIT = 0.25 # DO NOT CHANGE

GAP = 16 # VALID LOCAL RANGE
CHANNEL_NUM = 4 
ENCODER_HIDDEN = 512 
DECODER_HIDDEN = 128

EVENT_LOSS_COEF = 0.5 
SHOT_LOSS_COEF = 0.2
WHOLE_LOSS_COEF = 0.3

AUX_LOSS_COEF = 0.5   

BATCH_SIZE = 64
LEARNING_RATE = 1e-4
DROP_RATE = 0.2

GLUE_PROB = 0.3 # Probability of glueing augmentation 

VAL_VIDEOS = ["01BFInmg3Zs", "77aDh42ddw8", "hlUDq3QKZo8", "jwO2HAMrCt4", "jwYikLyqs0k"] # files in visualizing folder

GAUSSIAN_KERNEL = 3
MAX_POOL_KERNEL = 5

THRESHOLD = 0.1 # Minimum score to be event boundary
SIGMA_LIST = [-1, 0.4] # List of sigma values of gaussian filtering in validation
TEST_THRESHOLD = 0.808
GOAL_SCORE = 0.815 # Train ends when validation score gets here

PATIENCE = 10 # Patience for early stopping

NUM_WORKERS = 0