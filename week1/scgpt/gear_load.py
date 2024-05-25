import sys
sys.path.append('../')

from gears import PertData, GEARS

pert_data = PertData('./data')
pert_data.load(data_name = 'norman')
pert_data.prepare_split(split = 'simulation', seed = 1)
pert_data.get_dataloader(batch_size = 16, test_batch_size = 32)

gears_model = GEARS(pert_data, device = "cpu", 
                        weight_bias_track = False, 
                        proj_name = 'pertnet', 
                        exp_name = 'pertnet')

gears_model.load_pretrained('test_model')


print("==========================")
print(gears_model.predict([['CBL', 'CNN1'], ['FEV']]))
print(gears_model.predict([['CBL', 'CNN1'], ['FEV']])['CBL_CNN1'].shape)
print(gears_model.predict([['CBL', 'CNN1'], ['FEV']])['FEV'].shape)
print("==========================")
print(gears_model.GI_predict(['CBL', 'CNN1'], GI_genes_file=None))
print("==========================")
print(gears_model.predict([['CBL', 'CNN1']]))
