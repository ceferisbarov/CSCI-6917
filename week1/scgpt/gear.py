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

gears_model.model_initialize(hidden_size = 2, decoder_hidden_size=2)

gears_model.train(epochs = 1, lr = 1e-3)

gears_model.save_model('test_model')
gears_model.load_pretrained('test_model')

