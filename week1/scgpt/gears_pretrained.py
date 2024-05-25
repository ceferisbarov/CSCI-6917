from gears import PertData, GEARS
from gears.utils import dataverse_download
from zipfile import ZipFile
import sys
sys.path.append('../')

from gears import PertData, GEARS

pert_data = PertData('./data')
pert_data.load(data_name = 'norman')
pert_data.prepare_split(split = 'simulation', seed = 1)
pert_data.get_dataloader(batch_size = 16, test_batch_size = 32)
## Download dataloader from dataverse
# dataverse_download('https://dataverse.harvard.edu/api/access/datafile/6979957', 'norman_umi_go.tar.gz')

## Download model from dataverse
dataverse_download('https://dataverse.harvard.edu/api/access/datafile/6979956', 'model.zip')

## Extract and set up model directory
with ZipFile(('model.zip'), 'r') as zip:
    zip.extractall(path = './')
    
model_name = 'gears_misc_umi_no_test'

## Extract and set up dataloader directory
import tarfile
with tarfile.open('norman_umi_go.tar.gz', 'r:gz') as tar:
    tar.extractall()
    
gears_model = GEARS(pert_data, device = 'cpu',
                        weight_bias_track = False,
                        proj_name = 'gears',
                        exp_name = model_name)

gears_model.load_pretrained('./model_ckpt')

print(gears_model.predict([['CNN1', 'CBL']]))
