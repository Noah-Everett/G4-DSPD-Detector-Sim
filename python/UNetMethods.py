import yaml

def get_config(paths_train, paths_val, 
               label_input='x', label_output='y', 
               num_workers=1,
               patch_shape=[40, 40, 40], stride_shape=[40, 40, 40],
               device='mps'):
    config = {
        "device": device,
        "model": {
            "name": "UNet3D",
            "in_channels": 6,
            "out_channels": 1,
            "layer_order": "crg",
            "f_maps": 32,
            "num_groups": 8,
            "final_sigmoid": True
        },
        "loss": {
            "name": "BCEDiceLoss",
            "ignore_index": None,
            "skip_last_target": True
        },
        "optimizer": {
            "learning_rate": 0.0002,
            "weight_decay": 0.00001
        },
        "eval_metric": {
            "name": "BoundaryAdaptedRandError",
            "threshold": 0.4,
            "use_last_target": True,
            "use_first_input": True
        },
        "lr_scheduler": {
            "name": "ReduceLROnPlateau",
            "mode": "min",
            "factor": 0.5,
            "patience": 30
        },
        "trainer": {
            "eval_score_higher_is_better": False,
            "checkpoint_dir": "/Users/noah-everett/Documents/FNAL/Geant4/USSD_Geant4/analysis/data/h5-UNet",
            "resume": None,
            "pre_trained": None,
            "validate_after_iters": 1000,
            "log_after_iters": 500,
            "max_num_epochs": 1000,
            "max_num_iterations": 150000
        },
        "loaders": {
            "num_workers": num_workers,
            "raw_internal_path": "/"+label_input,
            "label_internal_path": "/"+label_output,
            "train": {
                "file_paths": paths_train,
                "slice_builder": {
                    "name": "SliceBuilder", #"FilterSliceBuilder",
                    "patch_shape": patch_shape,
                    "stride_shape": stride_shape,
                    "skip_shape_check": True,
                    "threshold": 0.6,
                    "slack_acceptance": 0.01
                },
                "transformer": {
                    "raw": [
                        {"name": "Standardize"},
                        {"name": "RandomFlip"},
                        {"name": "RandomRotate90"},
                        {
                            "name": "RandomRotate",
                            "axes": [[2, 1]],
                            "angle_spectrum": 45,
                            "mode": "reflect"
                        },
                        {"name": "ElasticDeformation", "spline_order": 3},
                        {"name": "GaussianBlur3D", "execution_probability": 0.5},
                        {"name": "AdditiveGaussianNoise", "execution_probability": 0.2},
                        {"name": "AdditivePoissonNoise", "execution_probability": 0.2},
                        {"name": "ToTensor", "expand_dims": True}
                    ],
                    "label": [
                        {"name": "RandomFlip"},
                        {"name": "RandomRotate90"},
                        {
                            "name": "RandomRotate",
                            "axes": [[2, 1]],
                            "angle_spectrum": 45,
                            "mode": "reflect"
                        },
                        {"name": "ElasticDeformation", "spline_order": 0},
                        {"name": "StandardLabelToBoundary", "append_label": True},
                        {"name": "ToTensor", "expand_dims": False}
                    ]
                }
            },
            "val": {
                "file_paths": paths_val,
                "slice_builder": {
                    "name": "SliceBuilder", #"FilterSliceBuilder",
                    "patch_shape": patch_shape,
                    "stride_shape": stride_shape,
                    "skip_shape_check": True,
                    "threshold": 0.6,
                    "slack_acceptance": 0.01
                },
                "transformer": {
                    "raw": [
                        {"name": "Standardize"},
                        {"name": "ToTensor", "expand_dims": True}
                    ],
                    "label": [
                        {"name": "StandardLabelToBoundary", "append_label": True},
                        {"name": "ToTensor", "expand_dims": False}
                    ]
                }
            }
        }
    }

    return config

def save_config(config, path):
    with open(path, 'w') as f:
        yaml.dump(config, f)